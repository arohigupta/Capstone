from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
#im
import json
import requests

import avro.schema
import avro.io
import io

schema = avro.schema.parse("""{"namespace": "com.cisco.pnda",
 "type": "record",
 "name": "PndaRecord",
 "fields": [
     {"name": "timestamp",   "type": "long"},
     {"name": "src",         "type": "string"},
     {"name": "host_ip",     "type": "string"},
     {"name": "rawdata",     "type": "bytes"}
 ]
}""")

reader = avro.io.DatumReader(schema)

ssc = StreamingContext(sc, 10)

def avroDecoder(s):
    if s is None:
        return None
    byte_reader = io.BytesIO(s)
    decoder = avro.io.BinaryDecoder(byte_reader)
    return reader.read(decoder)

kafkaParams = {"metadata.broker.list": "192.168.56.101:9092", "auto.offset.reset": "largest"}

topic = "collectd"

kafkaStream = KafkaUtils.createDirectStream(ssc,[topic],kafkaParams, valueDecoder=avroDecoder)

kafka_rdd = kafkaStream.map(lambda x:x[1])

def transform(rdd):

    def openTsdbApiPut(data):
        host = 'localhost:4242'
        openTsdbUrl = 'http://' + host + '/api/put/details'
        r = requests.post(openTsdbUrl, data = json.dumps(data))
        r.raise_for_status()

    items = rdd.collect()
    for item in items:
        message = json.loads(item['rawdata'])
        data = []
        for name in 'inPkts', 'outPkts':
            metric = {
                "metric": name,
                "timestamp": item['timestamp'],
                "value": message[name],
                "tags": {
                    "node": item['host_ip'],
                    "interface": message['interface']
                }
            }
            data.append(metric)
        openTsdbApiPut(data)
    if len(items) > 0:
        print "Stored metrics for {} samples".format(len(items))

kafka_rdd.foreachRDD(lambda rdd: transform(rdd))

ssc.start()
ssc.awaitTermination()

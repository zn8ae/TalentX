from kafka import KafkaConsumer
import time
import json


kc = None

while kc is None:
    try:
        kc = KafkaConsumer('co-views', group_id='co-views', bootstrap_servers=['kafka:9092'])
    except:
        time.sleep(5)

for msg in kc:
    msg_json = json.loads(msg.value.decode('utf-8'))
    with open('/app/data/access.log', 'a') as file:
        file.write("\n")
        file.write(msg_json["username"])
        file.write("\t")
        file.write(str(msg_json["id"]))
    file.close()
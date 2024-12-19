import json

import paho.mqtt.client as mqtt
import time


# 定义回调函数，用于处理连接事件
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed with code", rc)


# 定义回调函数，用于处理发布消息的确认
def on_publish(client, userdata, mid):
    print("Message Published")


# 设置 MQTT 代理的地址和端口
broker_address = "10.30.30.87"
port = 21883
username = "edgegateway@gateway3"
password = "76dd793b8c6dc88fe3d073b49086ff6f770f093b30906a28fa48e9beec8182fa"


# 创建 MQTT 客户端实例
client = mqtt.Client()
client.username_pw_set(username, password)
# 设置连接和发布消息的回调函数
client.on_connect = on_connect
client.on_publish = on_publish

# 连接到 MQTT 代理
client.connect(broker_address, port, keepalive=60)

# 启动 MQTT 客户端的消息循环
client.loop_start()
current_time_seconds = time.time()
message_body = {
    "operate": "EVENT_UP",
    "operateId": 1,
    "data": [{
        "pk": "CY6BoIxBlgG",
        "devId": "dev001",
        "identifier": "mock_event_info",
        "time": int(current_time_seconds * 1000),
        "params": {
            "out_double_event_info": "35"
        }
    }]
}
json_message = json.dumps(message_body)
try:
    while True:
        # 发布消息到指定主题

        topic = "up/dev/edgegateway/gateway3"
        client.publish(topic, json_message)
        print(f"Published message: {json_message} to topic: {topic}")

        # 等待一段时间
        time.sleep(60)

except KeyboardInterrupt:
    # 在收到中断信号时，断开连接并停止消息循环
    print("Disconnecting from MQTT broker")
    client.disconnect()
    client.loop_stop()

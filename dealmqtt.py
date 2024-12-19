import paho.mqtt.client as mqtt
import pymysql
from datetime import datetime

# 配置MQTT连接信息
mqtt_broker = "10.30.30.87"
mqtt_port = 21883
mqtt_topic = "nup/system/+/event/+/+"
mqtt_username = "admin"
mqtt_password = "1Sysc0re!"

# 配置MySQL数据库连接信息
db_host = "10.30.30.87"
db_port = 23306
db_user = "root"
db_password = "ZljIsysc0re123"
db_name = "yizhan"


# 回调函数，处理收到的MQTT消息
def on_message(client, userdata, msg):
    try:
        # 解析收到的消息
        payload = msg.payload.decode("utf-8")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 连接到MySQL数据库
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            port=db_port
        )
        cursor = conn.cursor()

        # 存储到MySQL数据库
        cursor.execute("INSERT INTO mqtt_data (topic, payload, timestamp) VALUES (%s, %s, %s)",
                       (msg.topic, payload, timestamp))
        conn.commit()
        conn.close()

        print(f"Received message: Topic={msg.topic}, Payload={payload}, Timestamp={timestamp}")

    except Exception as e:
        print(f"Error processing message: {str(e)}")


# 创建MQTT客户端
client = mqtt.Client()
client.username_pw_set(username=mqtt_username, password=mqtt_password)
client.on_message = on_message

# 连接到MQTT代理
client.connect(mqtt_broker, mqtt_port, 60)
client.subscribe(mqtt_topic)

# 循环等待消息
client.loop_forever()

if __name__ == '__main__':
    on_message()

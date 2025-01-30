import socket # библиотека для 

target_host = "0.0.0.0"
target_port = 9998

#обьект сокета
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - использование IPv4 | SOCK_STREAM - использоваие TCP 

client.connect((target_host,target_port))

#отправка данных 
client.send(b"HI it's me!\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()

import socket 

target_host = "www.google.com"
target_port = 80

#обьект сокета
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - использование IPv4 | SOCK_STREAM - использоваие TCP 

client.connect((target_host,target_port))

#отправка данных 
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()

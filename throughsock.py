import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data=mysock.recv(514)
	l=len(data)
	if l<1:
		break
	p=data.decode()
	print(p)

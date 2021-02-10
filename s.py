import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.sagartours.co.in",80))
cmd="GET http://www.sagartours.co.in/contact.php HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
	data=mysock.recv(512)
	l=len(data)
	if l<1:
		break
	p=data.decode()
	print(p)
mysock.close()

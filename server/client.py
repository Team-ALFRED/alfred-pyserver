import socket
import time
import sys

HOST, PORT = "192.168.0.3", 5001
TIMEOUT = 5.0
DEBUG = True

def debug(msg):
    if DEBUG:
	    if isinstance(msg, bytes):
	    	sys.stdout.buffer.write(msg + b"\n")
	    	sys.stdout.buffer.flush()
	    else:
	    	print(msg)

def req(item):
	debug(b"Sending request for " + item)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(item, (HOST, PORT))
	sock.close()

def ack():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.settimeout(TIMEOUT)
	sock.bind(("0.0.0.0", PORT))
	try:
		datagram = sock.recv(1024)
		sock.close()
	except socket.timeout:
		return False
	return True

if __name__ == "__main__":
	while True:
		item = input("Select an item (Water, Granola): ")
		item = item.encode('ascii')
		try:
			req(item)
			if ack():
				debug(b"ack")
			else:
				debug(b"nack")
		except Exception as e:
			print(e)

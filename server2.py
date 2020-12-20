import socket
import subprocess
import sys
import os
from _thread import *

host=''
port=8080
ThreadCount=0

serversoc=socket.socket()
print("Socket Created")

serversoc.bind((host, port))
print("Socket bind in port ")

serversoc.listen(5)
print("Waiting for Client! ")

def threaded_client(connection,address):
	while True:
		raw=connection.recv(2048)
		comm=raw.decode("utf-8")
		first=comm.split()[0]

		if comm == "quit":
			connection.close()
			break

		elif comm == "cd":
			dir=comm[comm.index("")+1:]
			if dir == "":
				os.chdir("")
			else :
				os.chdir(os.path.join(os.getcwd(), dir))
			cwd=os.getcwd()
			output="Directory: "+cwd

		elif comm == "ls":
			dir=os.listdir(os.getcwd())
			output=str(dir)

		elif first == "echo":
			print(comm[5:])

		connection.send(str.encode(output))

while True:
	c,address=serversoc.accept()
	print("Client connected from: "+str(address))
	print("\n")
	start_new_thread(threaded_client,(c,address))
	ThreadCount += 1
	print('How many user: '+ str(ThreadCount))

serversoc.close()

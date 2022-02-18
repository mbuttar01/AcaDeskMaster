# first of all import the socket library
import socket
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='localhost')
mycursor = cnx.cursor()
mycursor.execute("USE test_aca;")


# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(4096).decode("utf-8")
    # output received data
    print("Data: %s" % data)
    mycursor.execute(f"SELECT * FROM rfid WHERE id = {int(data)}")
    results = mycursor.fetchall()
    print(results)
    c.send(str(results).encode('utf-8')+b' ')

    c.close()



exit(0)

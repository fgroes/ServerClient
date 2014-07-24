import socket
import time


class State(object):
    Idle = 0
    Active = 1
    

class Server(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.state = State.Idle
        self.socket = None
        self.connection = None
        self.address = None

    def start(self):
        while True:
            if self.state == State.Idle:
                print(self.state)
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.bind((self.host, self.port))
                self.socket.listen(1)
                self.connection, self.address = self.socket.accept()
                print('Connection {0} ... OPEN'.format(self.address))
                self.state = State.Active
            elif self.state == State.Active:
                print(self.state)
                data = self.connection.recv(2048)
                if data == 'disconnect':
                    self.connection.close()
                    self.state = State.Idle
                else:
                    print(data)
                    self.connection.sendall(data)
            time.sleep(0.5)



if __name__ == '__main__':
    s = Server('', 50011)
    s.start()

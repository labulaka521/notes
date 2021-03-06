from __future__ import print_function
import sys
from gevent import socket


address = ('127.0.0.1',9000)
message = ' '.join(sys.argv[1:])
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.connect(address)
print('Sending %s bytes to %s:%s' % ((len(message),) + address))
sock.send(message.encode())
data, address = sock.recvfrom(8192)
print('%s:%s got %r' % (address + (data,)))
sock.close()

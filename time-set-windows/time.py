import socket
import struct
import sys
import time
import datetime
import os

def RequestTimefromNtp(addr='0.de.pool.ntp.org'):
    REF_TIME_1970 = 2208988800  # Reference time
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (addr, 123))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= REF_TIME_1970
    return t

if __name__ == "__main__":
    print('script started, connecting to time server...')
    timestamp = RequestTimefromNtp()
    print('connection done!')
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)
    print('setting date to', datetime_obj.strftime('%d-%m-%Y'))
    os.system('date ' + datetime_obj.strftime('%d-%m-%Y'))
    print('setting time to', datetime_obj.strftime('%H:%M:%S'))
    os.system('time ' + datetime_obj.strftime('%H:%M:%S'))
    print('done!')

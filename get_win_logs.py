import os
import win32evtlog
import socket

def main():
    host = get_host()
#    get_log(server, log_type)

def get_log (host, log_type):
    print ("Hello")

def get_host ():
    host_name = socket.gethostname()
    print("Hostname :  ",host_name)
    return host_name


if __name__ == '__main__':
    main()

import socket

def ISopen(ip,port):
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cnct=s.connect_ex((ip,int(port)))
    s.close()
    return cnct

print("enter IP you want to check: ")
ip=input()
p=1
print("open ports: ")
while (p < 1024):
    if (ISopen(ip, p) == 0):
        print(p, "\n")
    p = p + 1

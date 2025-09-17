import socket as sk
import requests as req

#Internal IP
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sock.connect(("www.google.com", 443))
print('Internal IP: ', sock.getsockname()[0])
sock.close()

# External IP
outside_addr = req.get('https://api.ipify.org').text
print('External IP: ', outside_addr)


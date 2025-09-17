# import socket as sk
# Addr = sk.gethostbyname(sk.gethostname)
# print(Addr)

# IpAddr = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
# IpAddr.connect(("www.google.com", 443))
# print(IpAddr.getsockname()[0])


import socket as sk

try:
    # Get the local IP address
    Addr = sk.gethostbyname(sk.gethostname())
    print(f"Local Hostname IP: {Addr}")

    # Create a socket object and connect to Google
    IpAddr_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    IpAddr_socket.connect(("www.google.com", 443))

    # Get the IP address used for the connection
    connected_ip = IpAddr_socket.getsockname()[0]
    print(f"Connected IP to www.google.com: {connected_ip}")

    IpAddr_socket.close()

except sk.gaierror as e:
    print(f"Address-related error connecting to www.google.com: {e}")
except sk.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
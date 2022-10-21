import socket
import os
from time import sleep

s = socket.socket()
s.bind(("0.0.0.0", 40008))
s.listen(10) # accepteert tot 10 connecties

tap = """
        ====
     /'\_||_
     ( )___  `.
     \./  `=='
           |||
           |||
            |||
"""            
tap1 = """
        ====
     /'\_||_
     ( )___  `.
     \./  `=='
           |||
            |||
           |||
"""
tap2 = """
        ====
     /'\_||_
     ( )___  `.
     \./  `=='
           |||
           |||
          |||
"""

def spacetap():
    loading = "#"
    for i in range(20):
        
        print(tap)
        print(loading)
        sleep(0.159)
        os.system("clear")
        print(tap1)
        print(loading)
        sleep(0.159)
        os.system("clear")
        print(tap2)
        sleep(0.159)
        print(loading)
        os.system("clear")
        loading+="#"
    print("File succesfully received!")
    sleep(2)
    os.system("clear")
i = 1
while True:
    print("Printer ready for receiving")
    sc, address = s.accept()
    print(f"Connection from: {address}")
    filename = 'file_'+str(i)
    f = open(filename, "wb") ##replace first two with result of function to receive name
    i += 1
    try:
        l = sc.recv(1024)
        while l:
           f.write(l)
           l = sc.recv(1024)
        f.close()
        sc.close()
    except:
        pass
    spacetap()
    
s.close()
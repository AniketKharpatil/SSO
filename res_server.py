import socket
import rsa_module as rsa
import hashlib
import pyfiglet
import gui


print(pyfiglet.figlet_format("Res-Server", font="slant"))


bufferSize = 4096
Address= ("127.0.0.1", 20001)
# Create a UDP socket at client side
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#start the process
sock.sendto("Resource server connected".encode(), Address)
print("connected to authentication server")


def verify():
        # receiving keys
        d = int(sock.recv(bufferSize).decode())
        N = int(sock.recv(bufferSize).decode())
        g = int(sock.recv(bufferSize).decode())
        n = int(sock.recv(bufferSize).decode())
        e = int(sock.recv(bufferSize).decode())

        n1 = rsa.generateLargePrime(32)
        n2 = rsa.generateLargePrime(32)
        n3 = rsa.generateLargePrime(32)

        k = rsa.generateLargePrime(32)

        Z = pow(g, k, n)
        # print("Z : ",Z)

        ID_serviceprov = str("harsh12345678")
        # sock.sendto(ID_serviceprov.encode(),Address)

        concatu = str(Z) + str(n1) + str(ID_serviceprov)
        u = hashlib.md5(concatu.encode()).hexdigest()
        concatv = str(u) + hashlib.md5(u.encode()).hexdigest()
        # print(concatv)
        # byteconcatv=int.from_bytes(concatv.encode(),"big")
        # msg=5100842592844213720512507 print(msg)
        # v=pow(msg,d,N)

        v = rsa.encrypt(d, N, str(concatv))
        # print("v is: ",v)

        # send z,v,n2 to client
        sock.sendto(str(Z).encode(), Address)
        sock.sendto(str(v).encode(), Address)
        sock.sendto(str(n2).encode(), Address)
        sock.sendto(str(n3).encode(), Address)
        sock.sendto(str(concatv).encode(), Address)
        sock.sendto(ID_serviceprov.encode(), Address)

        print("Z,v,n2 sent to client successfully")

        # Receive w x y from client
        W = (sock.recv(bufferSize).decode())
        X = (sock.recv(bufferSize).decode())
        #Y = (sock.recv(bufferSize).decode())
        USER_ID = (sock.recv(bufferSize).decode())

        # calculating K
        kiS = pow(int(W), k, N)
        concatKiS = str(kiS) + str(ID_serviceprov)
        KiS = hashlib.md5(concatKiS.encode()).hexdigest()

        # print("Kis: ",KiS)

        '''
        decimal_KiS=int.from_bytes(KiS.encode(), "big")
        concat_Y=str(ID_serviceprov)+str(n3)+str(n2
        Decrypted_Y=rsa.decrypt(decimal_KiS,Y,N)
        print(Decrypted_Y)'''

        hash_result = hashlib.md5(USER_ID.encode()).hexdigest()
        STD = hash_result + USER_ID
        STD_pow = int.from_bytes(STD.encode(), "big")

        print("std=", STD_pow)

        # power_of_STD=hashlib.md5((str(KiS)+str(W)+str(n2)).encode()).hexdigest()
        # decimal_power_of_STD=int.from_bytes(power_of_STD.encode(), "big")
        '''
        #lhs=rsa.decrypt(decimal_power_of_STD,N,str(STD))
        #print(lhs)
        x=hashlib.md5(X.encode()).hexdigest()
        x=int.from_bytes(x.encode(),"big")
        print(e)
        #decrypted x=signature
        rhs=rsa.decrypt(e,N,str(x))
        print(rhs)
        '''

        V = hashlib.md5(str(n3).encode()).hexdigest()
        sock.sendto(str(V).encode(), Address)

while True:
    req = sock.recv(bufferSize).decode()
    if req == 'y':
            verify()
            gui.run_service()
    if req == 'yes':
            gui.run_service()









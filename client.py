import socket
import rsa_module as rsa
import hashlib
from tkinter import *
root=Tk()

Label(root, text='Enter the Username for Registration: ').pack(padx=10,pady=10)
username=Entry(root)
username.pack(padx=10,pady=10)

#def register_auth():
Address = ("127.0.0.1", 20001)
bufferSize = 4096
# Create a UDP socket at client side
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def register_auth():
    USER_ID = username.get()
    # Send USER_ID to server
    sock.sendto(USER_ID.encode(), Address)
    # get signature
    msgFromServer = sock.recv(bufferSize)
    print("Server: ", msgFromServer.decode())

    msg2 = sock.recv(bufferSize)
    print("Server: ", msg2.decode())
    # receive signature
    S = int(sock.recv(bufferSize).decode())

    def verification():
        response = 'y'
        sock.sendto(response.encode(), Address)
        # receive keys
        e = int(sock.recv(bufferSize).decode())
        N = int(sock.recv(bufferSize).decode())
        g = int(sock.recv(bufferSize).decode())
        n = int(sock.recv(bufferSize).decode())

        t = rsa.generateLargePrime(32)
        # print("t is:",t)
        W = pow(g, t, n)
        # print("W ",W)

        # receive v ,Z,n3,n2 from server
        Z = (sock.recv(bufferSize).decode())
        v = (sock.recv(bufferSize).decode())
        n2 = int(sock.recv(bufferSize).decode())
        n3 = int(sock.recv(bufferSize).decode())
        concatv = sock.recv(bufferSize).decode()
        # RECV SERVER'S ID
        ID_server = sock.recv(bufferSize).decode()
        # --------------------------------------------------------------------------------------------------------------------------------
        print("Server ID: ", ID_server)

        # print("z:",Z)
        v1 = rsa.decrypt(e, N, v)
        # ---------------------------------------------------------------------------------------------
        if concatv == v1:
            print("\nValues matched, SP is verified")
        else:
            print(" authentication invalid ")

        kiS = pow(int(Z), t, N)
        concatkiS = str(kiS) + str(ID_server)
        KiS = hashlib.md5(concatkiS.encode()).hexdigest()

        concat_power = str(KiS) + str(W) + str(n2)
        power_of_S = hashlib.md5(concat_power.encode()).hexdigest()
        dec_power = int(power_of_S, 16)
        # changed here
        X = rsa.encrypt(e, N, S)
        # encrypted signature==x
        # ------------------------------------------------------------------------------------------------
        print("Proof of identity: ", X)

        # Y Using encryption
        #concat_Y = str(USER_ID) + str(n3) + str(n2)
        decimal_KiS = int.from_bytes(KiS.encode(), "big")
        #Y = rsa.encrypt(decimal_KiS, N, concat_Y)

        # sending w,x,y to service prov

        sock.sendto(str(W).encode(), Address)
        sock.sendto(str(X).encode(), Address)
        #sock.sendto(str(Y).encode(), Address)

        v_dash = hashlib.md5(str(n3).encode()).hexdigest()
        V = sock.recv(bufferSize).decode()
        # ------------------------------------------------------------------------------------------------
        if v_dash == V:
            print("Verification successful")
        else:
            print("Verification failed")

    Button(root, text="Login", command=verification).pack(padx=10, pady=10)
def new_window():
    root_new = Tk()
    sock.sendto('yes'.encode(),Address)
    sign = Entry(root_new)
    sign.pack(padx=10, pady=10)
    sign_id = sign.get()
    def send_sign():

        sock.sendto(sign_id.encode(),Address)

    Label(root_new, text='Enter the Signature: ').pack(padx=10, pady=10)
    Button(root_new, text="LOGIN NOW", command=send_sign).pack(padx=10, pady=10)
    Label(root_new, text=sock.recv(bufferSize).decode()).pack(padx=10, pady=10)
    root_new.mainloop()




Button(root,text="Register",command=register_auth).pack(padx=10,pady=10)
Label(master=root, text="Already registered, click login button below", wraplength=400).pack()
Button(root,text="log in",command=new_window).pack(padx=10,pady=10)
root.mainloop()
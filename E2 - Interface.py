import requests
from tkinter import *

tela = Tk()
tela.title("Login")
tela.geometry("800x600")
tela.configure(background="#FFF")

def apaga_texto():
    array_login = v_info.get().split(";")
    if len(array_login) > 1:
        print("Email: " +array_login[0] +"\nSenha: "+array_login[1])
        # print(response.json()['city'])
        
        
v_info = StringVar()

screen_frame = Frame(tela)
screen_frame.place(relx=0.5, rely=0.5, anchor="s")
screen_frame.configure(background="#FFF")

e_info = Entry(screen_frame, textvariable=v_info, background="#EEF", width=50)

button = Button(screen_frame, text="Login", command=apaga_texto)

texto_final = Label(screen_frame, text="")

e_info.grid(column=0, row=0)
button.grid(column=0, row=1,pady=20)

texto_final.grid(column=0, row=3)

tela.mainloop()

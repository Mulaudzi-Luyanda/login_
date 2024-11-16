from tkinter import *

from tkinter import messagebox


def login():
	username="Luyanda"
	password="12345"

	if username_entry.get()==username and password_entry.get()==password:
		messagebox.showinfo(title="Login success",message="You successfully logged in.")
	else:
		messagebox.showerror(title="Login unsuccessfully",message="Invalid login, please re-try.")

		

Lulu=Tk()
Lulu.title("Login Form")
Lulu.geometry("340x440")
Lulu.configure(bg="#626567")

frame=Frame(bg="#626567")


login_label=Label(frame,text="Login",fg="#3498db",bg="#626567",font=("Arial",30))
username_label=Label(frame, text="Username",bg="#626567",font=("Arial",15))
username_entry=Entry(frame,font=("Arial",15))
password_entry=Entry(frame, show="*",font=("Arial",15))
password_label=Label(frame,text="Password",bg="#626567",font=("Arial",15))
login_btn=Button(frame,text="Login",bg="#3498db",fg="#fdfefe",font=("Arial",15),command=login)

login_label.grid(row=0,column=1,sticky="news",pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
login_btn.grid(row=3,column=1,pady=30)

frame.pack()






Lulu.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Formularz")
root.geometry("720x720")

img = tk.PhotoImage(file='img.png')
l = tk.Label(root, image=img, height=200, width=200)
l.grid(row=0, column=0)

l2 = tk.Label(root, text='Formularz', font='Arial 20 bold')
l2.grid(row=1, column=0)

l3 = tk.Label(root, text='Nazwa użytkownika: ', font='Arial 20 bold')
l3.grid(row=2, column=0)
en1_txt = tk.StringVar()
en1 = tk.Entry(root, text=en1_txt)
en1.grid(row=2, column=1)

l4 = tk.Label(root, text='Hasło: ', font='Arial 20 bold')
l4.grid(row=3, column=0)
en2_txt = tk.StringVar()
en2 = tk.Entry(root, text=en2_txt, show='*')
en2.grid(row=3, column=1)

l5 = tk.Label(root, text='Wiek: ', font='Arial 20 bold')
l5.grid(row=4, column=0)
sl =tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
sl.grid(row=4, column=1)

ll = tk.Label(root, text='Państwo: ', font='Arial 20 bold')
ll.grid(row=4, column=2)
values = ['Polska', 'Niemcy', 'Francja']
combobox = ttk.Combobox(root, values=values)
combobox.bind("<<ComboboxSelected>>", combobox.get())
combobox.grid(row=4, column=3)

l7 = tk.Label(root, text='Płeć', font='Arial 20 bold')
l7.grid(row=5, column=0)
gender_var = tk.StringVar()
gender_var.set("Kobieta")
r1 = tk.Radiobutton(root, text="Kobieta", variable=gender_var, value="Kobieta")
r1.grid(row=5, column=1)
r2 = tk.Radiobutton(root, text='Mężczyzna', variable=gender_var, value='Mężczyzna')
r2.grid(row=5, column=2)
btn = tk.Button(root, text='Zaloguj', command=lambda: zal())
btn.grid(row=6, column=0)

l6 = tk.Label(root, text='', font='Arial 20 bold')

def logout():
    root.destroy()

def zal():
    user_name=en1_txt.get()
    passw = en2_txt.get()
    age = sl.get()
    gen = gender_var.get()
    val = combobox.get()

    if user_name!='User123' or passw!='1234' or age!=31 or gen!='Mężczyzna' or val!='Polska':
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        messagebox.showerror("Error", "Podałeś złe dane")
        raise ValueError('Podałeś złe dane')
    l3.config(text=f"Zalogowano")
    l4.config(text = f"Nazwa użytkownika: {en1_txt.get()}")
    l5.config(text = f"Hasło: {en2_txt.get()}")
    l5.grid(row=5, column=0)
    l6.config(text=f"Wiek: {sl.get()}")
    l6.grid(row=6, column=0)
    l7.config(text=f"Płeć: {gender_var.get()}")
    l7.grid(row=7, column=0)
    ll.config(text=f"Państwo: {combobox.get()}")
    ll.grid(row=8,column=0)
    en1.destroy()
    en2.destroy()
    btn.config(text="Wyloguj", command=lambda: logout())
    sl.destroy()
    r1.destroy()
    r2.destroy()
    combobox.destroy()
    btn.grid(row=9,column=0)

root.mainloop()
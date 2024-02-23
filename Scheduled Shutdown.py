import tkinter as tk
from tkinter import ttk
from time import sleep
from os import system


root = tk.Tk()
root.title("Scheduled Shutdown")

root.configure(bg='black')
root.minsize(400, 250)


frame = tk.Frame(root)
frame.pack(expand=True)
frame.configure(bg='black')

entry1 = tk.Entry(frame, font=("Arial", 14), width=10, justify="center", cursor="arrow")
entry2 = tk.Entry(frame, font=("Arial", 14), width=10, justify="center", cursor="arrow")
entry1.configure(background="gray",foreground="white")
entry2.configure(background="gray",foreground="white")

label1 = tk.Label(frame, text="Hour", font=("Arial", 14))
label2 = tk.Label(frame, text="Minute", font=("Arial", 14))
label1.configure(bg='black',foreground="white")
label2.configure(bg='black',foreground="white")

label1.grid(row=0, column=0, padx=5, pady=(50,5))
entry1.grid(row=1, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=(50,5))
entry2.grid(row=1, column=1, padx=5, pady=5)




def go_button_clicked():
    hour = entry1.get() or 0
    minute = entry2.get() or 0
    val = int(hour)*60*60 + int(minute)*60
    print(val)
    system(f"shutdown /s {(var1.get() and "/f") or ""} /t {val}")


def cancel_shutdown():
    system(f"shutdown /a")


button_frame = tk.Frame(root)
button_frame.pack(expand=True, pady=(20, 50))

var1 = tk.IntVar()
c = tk.Checkbutton(button_frame, text='Force shutdown',variable=var1, onvalue=1, offvalue=0)
c.pack()

go_button = tk.Button(button_frame, text="GO", command=go_button_clicked, width=15, height=2)
go_button.configure(background="black", foreground="white")
go_button.pack(padx=1, pady=1, anchor="center")

reset_button = ttk.Button(root, text="Cancel Shutdown", command=cancel_shutdown, cursor="hand2")
reset_button.place(relx=1,rely=1, x=00, y=00, anchor=tk.SE)

root.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("My Graphics")
root.geometry("500x500")

frames = [tk.PhotoImage(file='animatie.gif', format=f'gif -index {i}') for i in range(13)]
label = tk.Label(root)
label.pack(expand=True)

def update(i=0):
    label.config(image=frames[i])
    root.after(100, update, (i+1) % len(frames))

update()
root.mainloop()
import wikipedia
import tkinter as tk

root = tk.Tk()
root.title("Wikipedia")
canvas = tk.Canvas(root, width = 800, height = 700,  relief = 'raised', bg='black')
canvas.pack()

label1 = tk.Label(root, text='Wikipedia', bg='black', fg="#00DEA1")
label1.config(font=('Comic Sans MS', 30))
canvas.create_window(400, 100, window=label1)

label2 = tk.Label(root, text='What are you looking for?', bg='black', fg="white")
label2.config(font=('Comic Sans MS', 15))
canvas.create_window(400, 155, window=label2)

entry1 = tk.Entry (root) 
canvas.create_window(400, 210, window=entry1, width=300)

label3 = tk.Label(root, bg='black', fg="white", wraplength=700)

def findOnWiki():

    def deleteText():
        label3.config(text="")
    deleteText()

    x1 = entry1.get()
    info = wikipedia.summary(x1, 3)

    label3.config(font=('Comic Sans MS', 13), textvariable=info, text=info)
    canvas.create_window(400, 450, window=label3)


button = tk.Button(text='Search', bg='#14A285',activebackground='#6EEECB',activeforeground='white', border=0, command = findOnWiki, fg='white', font=('Comic Sans MS', 15))
canvas.create_window(400, 280, window=button)

root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title("Layouts em Tkinter")
root.geometry("200x200")
# label1 = tk.Label(root, text="Label 1 - pack")
# label1.pack()

# label2 = tk.Label(root, text="AAAAAAAA")
# label2.grid(row=0, column=0)

# label3 = tk.Label(root, text="BBBBBBBBBB")
# label3.grid(row=0, column=1)

label4 = tk.Label(root, text="Label 4 - place")
label4.place(x=50, y=50)

root.mainloop()


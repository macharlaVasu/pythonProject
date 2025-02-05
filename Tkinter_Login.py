# import tkinter as tk 

# def greetings():
#     print("Welocme to new App")

# root =tk.Tk()
# # root.geometry("1000x500")
# # root.title("Krithik Macharla  Managment school")
# button =root.Button(root,text="Greet",command=greetings)
# button.pack()
# root.mainloop()

import tkinter as tk

def greet():
    print("Hello, welcome to the app!")

root = tk.Tk()
root.geometry("1000x500")
root.title("Krithik Macharla  Managment school")
button = tk.Button(root, text="Greet", command=greet)
button.pack()
root.mainloop()
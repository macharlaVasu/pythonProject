from  tkinter import *

root = Tk()
root.geometry("1460x750")  # Set window size
root.title("Studnet Portal")  # Set window title
 
name = Label(root, text = "Name").place(x = 40,y = 50)  
email = Label(root, text = "Email").place(x = 40, y = 90)  
password = Label(root, text = "Password").place(x = 30, y = 130) 
# submit = Button(root, text = "Submit").grid(row = 4, column = 0)  
e1 = Entry(root).place(x = 80, y = 50)  
e2 = Entry(root).place(x = 80, y = 90)  
e3 = Entry(root).place(x = 95, y = 130)  


root.mainloop()
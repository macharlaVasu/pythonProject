import tkinter as tk
from tkinter import messagebox
import snowflake.connector

# Snowflake connection parameters
config = {
        "user": "SRINI",          # Your Snowflake username
        "password": "Sreenivasulu@123",      # Your Snowflake password
        "account": "fspzgvp-io77649",        # Your Snowflake account identifier (e.g., xy12345)
        "warehouse": "COMPUTE_WH",    # Your Snowflake warehouse
        "database": "DEMO",      # Your Snowflake database
        "schema": "TEST"           # Your Snowflake schema
    }

def create_snowflake_connection():
    """
    Create and return a Snowflake connection.
    """
    try:
        conn = snowflake.connector.connect(**config)
        print("Connected to Snowflake successfully!")
        return conn
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to Snowflake: {str(e)}")
        return None

def register_student():
    """
    Register a new student by taking input from the GUI.
    """
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    if not name or not age or not email:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    # Insert the student data into Snowflake
    conn = create_snowflake_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Insert query
        query = """
        INSERT INTO students (name, age, email)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, age, email))
        conn.commit()
        messagebox.showinfo("Success", f"Student '{name}' registered successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to register student: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed.")

def view_students():
    """
    View all registered students from the Snowflake table.
    """
    conn = create_snowflake_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Select query
        query = "SELECT * FROM students"
        cursor.execute(query)

        # Fetch and display results
        students = cursor.fetchall()
        if not students:
            messagebox.showinfo("Info", "No students registered yet.")
        else:
            student_list = "\n".join([f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Email: {s[3]}" for s in students])
            messagebox.showinfo("Registered Students", student_list)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch students: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed.")

# Create the main window
root = tk.Tk()

root.title("Student Registration System")

# Set the initial window size (width x height)
root.geometry("500x300")  # Increase the window size to 500x300 pixels

# Make the window resizable (width, height)
root.resizable(True, True)  # Allow both horizontal and vertical resizing

# Set background color
root.configure(bg="#f0f0f0")

# Create and place widgets
label_name = tk.Label(root, text="Name:",bg="#f0f0f0", fg="#333333")
label_name.grid(row=0, column=0, padx=10, pady=10,)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age:",bg="#f0f0f0", fg="#333333")
label_age.grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:",bg="#f0f0f0", fg="#333333")
label_email.grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

button_register = tk.Button(root, text="Register", command=register_student)
button_register.grid(row=3, column=0, padx=10, pady=10)

button_view = tk.Button(root, text="View Students", command=view_students)
button_view.grid(row=3, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
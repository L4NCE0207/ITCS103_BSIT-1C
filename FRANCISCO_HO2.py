import tkinter as tk

window = tk.Tk()
window.title ("Lance Daniel Francisco's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="lightgreen")


StudentTitle = tk.Label(text="Student Profile", font=("Times New Roman",16,"bold"), padx=20, pady=20, bg="lightgreen")

Name = tk.Label(text="Name: Lance Daniel P. Francisco", font=("Times New Roman", 10), pady=10, padx=5, bg="lightgreen")

Age = tk.Label(text="Age: 19", font=("Times New Roman", 10), pady=10, padx=5, bg="lightgreen")

Address = tk.Label(text="Address: Brgy Ibabang dupay, Lucena, Quezon", font=("Times New Roman", 10), pady=10, padx=5, bg="lightgreen")

Course = tk.Label(text="Course: BSIT-1C", font=("Times New Roman", 10), pady=10, padx=5, bg="lightgreen")

Birthday = tk.Label(text="Birthday: February 2, 2007", font=("Times New Roman", 10), pady=10, padx=5, bg="lightgreen")

MottoLabel = tk.Label(text="Motto:", font=("Times New Roman", 10), pady=10, padx=5, bg="lightgreen")

Motto = tk.Label(text="\"Life is a one time offer, use it carefully.\"", font=("Times New Roman", 10,"italic"), pady=10, padx=5, bg="lightgreen")

StudentTitle.pack(fill="both")
Name.pack(anchor='nw')
Age.pack(anchor='nw')
Address.pack(anchor='nw')
Course.pack(anchor='nw')
Birthday.pack(anchor='nw')
MottoLabel.pack(anchor='nw')
Motto.pack(anchor='center')
 
window.mainloop()

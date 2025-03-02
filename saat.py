from tkinter import *  
import time  

# Create main window
clock_window = Tk()
clock_window.title("Digital Clock")  
clock_window.geometry("400x200") 
clock_window.config(bg="#0C1E28")  

# Clock labels
label_hour = Label(clock_window, text="00", font=("Arial", 40), fg="white", bg="#0C1E28")
label_hour.place(x=50, y=70)

label_minute = Label(clock_window, text="00", font=("Arial", 40), fg="white", bg="#0C1E28")
label_minute.place(x=150, y=70)

label_second = Label(clock_window, text="00", font=("Arial", 40), fg="white", bg="#0C1E28")
label_second.place(x=250, y=70)

# Function to update time
def update_clock():
    hour = str(time.strftime("%H"))  # Get hour (24-hour format)
    minute = str(time.strftime("%M"))  
    second = str(time.strftime("%S"))  

    label_hour.config(text=hour)
    label_minute.config(text=minute)
    label_second.config(text=second)
    
    clock_window.after(1000, update_clock)  # Update every second

update_clock()  
clock_window.mainloop()  

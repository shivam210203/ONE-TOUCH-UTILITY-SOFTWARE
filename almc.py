import datetime
import winsound
import tkinter as tk
from PIL import Image, ImageTk


alarms = {}



def set_alarm():
    alarm_time = entry_alarm_time.get()
    alarm_name = entry_alarm_name.get()
    alarms[alarm_name] = alarm_time
    update_alarm_listbox()

def delete_alarm():
    selected_alarm = listbox_alarms.get(listbox_alarms.curselection())
    alarms.pop(selected_alarm)
    update_alarm_listbox()

def reset_alarm():
    alarms.clear()
    update_alarm_listbox()

def update_alarm_listbox():
    listbox_alarms.delete(0, tk.END)
    for alarm_name, alarm_time in alarms.items():
        listbox_alarms.insert(tk.END, f"{alarm_name}: {alarm_time}")

def check_alarms():
    current_time = datetime.datetime.now().strftime("%H:%M")
    for alarm_name, alarm_time in alarms.items():
        if current_time == alarm_time:
            winsound.PlaySound("Alarm.wav", winsound.SND_ALIAS)
            #tk.messagebox.showinfo("Alarm", f"{alarm_name} alarm is going off!")
            alarms.pop(alarm_name)
            update_alarm_listbox()
    root.after(1000, check_alarms)

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("450x400")

img = Image.open("almcbck2.jpg")
img = img.resize((500, 500), Image.ANTIALIAS)
root.background_image = ImageTk.PhotoImage(img)
root.background_label = tk.Label(root.master, image=root.background_image)
root.background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_alarm_time = tk.Label(root, text="Alarm Time (HH:MM):", fg="cyan",bg="black", font=("Arial", 9,"italic"))
label_alarm_time.place(x=20,y=50)


entry_alarm_time = tk.Entry(root, fg="cyan",bg="black", font=("Arial", 9,"italic"))
entry_alarm_time.place(x=155,y=50)

label_alarm_name = tk.Label(root, text="Alarm Name:", fg="cyan",bg="black", font=("Arial", 9,"italic"))
label_alarm_name.place(x=20,y=100)

entry_alarm_name = tk.Entry(root, fg="cyan",bg="black", font=("Arial", 9,"italic"))
entry_alarm_name.place(x=110,y=100)

button_set_alarm = tk.Button(root, text="Set Alarm", command=set_alarm, fg="cyan",bg="black", font=("Arial", 9,"italic"))
button_set_alarm.place(x=20,y=150)

listbox_alarms = tk.Listbox(root,bd=5,relief='solid',justify="center",bg="black",selectbackground="cyan",selectforeground="cyan",fg="white")
listbox_alarms.place(x=80,y=200)

button_delete_alarm = tk.Button(root, text="Delete Alarm", command=delete_alarm, fg="cyan",bg="black", font=("Arial", 9,"italic"))
button_delete_alarm.place(x=90,y=150)

button_reset_alarm = tk.Button(root, text="Reset Alarms", command=reset_alarm, fg="cyan",bg="black", font=("Arial", 9,"italic"))
button_reset_alarm.place(x=175,y=150)



check_alarms()

root.mainloop()

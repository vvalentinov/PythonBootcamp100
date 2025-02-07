import tkinter as tk

root = tk.Tk()
root.title("Miles To Kilometers Converter")
root.geometry("800x500")
root.resizable(width=False, height=False)
root.config(background="black")

def on_entry(event):
    if event.keycode == 13:
        button_clicked()

miles_entry_text = tk.StringVar()
miles_entry_text.set("Enter Miles Here...")
miles_entry = tk.Entry()
miles_entry.bind("<Return>", on_entry)
miles_entry.config(font=("Consolas", 20), textvariable=miles_entry_text)
miles_entry.pack(pady=(100, 0))

def button_clicked():
    miles_input = miles_entry.get()
    try:
        miles = float(miles_input)
        miles_entry["fg"] = "black"
        kilometers = round(miles * 1.60934, 4)
        km_entry.delete(0, "end")
        km_entry.insert(0, f"{kilometers} km")
    except ValueError:
        miles_entry.delete(0, "end")
        miles_entry["fg"] = "red"
        miles_entry.insert(0, "Invalid Input!")

converter_btn = tk.Button()
converter_btn.config(
    text="Convert To Kilometers",
    command=button_clicked,
    background="#42ff33",
    activebackground="#42ff33",
    highlightthickness=2,
    highlightcolor="red",
    border=0,
    font=("Consolas", 20),
    padx=30,
    cursor="hand2"
)
converter_btn.pack(pady=50)

km_entry = tk.Entry()
km_entry.config(font=("Consolas", 20))
km_entry.pack()

root.mainloop()

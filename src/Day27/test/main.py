import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=500)

my_label = tkinter.Label(text="I am a label", font=("Consolas", 20))
my_label.pack()

# my_label["text"]= "Updated Text"
# my_label.config(text="New Updated Text")

def button_clicked():
    # my_label["text"] = "Button was clicked!"
    my_label["text"] = example_input.get()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

example_input = tkinter.Entry(width=100)
example_input.pack()


window.mainloop()
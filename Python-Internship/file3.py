import tkinter

def say_hello():
    print("Hey There")
    label2 = tkinter.Label(text="Hey i am a label")
    label2.pack(side="top")
    label1["text"] = "Hello"

window = tkinter.Tk()
window.title("Gui App")
window.minsize(500,500)

label1 = tkinter.Label(text="Hey i am a label")
label1.pack(side="left")
button = tkinter.Button(text="Click ME", command=say_hello)
button.pack(side="bottom")
#button["text"] = "Hello"
window.mainloop()
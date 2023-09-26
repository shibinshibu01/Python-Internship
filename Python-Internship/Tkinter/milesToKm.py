import tkinter as tk

def milesToKm():
    mile=float(input.get())
    km=round(mile*1.609,2)
    output["text"] = f"{mile} mile is {km} km!"
    
    
screen=tk.Tk()
screen.title("Miles to KM")
screen.minsize(500,300)

miles=tk.Label(text="Enter Miles: ")
input=tk.Entry()
miles.pack()
input.pack()
button=tk.Button(text="Convert",command=milesToKm)
button.pack()
output=tk.Label(text="")
output.pack()

screen.mainloop()
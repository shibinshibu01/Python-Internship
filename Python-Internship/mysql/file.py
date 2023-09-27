import mysql.connector as myco
import tkinter as tk

def calculatePer(results):
    x=results[4]
    y=results[5]
    z=results[6]
    percent=((x+y+z)/300)*100
    output.config(text=f"The percentage mark of {results[1]} is {percent:.2f}%")

screen = tk.Tk()
screen.title("Student Database")

mydb = myco.connect(
  host="localhost",
  user="root",
  password="",
  database="demodb"
)

m= mydb.cursor()

#m.execute("insert into user values('st1','Shibin','2001-12-08',7736058923,95,99,100);")
#mydb.commit()
m.execute("select * from user;")
#m.execute("desc user;")
results = m.fetchone()
print(results)
name=tk.Label(text="Student Database")
name.grid(row=0, column=0, padx=10, pady=5, columnspan=7)

labels = [
    ("Userid", 1, 0),
    ("Username", 1, 1),
    ("DOB", 1, 2),
    ("Phone", 1, 3),
    ("Mark1", 1, 4),
    ("Mark2", 1, 5),
    ("Mark3", 1, 6),
]

for label_text, row, column in labels:
    label = tk.Label(text=label_text)
    label.grid(row=row, column=column, padx=10, pady=5, sticky="w")
    
labels1 = [
    (results[0], 2, 0),
    (results[1], 2, 1),
    (results[2], 2, 2),
    (results[3], 2, 3),
    (results[4], 2, 4),
    (results[5], 2, 5),
    (results[6], 2, 6),
]

for label_text, row, column in labels1:
    label1 = tk.Label(text=label_text)
    label1.grid(row=row, column=column, padx=10, pady=5, sticky="w")    
calculate = tk.Button(text='Calculate',command=lambda: calculatePer(results))
calculate.grid(row=3, column=0,columnspan=7, padx=10, pady=5)

output=tk.Label(text="")
output.grid(row=4, column=0, padx=10, pady=5, columnspan=7)

screen.mainloop()
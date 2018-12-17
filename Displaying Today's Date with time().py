from tkinter import *
from time import *
from datetime import *


myInterface = Tk()
s = Canvas(myInterface, width=1200, height=1000, background="black")
s.pack()
BGIMG = PhotoImage(file = "wood.gif")
BG = s.create_image(600, 425, image = BGIMG)




######################  user inputs

Proceed = True
List = []
while Proceed == True:
    file = open("text.txt", "w")
    print("Would you like to add anything?")
    print("Current list:")
    for i in range(len(List)):
        print(List[i])
    print("['EXIT'] to exit this page")
    newItem = input("New item: ")
    if newItem in ["exit", "Exit", "EXIT"]:
        file.write(str(List))
        file.close()
        Proceed = False
    else:
        List.append(newItem)
        file.write(str(List))
        file.close()
        print()


file = open("text.txt","r")
itemsInTextList = file.read()
print(itemsInTextList)

#######################  to do list
s.create_text(850, 200, text="To do:", font="Helvetica 50", fill="white")
y = 320
for i in range(len(List)):
    s.create_text(850, y, text=List[i], font="Helvetica 30", fill="white")
    y+=50


#######################  year, month, day
today = date.today()
s.create_text(400, 148, text=(today), font="Helvetica 40", fill="white")

#######################  hours, minutes, seconds
while True:
    now = datetime.now()
    t = now.strftime("%I:%M:%S") 

    time = s.create_text(420, 250, text=(t), font="Helvetica 70", fill="white")
    s.update()
    sleep(1)
    s.delete(time)

s.update()


































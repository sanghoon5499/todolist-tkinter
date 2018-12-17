from tkinter import *
from time import *
from datetime import *
from time import  *

myInterface = Tk()
s = Canvas(myInterface, width=1200, height=1000, background="black")
s.pack()
BGIMG = PhotoImage(file = "wood.gif")
BG = s.create_image(600, 425, image = BGIMG)

def convertStringToList(s):
    return s.split("\n")  #save the shit as variable using this function
def convertListToString(l):
    return "\n".join(l)

######################  user inputs

print("Add anything to list?")
ans = input("[yes]/[no]")
if ans in ["y", "Y", "yes", "YES"]:
    with open("text.txt", "w") as file:
        Proceed = True
        List = []
        while Proceed == True:
            print("Would you like to add anything?")
            print("Current list:")
            for i in range(len(List)):
                print(List[i])
            print("['EXIT'] to exit this page")
            newItem = input("New item: ")
            if newItem in ["exit", "Exit", "EXIT"]:
                Proceed = False
            else:
                List.append(newItem)
                print()
        file.write(convertListToString(List))
else:
    with open("text.txt", "r") as readfile:
        List = readfile.read()
        print("Items in list:", List)
        sleep(1)


##file.write(str(List))
##file.close()
##file = open("text.txt","r")
##itemsInTextList = file.read()
##print(itemsInTextList)

#######################  to do list
s.create_text(850, 200, text="To do:", font="Helvetica 50", fill="white")
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


































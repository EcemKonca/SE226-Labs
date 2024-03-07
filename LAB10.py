from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("LAB10")


def read():
    file = open("C:\\Users\\ECEM\\Downloads\\Marvel.txt")
    readFile = file.read()
    myTextBox.delete(1.0, END)
    myTextBox.insert(END, readFile)
    file.close()


def calculate():
    myTextBox.delete(1.0, END)
    file = open("C:\\Users\\ECEM\\Downloads\\Marvel.txt", "r")
    x = file.read().split()
    frequentslist = []
    for i in x:
        if i not in frequentslist:
            frequentslist.append(i)
    for i in range(0, len(frequentslist)):
        text = 'Frequency of {} is: {}\n'.format(frequentslist[i], x.count(frequentslist[i]))
        myTextBox.insert(END, text)


myTextBox = Text(root, width=70, height=30)
myTextBox.pack()

readButton = Button(master=root, text="READ", width=60, command=read)
readButton.pack()

calculateButton = Button(master=root, text="CALCULATE", width=60, command=calculate)
calculateButton.pack()

root.mainloop()

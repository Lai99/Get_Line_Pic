from Tkinter import *


def main():
    root = Tk()
    inputText = Label(root, text="URL:", bd=3)
    inputText.pack(side=LEFT)
    url = StringVar()
    inputField = Entry(root, bd=4, width=50, textvariable=url)
    inputField.pack(side=LEFT)
    execBtn = Button(root, text="GET", bd=3)
    execBtn.pack(side=LEFT, expand=1)

    mainloop()

if __name__ == '__main__':
    main()



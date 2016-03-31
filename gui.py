from Tkinter import *
from get_png import get_pic, download_file

class GUI():
    def __init__(self, root):
        inputText = Label(root, text="URL:", bd=3)
        inputText.pack(side=LEFT)
        self.url = StringVar()
        self.inputField = Entry(root, bd=4, width=50, textvariable=self.url)
        self.inputField.pack(side=LEFT)
        self.statusText = Label(root, width=8, bd=3)
        self.statusText.pack(side=LEFT)
        self.execBtn = Button(root, text="GET", bd=3, command=self.btn_active)
        self.execBtn.pack(side=LEFT, padx=4)

    def btn_active(self):
        url = self.url.get()
        self.statusText['text'] = "Running"
        if self.check_url(url):
            get_pic(url)
        self.statusText['text'] = "Done"

    def check_url(self, url):
        if len(url) > 4:
            return True
        else:
            return False
def main():
    root = Tk()
    gui = GUI(root)
    mainloop()

if __name__ == '__main__':
    main()



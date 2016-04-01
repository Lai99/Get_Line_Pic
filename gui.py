from Tkinter import *
from get_png import get_pic, download_file
import Queue
from threading import Thread
import re

class GUI:
    def __init__(self, root):
        """
                Initial the gui components and make a queue for  catching the picture download complete message
                """
        self.root = root
        self.inputText = Label(root, text="URL:", bd=3)
        self.inputText.pack(side=LEFT)
        self.url = StringVar()
        self.inputField = Entry(root, bd=4, width=50, textvariable=self.url)
        self.inputField.pack(side=LEFT)
        self.inputField.focus()
        self.var = IntVar()
        self.checkBtn = Checkbutton(root, variable=self.var)
        self.checkBtn.pack(side=LEFT)
        self.statusText = Label(root, width=8, bd=3)
        self.statusText.pack(side=LEFT)
        self.execBtn = Button(root, text="GET", bd=3, command=self.btn_active)
        self.execBtn.pack(side=LEFT, padx=4)
        # Make the queue for catching the picture download complete message
        self.queue = Queue.Queue()

    def btn_active(self):
        """
                Button event -> When the button pressed, the button disable and start a thread to execute download task.
                                         Then call  "process_queue" to listen the task is done or not.
                """
        if not self.check_url():
            # If return None means illegal URL
            self.url.set("Invalid URL")
            return None

        self.execBtn.config(state=DISABLED)
        self.statusText['text'] = "Running"
        ThreadTask(self.queue, self.url.get(), self.var.get()).start()
        self.root.after(100, self.process_queue)

    def process_queue(self):
        """
                process_queue will continue to get task from queue to check the download finish message. If the task
                 is got, the gui will reset.
                """
        try:
            # No task in queue will raise Queue.Empty
            msg = self.queue.get(0)
            print msg
            self.statusText['text'] = msg
            self.url.set("")
            self.execBtn.config(state=NORMAL)
        except Queue.Empty:
            self.root.after(100, self.process_queue)

    def check_url(self):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return regex.match(self.url.get())


class ThreadTask(Thread):
    def __init__(self, queue, url, check):
        Thread.__init__(self)
        self.queue = queue
        self.url = url
        self.check = check

    def run(self):
        try:
            get_pic(self.url, self.check)
            self.queue.put("Finish")
        except:
            self.queue.put("Fail")


def main():
    root = Tk()
    GUI(root)
    mainloop()

if __name__ == '__main__':
    main()



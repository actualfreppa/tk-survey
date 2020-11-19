

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:
    def __init__(self, master):

        master.title("Feedback Form")
        master.resizable(False, False)
        master.configure(background="#e1d8b9")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#e1d8b9")
        #self.style.configure("TButton", background="#e1d8b9")
        self.style.configure("TLabel", background="#e1d8b9", font=("Ariel", 11))
        self.style.configure("Header.TLabel", font=("Ariel", 18, "bold"))
        self.style.configure("TEntry", font=("Ariel", 11))
        
        self.frame_header = ttk.Frame(master)
        self.logo = PhotoImage(file="tour_logo.gif")
        self.label_logo = ttk.Label(self.frame_header, image=self.logo)
        self.label_thanks = ttk.Label(self.frame_header, text="Thanks for participating in the survey", style="Header.TLabel")
        self.label_message = ttk.Label(self.frame_header, wraplength=300, text = ("We're glad that you participated in the recent adventure. "
                                                                   "Please tell us what you thought about hte trip"))
        self.frame_content = ttk.Frame(master)
        self.label_name = ttk.Label(self.frame_content, text="Name:")
        self.label_email = ttk.Label(self.frame_content, text="Email:")
        self.label_comments = ttk.Label(self.frame_content, text="Comments:")

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)
        self.text_comments = Text(self.frame_content, width=50, height=10, wrap=WORD, font=("Ariel", 11))

        self.button_submit = ttk.Button(self.frame_content, text="Submit", command=self.submit)
        self.button_clear = ttk.Button(self.frame_content, text="Clear", command=self.clear)

        self.frame_header.pack()
        self.frame_content.pack()

        self.label_logo.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        self.label_thanks.grid(row=0, column=1, padx=5)
        self.label_message.grid(row=1, column=1, padx=5)

        self.label_name.grid(row=0, column=0, padx=5, sticky="sw")
        self.label_email.grid(row=0, column=1, padx=5, sticky="sw")
        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.label_comments.grid(row=2, column=0, padx=5, sticky="sw")
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)
        self.button_submit.grid(row=4, column=0, padx=5, sticky="e")
        self.button_clear.grid(row=4, column=1, padx=5, sticky="w")

    def submit(self):
        name=self.entry_email.get()
        email=self.entry_email.get()
        comments=self.text_comments.get(1.0, END)
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Comments: {comments}")
        self.clear()
        messagebox.showinfo(title="Comment Submitted", message="Comment submitted")


    def clear(self):
        self.entry_name.delete(0, END)
        self.entry_email.delete(0, END)
        self.text_comments.delete(1.0, END)


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":
    main()




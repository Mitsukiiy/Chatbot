from tkinter import *
from PIL import ImageTk, Image
from chat import get_response, bot_name

BG_GRAY = "#a3a3a3"
BG_COLOR = "#1a1a1a"
TEXT_COLOUR = "#EAECEE"
FONT = "BradleyHandITCRegular"
FONT_BOLD = "BradleyHandITCRegular"


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1450, height=790, bg=BG_COLOR)

        # Load and resize the icon image
        icon_image = Image.open("3.png")  # Replace "icon.png" with the path to your icon image
        icon_image = icon_image.resize((95, 50), Image.ANTIALIAS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        # head label with icon
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOUR, font=FONT_BOLD, pady=10)
        head_label.config(text="Welcome to Aura", compound=LEFT, image=icon_photo)
        head_label.image = icon_photo
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=300, bg=BG_GRAY)
        line.place(relwidth=5, rely=0.10, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOUR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=45)
        bottom_label.place(relwidth=1, rely=0.91)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#1a1a1a", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.09, rely=0.005, relx=0.005)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, bg="#e15b5b",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.78, rely=0.0018, relheight=0.09, relwidth=0.22)


    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
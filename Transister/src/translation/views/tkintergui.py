import tkinter as tk
from PIL import ImageTk

class  Application(tk.Frame):
    """tkinterGUI作成"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry()
        self.master.title('English Translation')

        self.entry = tk.Entry(self.master)
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.create_widgets()

    def create_widgets(self):
        file_menu = tk.Menu(self.menu_bar)
        file_menu.add_command(label='Exit', command=self.master.quit)
        self.menu_bar.add_cascade(label='File', menu=file_menu)

        test_button = tk.Button(self.master, text = "Open", command=self.create_picture_window)
        test_button.pack()

    def create_picture_window(self, img):
        photo = ImageTk.PhotoImage(img)

        new_window = tk.Toplevel(self.master)
        window_label = tk.Label(new_window, text="Taken Photo")
        window_img = tk.Label(new_window, image=photo)
        window_button = tk.Button(new_window, text = "Exit", command=new_window.destroy)

        window_label.pack()
        window_img.pack()
        window_button.pack()

    # def add_button(self):
    #     pic_label = tk.Label(new_window, text="Taken Photo")
    #     pic_button = tk.Button(self.master, text=)

    def widgets_update(self, txt):
        message = tk.Message(self.master, txt)

def start_tkinter():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
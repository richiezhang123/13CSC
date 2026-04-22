from tkinter import *
from PIL import Image, ImageTk

class MenuPage:
    def __init__(self,parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Menu.png")
        self.background_image =self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill=BOTH, expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk, borderwidth=0)  # Creates a label, which holds the background image
        self.image_label.place(relwidth=1, relheight=1)  # Ensures that the label/image fits the entire screen

        # self.text_label = Label(self.studi_frame, text = "Hi", font=["Tw Cen Mt", "26", "bold"])
        # self.text_label.place(relx=0.5, rely=0.78, anchor="center")

        self.timer_image = Image.open("Timer.png")
        self.timer_image_tk = ImageTk.PhotoImage(self.timer_image)

        self.tasks_image = Image.open("Tasks.png")
        self.tasks_image_tk = ImageTk.PhotoImage(self.tasks_image)

        self.timer_button = Button(self.studi_frame, image = self.timer_image_tk, command = clicked, cursor = "hand2")
        self.timer_button.place(relx = 0.27, rely= 0.44)

        self.tasks_button = Button(self.studi_frame, image = self.tasks_image_tk, command = clicked, cursor = "hand2")
        self.tasks_button.place(relx = 0.53, rely= 0.44)

def clicked():
    print("Hi")



#Runs the program
if __name__ == "__main__": #Ensures the code only runs when the program is executed
    root = Tk() #Creates the root Tkinter window
    root.title("Studi") #Sets the title of the window to "Studi"
    root.attributes("-fullscreen", True) #Makes the window fullscreen
    studi_instance = MenuPage(root) #Creates an instance of the MenuPage class
    root.mainloop() #Starts the window loop until the user closes it
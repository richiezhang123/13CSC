from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
class MenuPage:
    def __init__(self,parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Menu.png")
        self.background_image =self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill="both", expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk)  # Creates a label, which holds the background image
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ensures that the label/image fits the entire screen

        self.timer_image =PhotoImage("Timer Button.png")

        self.timer_button = Button(self.studi_frame, text = "", image=self.timer_image)
        self.timer_button.place(relx=0.5, rely = 0.6, anchor="center")
#Runs the program
if __name__ == "__main__": #Ensures the code only runs when the program is executed
    root = Tk() #Creates the root Tkinter window
    root.title("Studi") #Sets the title of the window to "Studi"
    root.attributes("-fullscreen", True) #Makes the window fullscreen
    studi_instance = MenuPage(root) #Creates an instance of the MenuPage class
    root.mainloop() #Starts the window loop until the user closes it
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
import pywinstyles

class MenuPage:
    def __init__(self,parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Menu.png")
        self.background_image =self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk =ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill=BOTH, expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk, borderwidth=0)  # Creates a label, which holds the background image
        self.image_label.place(relwidth=1, relheight=1)  # Ensures that the label/image fits the entire screen

        self.timer_image = Image.open("Timer.png")
        self.timer_image_tk = ImageTk.PhotoImage(self.timer_image)

        self.tasks_image = Image.open("Tasks.png")
        self.tasks_image_tk = ImageTk.PhotoImage(self.tasks_image)

        self.user_image = Image.open("User.png")
        self.user_image_tk = ImageTk.PhotoImage(self.user_image)

        self.settings_image = Image.open("Settings.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)

        self.exit_image = Image.open("Exit.png")
        self.exit_image_Tk = ImageTk.PhotoImage(self.exit_image)

        self.timer_button = Button(self.studi_frame, image = self.timer_image_tk, bg="#a60c09", activebackground="#a60c09", command = self.clicked, cursor = "hand2",  borderwidth=0, )
        self.timer_button.place(relx = 0.27, rely= 0.44)
        pywinstyles.set_opacity(self.timer_button, color="#a60c09")

        self.tasks_button = Button(self.studi_frame, image = self.tasks_image_tk, command = self.clicked, cursor = "hand2", bg="#a60c09", borderwidth=0, activebackground="#a60c09")
        self.tasks_button.place(relx = 0.53, rely= 0.44)
        pywinstyles.set_opacity(self.timer_button, color="#a60c09")

        # self.timer_button = Button(self.studi_frame, image=self.timer_image_tk, command=self.clicked, cursor="hand2")
        # self.timer_button.place(relx=0.27, rely=0.44)
        #
        # self.tasks_button = Button(self.studi_frame, image=self.tasks_image_tk, command=self.clicked, cursor="hand2")
        # self.tasks_button.place(relx=0.53, rely=0.44)

        self.user_button = Button(self.studi_frame, image = self.user_image_tk, command = self.clicked, cursor = "hand2", bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.user_button.place(relx = 0.85, rely= 0.022)

        self.settings_button = Button(self.studi_frame, image = self.settings_image_tk, command = self.clicked, cursor = "hand2", bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.settings_button.place(relx = 0.9, rely= 0.022)

        self.exit_button = Button(self.studi_frame, image = self.exit_image_Tk, command = self.exit_program, cursor = "hand2", bg="#8d0401",  borderwidth=0,   activebackground="#8d0401")
        self.exit_button.place(relx = 0.95, rely= 0.022)

        self.timer_button.bind("<Enter>", self.timer_on_enter)
        self.timer_button.bind("<Leave>", self.timer_on_leave)

        self.tasks_button.bind("<Enter>", self.tasks_on_enter)
        self.tasks_button.bind("<Leave>", self.tasks_on_leave)

        self.tasks_button.bind("<Enter>", self.tasks_on_enter)
        self.tasks_button.bind("<Leave>", self.tasks_on_leave)

        self.user_button.bind("<Enter>", self.user_on_enter)
        self.user_button.bind("<Leave>", self.user_on_leave)

        self.settings_button.bind("<Enter>", self.settings_on_enter)
        self.settings_button.bind("<Leave>", self.settings_on_leave)

        self.exit_button.bind("<Enter>", self.exit_on_enter)
        self.exit_button.bind("<Leave>", self.exit_on_leave)

    def clicked(self):
        print("button clicked")

    def exit_program(self):
        self.studi_frame.destroy()
        exit()

    def timer_on_enter(self, event):
        self.timer_image = Image.open("Timer_Hover.png")
        self.timer_image_tk = ImageTk.PhotoImage(self.timer_image)
        self.timer_button.config(image=self.timer_image_tk)
    def timer_on_leave(self,event):
        self.timer_image = Image.open("Timer.png")
        self.timer_image_tk = ImageTk.PhotoImage(self.timer_image)
        self.timer_button.config(image=self.timer_image_tk)

    def tasks_on_enter(self, event):
        self.tasks_image = Image.open("Tasks_Hover.png")
        self.tasks_image_tk = ImageTk.PhotoImage(self.tasks_image)
        self.tasks_button.config(image=self.tasks_image_tk)
    def tasks_on_leave(self,event):
        self.tasks_image = Image.open("Tasks.png")
        self.tasks_image_tk = ImageTk.PhotoImage(self.tasks_image)
        self.tasks_button.config(image=self.tasks_image_tk)

    def user_on_enter(self, event):
        self.user_image = Image.open("User_Hover.png")
        self.user_image_tk = ImageTk.PhotoImage(self.user_image)
        self.user_button.config(image=self.user_image_tk)
    def user_on_leave(self, event):
        self.user_image = Image.open("User.png")
        self.user_image_tk = ImageTk.PhotoImage(self.user_image)
        self.user_button.config(image=self.user_image_tk)

    def settings_on_enter(self, event):
        self.settings_image = Image.open("Settings_Hover.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)
        self.settings_button.config(image=self.settings_image_tk)
    def settings_on_leave(self, event):
        self.settings_image = Image.open("Settings.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)
        self.settings_button.config(image=self.settings_image_tk)

    def exit_on_enter(self, event):
        self.exit_image = Image.open("Exit_Hover.png")
        self.exit_image_tk = ImageTk.PhotoImage(self.exit_image)
        self.exit_button.config(image=self.exit_image_tk)
    def exit_on_leave(self, event):
        self.exit_image = Image.open("Exit.png")
        self.exit_image_tk = ImageTk.PhotoImage(self.exit_image)
        self.exit_button.config(image=self.exit_image_tk)

#Runs the program
if __name__ == "__main__": #Ensures the code only runs when the program is executed
    root = Tk()
    root.title("Studi") #Sets the title of the window to "Studi"
    root.attributes("-fullscreen", True) #Makes the window fullscreen
    studi_instance = MenuPage(root)  # Creates an instance of the MenuPage class
    root.mainloop() #Starts the window loop until the user closes it
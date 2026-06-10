from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import customtkinter
import pywinstyles
# import pygame
import pyglet
import time

# pygame.mixer.init()
# click_sound = pygame.mixer.Sound("mouse_click.mp3")


pyglet.options['win32_gdi_font'] = True

pyglet.font.add_file("Gaco_Strong_Font_Demo.otf")
pyglet.font.add_file("Nexa.ttf")
pyglet.font.add_file("AltoneTrial-Bold.ttf")
pyglet.font.add_file("Mont Heavy.otf")
pyglet.font.add_file("Etna.otf")


# tasks_font = Font(family="Mont Heavy DEMO", size = 35)

class MenuPage:
    def __init__(self, parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Menu.png")
        self.background_image = self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill=BOTH, expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk,
                                 borderwidth=0)  # Creates a label, which holds the background image
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

        self.timer_button = Button(self.studi_frame, image=self.timer_image_tk, command=self.openTimer, bg="#a60c09",
                                   activebackground="#a60c09", cursor="hand2", borderwidth=0, )
        self.timer_button.place(relx=0.27, rely=0.44)
        pywinstyles.set_opacity(self.timer_button, color="#a60c09")

        self.tasks_button = Button(self.studi_frame, image=self.tasks_image_tk, command=self.openTasks, cursor="hand2",
                                   bg="#a60c09", borderwidth=0, activebackground="#a60c09")
        self.tasks_button.place(relx=0.53, rely=0.44)
        pywinstyles.set_opacity(self.tasks_button, color="#a60c09")

        self.user_button = Button(self.studi_frame, image=self.user_image_tk, command=self.clicked, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.user_button.place(relx=0.85, rely=0.022)

        self.settings_button = Button(self.studi_frame, image=self.settings_image_tk, command=self.clicked,
                                      cursor="hand2", bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.settings_button.place(relx=0.9, rely=0.022)

        self.exit_button = Button(self.studi_frame, image=self.exit_image_Tk, command=self.exit_program, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.exit_button.place(relx=0.95, rely=0.027)

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
        pass

    def exit_program(self):
        self.studi_frame.destroy()
        exit()

    def timer_on_enter(self, event):
        self.timer_image = Image.open("Timer_Hover.png")
        self.timer_image_tk = ImageTk.PhotoImage(self.timer_image)
        self.timer_button.config(image=self.timer_image_tk)

    def timer_on_leave(self, event):
        self.timer_image = Image.open("Timer.png")
        self.timer_image_tk = ImageTk.PhotoImage(self.timer_image)
        self.timer_button.config(image=self.timer_image_tk)

    def tasks_on_enter(self, event):
        self.tasks_image = Image.open("Tasks_Hover.png")
        self.tasks_image_tk = ImageTk.PhotoImage(self.tasks_image)
        self.tasks_button.config(image=self.tasks_image_tk)

    def tasks_on_leave(self, event):
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

    def openTimer(self):
        # click_sound.play()
        self.studi_frame.destroy()
        TimerPage(root)

    def openTasks(self):
        # click_sound.play()
        self.studi_frame.destroy()
        TasksPage(root)


class TimerPage:
    def __init__(self, parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Timer_Page.png")
        self.background_image = self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill=BOTH, expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk,
                                 borderwidth=0)  # Creates a label, which holds the background image
        self.image_label.place(relwidth=1, relheight=1)  # Ensures that the label/image fits the entire screen

        self.user_image = Image.open("User.png")
        self.user_image_tk = ImageTk.PhotoImage(self.user_image)

        self.settings_image = Image.open("Settings.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)

        self.tasks_image = Image.open("Tasks.png")
        self.small_tasks_image = self.tasks_image.resize((240, 108))
        self.tasks_image_tk = ImageTk.PhotoImage(self.small_tasks_image)

        self.exit_image = Image.open("Exit.png")
        self.exit_image_Tk = ImageTk.PhotoImage(self.exit_image)

        self.user_button = Button(self.studi_frame, image=self.user_image_tk, command=self.clicked, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.user_button.place(relx=0.85, rely=0.022)
        self.user_button.bind("<Enter>", self.user_on_enter)
        self.user_button.bind("<Leave>", self.user_on_leave)

        self.settings_button = Button(self.studi_frame, image=self.settings_image_tk, command=self.clicked,
                                      cursor="hand2", bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.settings_button.place(relx=0.9, rely=0.022)
        self.settings_button.bind("<Enter>", self.settings_on_enter)
        self.settings_button.bind("<Leave>", self.settings_on_leave)

        self.exit_button = Button(self.studi_frame, image=self.exit_image_Tk, command=self.exit_program, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.exit_button.place(relx=0.95, rely=0.027)
        self.exit_button.bind("<Enter>", self.exit_on_enter)
        self.exit_button.bind("<Leave>", self.exit_on_leave)

        self.timer_button2 = customtkinter.CTkButton(
            self.studi_frame,
            text="TIMER",
            font=('Gaco Strong Demo', 50),
            width=250,
            height=60,
            text_color="white",
            fg_color="#9d0905",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#8c0603")
        self.timer_button2.place(relx=0.21, rely=0.28)

        self.short_break_button = customtkinter.CTkButton(
            self.studi_frame,
            text="SHORT BREAK",
            font=('Gaco Strong Demo', 50),
            width=550,
            height=60,
            text_color="white",
            fg_color="#9d0905",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#8c0603",
            command=self.start_short)
        self.short_break_button.place(relx=0.34, rely=0.28)

        self.long_break_button = customtkinter.CTkButton(
            self.studi_frame,
            text="LONG BREAK",
            font=('Gaco Strong Demo', 50),
            width=450,
            height=60,
            text_color="white",
            fg_color="#9d0905",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#8c0603",
            command=self.start_long)
        self.long_break_button.place(relx=0.61, rely=0.28)

        self.play_button = customtkinter.CTkButton(
            self.studi_frame,
            text="▶",
            font=('Gaco Strong Demo', 115),
            width=30,
            height=30,
            text_color="white",
            fg_color="#870c09",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#7D0502",
            command=self.start_timer)
        self.play_button.place(relx=0.4, rely=0.6327)

        self.pause_button = customtkinter.CTkButton(
            self.studi_frame,
            text="||",
            font=('Gaco Strong Demo', 100),
            width=100,
            height=40,
            text_color="white",
            fg_color="#870c09",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#7D0502",
            command=self.pause_timer
        )
        self.pause_button.place(relx=0.54, rely=0.645)

        self.minute_entry = customtkinter.CTkEntry(
            self.studi_frame,
            font=('Mont Heavy DEMO', 25),
            placeholder_text="Enter Time in Minutes",
            width=480,
            height=50,
            corner_radius=0)
        self.minute_entry.place(anchor="center", relx=0.475, rely=0.9)

        self.enter_button = customtkinter.CTkButton(
            self.studi_frame,
            text="Enter",
            font=('Mont Heavy DEMO', 30),
            width=100,
            height=70,
            text_color="white",
            fg_color="#870c09",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#7D0502",
            command=self.reset_timer
        )
        self.enter_button.place(relx=0.605, rely=0.87)

        self.timer_label = Label(self.studi_frame, text="00:00:00", font=('Gaco Strong Demo', 125), fg="white",
                                 bg="#a50c08")
        self.timer_label.place(anchor="center", relx=0.5, rely=0.5)
        pywinstyles.set_opacity(self.timer_label, color="#a50c08")

        self.timer_status = customtkinter.CTkLabel(self.studi_frame, text="", font=('Mont Heavy DEMO', 50),
                                                   text_color="white", fg_color="#a60c09")
        self.timer_status.place(anchor="center", relx=0.5, rely=0.585)
        pywinstyles.set_opacity(self.timer_status, color="#a60c09")

        self.reset_button = customtkinter.CTkButton(
            self.studi_frame,
            text="↻",
            font=('Gaco Strong Demo', 50),
            text_color="white",
            fg_color="#a30b08",
            border_width=0,
            border_spacing=10,
            corner_radius=0,
            border_color="#9d0905",
            hover_color="#8c0603",
            command=self.reset_timer)
        self.reset_button.place(relx=0.78, rely=0.38)

        self.tasks_button = Button(self.studi_frame, image=self.tasks_image_tk, command=self.openTasks, cursor="hand2",
                                   bg="#a60c09", borderwidth=0, activebackground="#a60c09")
        self.tasks_button.place(relx=0.85, rely=0.86)
        pywinstyles.set_opacity(self.tasks_button, color="#a60c09")

        self.tasks_button.bind("<Enter>", self.tasks_on_enter)
        self.tasks_button.bind("<Leave>", self.tasks_on_leave)

        self.is_timer_running = False
        self.is_paused = False
        self.end_time = 0
        self.time_remaining = 0

    def start_timer(self):
        if not self.is_timer_running:
            if self.is_paused:
                self.is_timer_running = True
                self.update_timer()
                self.timer_status.configure(text="Timer Running")
            else:
                self.time_remaining = int(self.minute_entry.get()) * 60
                self.is_timer_running = True
                self.timer_status.configure(text="Timer Running")
                self.update_timer()

    def start_short(self):
        self.time_remaining = int(5) * 60
        self.is_timer_running = True
        self.timer_status.configure(text="Timer Running")
        self.update_timer()

    def start_long(self):
        self.time_remaining = int(10) * 60
        self.is_timer_running = True
        self.timer_status.configure(text="Timer Running")
        self.update_timer()

    def pause_timer(self):
        self.is_timer_running = False
        self.is_paused = True
        self.timer_status.configure(text="Timer Paused")

    def reset_timer(self):
        if any(char in "!@#$%^&*()-_=+`~[]{}|;:'\",<.>?/\\" for char in self.minute_entry.get()):
            self.timer_status.configure(text="Cannot have special characters, try again!")
        elif self.minute_entry.get().strip() == "":
            self.timer_status.configure(text="Please enter a number, try again!")
        elif any(char in "abcdefghijklmnopqrstuvwxyz" for char in self.minute_entry.get()):
            self.timer_status.configure(text="Cannot have letters, try again!")
        else:
            self.is_timer_running = False
            self.time_remaining = int(self.minute_entry.get()) * 60
            minutes, seconds = divmod(self.time_remaining, 60)
            time_formatted = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_formatted)
            self.timer_status.configure(text="")

    def update_timer(self):
        if self.time_remaining > 0 and self.is_timer_running:
            minutes, seconds = divmod(self.time_remaining, 60)
            time_formatted = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_formatted)
            self.time_remaining -= 1
            self.studi_frame.after(1000, self.update_timer)
            print("HI!!")
        elif self.is_timer_running:
            self.timer_label.config(text="00:00")
            self.timer_status.configure(text="Timer Finished!")

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

    def tasks_on_enter(self, event):
        self.tasks_image = Image.open("Tasks_Hover.png")
        self.small_tasks_image = self.tasks_image.resize((240, 108))
        self.tasks_image_tk = ImageTk.PhotoImage(self.small_tasks_image)
        self.tasks_button.config(image=self.tasks_image_tk)

    def tasks_on_leave(self, event):
        self.tasks_image = Image.open("Tasks.png")
        self.small_tasks_image = self.tasks_image.resize((240, 108))
        self.tasks_image_tk = ImageTk.PhotoImage(self.small_tasks_image)
        self.tasks_button.config(image=self.tasks_image_tk)

    def openTasks(self):
        # click_sound.play()
        self.studi_frame.destroy()
        TasksPage(root)

    def clicked(self):
        # click_sound.play()
        pass

    def exit_program(self):
        self.studi_frame.destroy()
        exit()


class TasksPage:
    def __init__(self, parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Tasks_Page.png")
        self.background_image = self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill=BOTH, expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk,
                                 borderwidth=0)  # Creates a label, which holds the background image
        self.image_label.place(relwidth=1, relheight=1)  # Ensures that the label/image fits the entire screen

        self.user_image = Image.open("User.png")
        self.user_image_tk = ImageTk.PhotoImage(self.user_image)

        self.settings_image = Image.open("Settings.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)

        self.timer_image = Image.open("Timer.png")
        self.small_timer_image = self.timer_image.resize((240, 108))
        self.timer_image_tk = ImageTk.PhotoImage(self.small_timer_image)

        self.exit_image = Image.open("Exit.png")
        self.exit_image_Tk = ImageTk.PhotoImage(self.exit_image)

        self.user_button = Button(self.studi_frame, image=self.user_image_tk, command=self.clicked, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.user_button.place(relx=0.85, rely=0.022)
        self.user_button.bind("<Enter>", self.user_on_enter)
        self.user_button.bind("<Leave>", self.user_on_leave)

        self.settings_button = Button(self.studi_frame, image=self.settings_image_tk, command=self.clicked,
                                      cursor="hand2", bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.settings_button.place(relx=0.9, rely=0.022)
        self.settings_button.bind("<Enter>", self.settings_on_enter)
        self.settings_button.bind("<Leave>", self.settings_on_leave)

        self.exit_button = Button(self.studi_frame, image=self.exit_image_Tk, command=self.exit_program, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.exit_button.place(relx=0.95, rely=0.027)
        self.exit_button.bind("<Enter>", self.exit_on_enter)
        self.exit_button.bind("<Leave>", self.exit_on_leave)

        self.timer_button = Button(self.studi_frame, image=self.timer_image_tk, command=self.openTimer, bg="#a60c09",
                                   activebackground="#a60c09", cursor="hand2", borderwidth=0, )
        self.timer_button.place(relx=0.85, rely=0.86)
        pywinstyles.set_opacity(self.timer_button, color="#a60c09")
        self.timer_button.bind("<Enter>", self.timer_on_enter)
        self.timer_button.bind("<Leave>", self.timer_on_leave)

        self.subject_1 = customtkinter.CTkButton(
            self.studi_frame,
            text="placeholder 1",
            font=('Mont Heavy DEMO', 40),
            height=100,
            width=100,
            text_color="black",
            fg_color="#dbdbdb",
            corner_radius=50,
            bg_color="#a60c09",
            hover_color="#c2c0c0"
        )
        self.subject_1.place(relx=0.03, rely=0.185)
        pywinstyles.set_opacity(self.subject_1, color="#a60c09")

        self.subject_2 = customtkinter.CTkButton(
            self.studi_frame,
            text="placeholder 2",
            font=('Mont Heavy DEMO', 40),
            height=100,
            width=100,
            text_color="black",
            fg_color="#dbdbdb",
            corner_radius=50,
            bg_color="#a60c09",
            hover_color="#c2c0c0")
        self.subject_2.place(relx=0.03, rely=0.345)
        pywinstyles.set_opacity(self.subject_2, color="#a60c09")

        self.subject_3 = customtkinter.CTkButton(
            self.studi_frame,
            text="placeholder 3",
            font=('Mont Heavy DEMO', 40),
            height=100,
            width=100,
            text_color="black",
            fg_color="#dbdbdb",
            corner_radius=50,
            bg_color="#a60c09",
            hover_color="#c2c0c0")
        self.subject_3.place(relx=0.03, rely=0.505)
        pywinstyles.set_opacity(self.subject_3, color="#a60c09")

        self.subject_4 = customtkinter.CTkButton(
            self.studi_frame,
            text="placeholder 4",
            font=('Mont Heavy DEMO', 40),
            height=100,
            width=100,
            text_color="black",
            fg_color="#dbdbdb",
            corner_radius=50,
            bg_color="#a60c09",
            hover_color="#c2c0c0")
        self.subject_4.place(relx=0.03, rely=0.665)
        pywinstyles.set_opacity(self.subject_4, color="#a60c09")

        self.subject_5 = customtkinter.CTkButton(
            self.studi_frame,
            text="placeholder 5",
            font=('Mont Heavy DEMO', 40),
            height=100,
            width=100,
            text_color="black",
            fg_color="#dbdbdb",
            corner_radius=50,
            bg_color="#a60c09",
            hover_color="#c2c0c0")
        self.subject_5.place(relx=0.03, rely=0.825)
        pywinstyles.set_opacity(self.subject_5, color="#a60c09")

        self.enter_tasks = customtkinter.CTkEntry(
            self.studi_frame,
            placeholder_text="Enter Your Task",
            font=('Mont Heavy DEMO', 30),
            width=450,
            height=30,
            text_color="black",
            fg_color="#dbdbdb",
        )
        self.enter_tasks.place(relx=0.46, rely=0.74)

        self.add_button = customtkinter.CTkButton(
            self.studi_frame,
            text="ADD +",
            font=('Gaco Strong Demo', 30),
            text_color="white",
            fg_color="#bb5fc9",
            width=-50,
            height=-20,
            corner_radius=0,
            border_spacing=6,
            border_color="#9d0905",
            hover_color="#8d4b96",
            command=self.add_task
        )
        self.add_button.place(relx=0.698, rely=0.739)

        self.edit_button = customtkinter.CTkButton(
            self.studi_frame,
            text="EDIT 🖍",
            font=('Gaco Strong Demo', 30),
            text_color="white",
            fg_color="#d18c02",
            width=-50,
            height=-20,
            corner_radius=0,
            border_spacing=6,
            border_color="#9d0905",
            hover_color="#ad7402",
            command=self.edit_task
        )
        self.edit_button.place(relx=0.767, rely=0.739)

        self.delete_button = customtkinter.CTkButton(
            self.studi_frame,
            text="DELETE 🗑",
            font=('Gaco Strong Demo', 30),
            text_color="white",
            fg_color="#c9242d",
            width=-50,
            height=-20,
            corner_radius=10,
            border_spacing=6,
            border_color="#9d0905",
            hover_color="#a81e26",
            command=self.delete_task
        )
        self.delete_button.place(relx=0.355, rely=0.74)

        self.complete_button = customtkinter.CTkButton(
            self.studi_frame,
            text="COMPLETE ✔",
            font=('Gaco Strong Demo', 30),
            text_color="white",
            fg_color="#378714",
            width=-50,
            height=-20,
            corner_radius=50,
            border_spacing=6,
            border_color="#9d0905",
            hover_color="#2c6b10",
            command=self.complete_task
        )
        self.complete_button.place(relx=0.5, rely=0.69)

        self.tasks_list = Listbox(
            self.studi_frame,
            font=("Mont Heavy DEMO", 22),
            width=50,
            bg="#edebf2",
            bd=0,
            highlightthickness=0,
            selectbackground="#8e8d8f",
            activestyle="none"
        )
        self.tasks_list.place(anchor="center", relx=0.52, rely=0.42)

        self.tasks_list = Listbox(
            self.studi_frame,
            font=("Mont Heavy DEMO", 22),
            width=50,
            bg="#edebf2",
            bd=0,
            highlightthickness=0,
            selectbackground="#8e8d8f",
            activestyle="none"
        )
        self.tasks_list.place(anchor="center", relx=0.52, rely=0.42)

        self.list = ["Finish Homework", "Do project", "Sleep", "test123", "hi hello"]
        for item in self.list:
            self.tasks_list.insert(END, item)

        self.tasks_scrollbar = Scrollbar(self.studi_frame)
        self.tasks_scrollbar.place(relx=0.9, rely=0.24, relheight=0.5)

        self.tasks_list.config(yscrollcommand=self.tasks_scrollbar)
        self.tasks_scrollbar.config(command=self.tasks_list.yview)

    def add_task(self):
        self.tasks_list.insert(END,self.enter_tasks.get())
        self.enter_tasks.delete(0,END)

    def edit_task(self):
        print(self.enter_tasks.get())

    def delete_task(self):
        self.tasks_list.delete(ANCHOR)

    def complete_task(self):
        print(self.enter_tasks.get())

    def clicked(self):
        # click_sound.play()
        pass

    def openTimer(self):
        # click_sound.play()
        self.studi_frame.destroy()
        TimerPage(root)

    def exit_program(self):
        self.studi_frame.destroy()
        exit()

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

    def timer_on_enter(self, event):
        self.timer_image = Image.open("Timer_Hover.png")
        self.small_timer_image = self.timer_image.resize((240, 108))
        self.timer_image_tk = ImageTk.PhotoImage(self.small_timer_image)
        self.timer_button.config(image=self.timer_image_tk)

    def timer_on_leave(self, event):
        self.timer_image = Image.open("Timer.png")
        self.small_timer_image = self.timer_image.resize((240, 108))
        self.timer_image_tk = ImageTk.PhotoImage(self.small_timer_image)
        self.timer_button.config(image=self.timer_image_tk)


# Runs the program
if __name__ == "__main__":  # Ensures the code only runs when the program is executed
    root = Tk()
    canvas = Canvas(root)
    root.title("Studi")  # Sets the title of the window to "Studi"
    root.attributes("-fullscreen", True)  # Makes the window fullscreen
    studi_instance = MenuPage(root)  # Creates an instance of the MenuPage class
    root.mainloop()  # Starts the window loop until the user closes it
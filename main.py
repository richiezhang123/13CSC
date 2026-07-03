from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import customtkinter
import pywinstyles
# import pygame
import pyglet
from tkinter import filedialog
import pickle
import os

from pyglet.window.key import LCOMMAND

cwd = os.getcwd()


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

        self.settings_button = Button(self.studi_frame, image=self.settings_image_tk, command=self.openSettings,
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

    def openSettings(self):
        global current_page
        current_page = "Menu"
        self.studi_frame.destroy()
        SettingsPage(root)

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

        self.settings_image = Image.open("Settings.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)

        self.tasks_image = Image.open("Tasks.png")
        self.small_tasks_image = self.tasks_image.resize((240, 108))
        self.tasks_image_tk = ImageTk.PhotoImage(self.small_tasks_image)

        self.exit_image = Image.open("Exit.png")
        self.exit_image_Tk = ImageTk.PhotoImage(self.exit_image)

        self.settings_button = Button(self.studi_frame, image=self.settings_image_tk, command=self.openSettings,
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
            hover_color="#8c0603",
            command = self.start_normal_timer
            )
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

        self.info_button = customtkinter.CTkButton(
            self.studi_frame,
            font=('Mont Heavy DEMO',30),
            text = "?",
            command = self.open_info,
            border_width=-10,
            width=80,
            fg_color = "#750705",
            hover_color= "#4d0100"
        )
        self.info_button.place(relx=0.85,rely=0.295)

        self.timer_label = Label(self.studi_frame, text=timer_length+":00", font=('Gaco Strong Demo', 125), fg="white",
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
        self.timer_id = None



    def open_info(self):
        self.info_button.destroy()
        self.exit_info_button = customtkinter.CTkButton(
            self.studi_frame,
            font=('Mont Heavy DEMO',30),
            text = "X",
            border_width=-10,
            width=80,
            fg_color = "#750705",
            hover_color= "#4d0100",
            command = self.close_help
        )
        self.exit_info_button.place(relx=0.85,rely=0.295)

        self.help_text = customtkinter.CTkLabel(
            self.studi_frame,
            text = """Click on the Settings Button above to 
            adjust the length of the Timer, Short Break and Long Break.                
                   
    Clicking the Short Break and Long Break 
    buttons will automatically start the timer.
                       
    Default Lengths: 
    Timer = 25 Minutes
    Short Break = 5 Minutes
    Long Break = 15 Minutes""",
            font = ("Mont Heavy DEMO", 35),
            width=20,
            bg_color = "#ced6d0",
            text_color= "black"
        )
        self.help_text.place(relx=0.176, rely=0.36)

    def close_help(self):
        self.info_button = customtkinter.CTkButton(
            self.studi_frame,
            font=('Mont Heavy DEMO',30),
            text = "?",
            command = self.open_info,
            border_width=-10,
            width=80,
            fg_color = "#750705",
            hover_color= "#4d0100"
        )
        self.info_button.place(relx=0.85,rely=0.295)
        self.exit_info_button.destroy()
        self.help_text.destroy()

    def cancel_timer(self):
        if self.timer_id:
            self.studi_frame.after_cancel(self.timer_id)
            self.timer_id = None


    def start_timer(self):
        global timer_length
        if not self.is_timer_running:
            self.cancel_timer()

            if self.is_paused:
                self.is_timer_running = True
                self.timer_status.configure(text="Timer Running")
                self.update_timer()
            else:
                self.time_remaining = int(timer_length) * 60
                self.is_timer_running = True
                self.timer_status.configure(text="Timer Running")
                self.update_timer()

    def start_normal_timer(self):
        global timer_length
        self.cancel_timer()
        self.time_remaining = int(timer_length) * 60
        self.is_timer_running = True
        self.is_paused = False
        self.timer_status.configure(text="Timer Running")
        self.update_timer()

    def start_short(self):
        self.cancel_timer()
        self.time_remaining = int(5) * 60
        self.is_timer_running = True
        self.is_paused = False
        self.timer_status.configure(text="Timer Running")
        self.update_timer()

    def start_long(self):
        self.cancel_timer()
        self.time_remaining = int(10) * 60
        self.is_timer_running = True
        self.is_paused = False
        self.timer_status.configure(text="Timer Running")
        self.update_timer()

    def pause_timer(self):
        self.cancel_timer()
        self.is_timer_running = False
        self.is_paused = True
        self.timer_status.configure(text="Timer Paused")

    def reset_timer(self):
        if any(char in "!@#$%^&*()-_=+`~[]{}|;:'\",<.>?/\\" for char in self.minute_entry.get()):
            self.timer_status.configure(text="Cannot have special characters, try again!")
        elif self.minute_entry.get().strip() == "":
            self.timer_status.configure(text="Please enter a number, try again!")
        elif any(char in "abcdefghijklmnopqrstuvwxyz" for char in self.minute_entry.get().lower()):
            self.timer_status.configure(text="Cannot have letters, try again!")
        else:
            self.cancel_timer()
            self.is_timer_running = False
            self.is_paused = False
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
            self.timer_id = self.studi_frame.after(1000, self.update_timer)
            print("HI!!")
        elif self.is_timer_running:
            self.timer_label.config(text="00:00")
            self.timer_status.configure(text="Timer Finished!")
            self.is_paused = None

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

    def openSettings(self):
        global current_page
        current_page = "Timer"
        self.studi_frame.destroy()
        SettingsPage(root)


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
                                 borderwidth=0)
        self.image_label.place(relwidth=1, relheight=1)

        self.settings_image = Image.open("Settings.png")
        self.settings_image_tk = ImageTk.PhotoImage(self.settings_image)

        self.timer_image = Image.open("Timer.png")
        self.small_timer_image = self.timer_image.resize((240, 108))
        self.timer_image_tk = ImageTk.PhotoImage(self.small_timer_image)

        self.exit_image = Image.open("Exit.png")
        self.exit_image_Tk = ImageTk.PhotoImage(self.exit_image)


        self.settings_button = Button(self.studi_frame, image=self.settings_image_tk, command=self.openSettings,
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

        self.enter_tasks = customtkinter.CTkEntry(
            self.studi_frame,
            placeholder_text="Enter Your Task",
            font=('Mont Heavy DEMO', 30),
            width=450,
            height=30,
            text_color="black",
            fg_color="#dbdbdb",
        )
        self.enter_tasks.place(relx=0.28, rely=0.74)

        self.add_button = customtkinter.CTkButton(
            self.studi_frame,
            text="ADD +",
            font=('Gaco Strong Demo', 30),
            text_color="white",
            fg_color="#378714",
            width=-50,
            height=-20,
            corner_radius=0,
            border_spacing=6,
            border_color="#9d0905",
            hover_color="#2c6b10",
            command=self.add_task
        )
        self.add_button.place(relx=0.518, rely=0.739)

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
        self.edit_button.place(relx=0.695, rely=0.739)

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
        self.delete_button.place(relx=0.587, rely=0.739)

        self.complete_button = customtkinter.CTkButton(
            self.studi_frame,
            text="COMPLETE ✔",
            font=('Gaco Strong Demo', 30),
            text_color="white",
            fg_color="#5192d6",
            width=-50,
            height=-20,
            corner_radius=50,
            border_spacing=6,
            border_color="#9d0905",
            hover_color="#346291",
            command=self.complete_task
        )
        self.complete_button.place(relx=0.775, rely=0.739)

        self.tasks_list = Listbox(
            self.studi_frame,
            font=('Mont Heavy DEMO', 22),
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
            font=('Mont Heavy DEMO', 22),
            width=50,
            bg="#edebf2",
            bd=0,
            highlightthickness=0,
            selectbackground="#8e8d8f",
            activestyle="none"
        )
        self.tasks_list.place(anchor="center", relx=0.52, rely=0.42)

        self.tasks_scrollbar = Scrollbar(self.studi_frame, highlightcolor="red")
        self.tasks_scrollbar.place(relx=0.7679, rely=0.225, relheight=0.4)

        self.tasks_list.config(yscrollcommand=self.tasks_scrollbar.set)
        self.tasks_scrollbar.config(command=self.tasks_list.yview)

        self.save_button = customtkinter.CTkButton(
            self.studi_frame,
            text="SAVE",
            font=('Gaco Strong Demo', 50),
            text_color="white",
            fg_color="#e07f00",
            width=300,
            height=300,
            border_spacing=6,
            border_width=-5,
            hover_color="#a35e03",
            command=self.save_list
        )
        self.save_button.place(relx=0.05, rely=0.20)

        self.help_text = Label(
            self.studi_frame,
            text = "Enter your subject",
            font = ('Mont Heavy DEMO',22),
            bg = "#b56904",
            fg = "black"
        )
        self.help_text.place(relx=0.058,rely=0.38)
        pywinstyles.set_opacity(self.help_text,color = "#b56904")

        self.help_text2 = Label(
            self.studi_frame,
            text = "as the file name",
            font = ('Mont Heavy DEMO',22),
            bg = "#b56904",
            fg = "black"
        )
        self.help_text2.place(relx=0.066,rely=0.412)
        pywinstyles.set_opacity(self.help_text2,color = "#b56904")

        self.open_button = customtkinter.CTkButton(
            self.studi_frame,
            text="OPEN",
            font=('Gaco Strong Demo', 50),
            text_color="white",
            fg_color="#376dab",
            width=300,
            height=300,
            border_spacing=6,
            border_width=-5,
            hover_color="#23466e",
            command=self.open_list
        )
        self.open_button.place(relx=0.05, rely=0.525)



    def add_task(self):
        global task
        task = self.enter_tasks.get()
        if task.strip() == "":
            pass
        else:
            self.tasks_list.insert(END,"• " + task)
            self.enter_tasks.delete(0,END)

    def edit_task(self):
        if task.strip() == "":
            pass
        else:
            for item in self.tasks_list.curselection():
                self.tasks_list.delete(item)
                self.tasks_list.insert(item,task)

    def delete_task(self):
        self.tasks_list.delete(ANCHOR)

    def complete_task(self):
        self.tasks_list.itemconfig(
            self.tasks_list.curselection(),fg="#dedede"
        )
        self.tasks_list.selection_clear(0,END)

    def save_list(self):
        file_name = filedialog.asksaveasfilename(
            initialdir=cwd,
            initialfile="",
            title = "Save File",
            filetypes = (("Dat Files", "*.dat"),
                         ("All Files", "*.*"))
        )

        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name=f'{file_name}.dat'

        tasks = self.tasks_list.get(0,END)
        output = open(file_name, 'wb')
        pickle.dump(tasks, output)

    def open_list(self):
        file_name = filedialog.askopenfilename(
            initialdir=cwd,
            title = "Open File",
            filetypes=(("Dat Files", "*.dat"),("All Files","*.*"))
        )
        if file_name:
            self.tasks_list.delete(0,END)

            input_file = open(file_name, 'rb')
            tasks = pickle.load(input_file)

            for item in tasks:
                self.tasks_list.insert(END,item)

    def clicked(self):
        # click_sound.play()
        pass

    def openTimer(self):
        # click_sound.play()
        self.studi_frame.destroy()
        TimerPage(root)

    def openSettings(self):
        global current_page
        current_page = "Tasks"
        self.studi_frame.destroy()
        SettingsPage(root)

    def exit_program(self):
        self.studi_frame.destroy()
        exit()

    def sub1(self):
        pass

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

class SettingsPage:
    def __init__(self, parent):
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()

        self.background_image = Image.open("Settings_Page.png")
        self.background_image = self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS)
        self.background_image_tk = ImageTk.PhotoImage(self.background_image)

        self.studi_frame = Frame(parent)
        self.studi_frame.pack(fill=BOTH, expand=TRUE)

        self.image_label = Label(self.studi_frame, image=self.background_image_tk,
                                 borderwidth=0)  # Creates a label, which holds the background image
        self.image_label.place(relwidth=1, relheight=1)  # Ensures that the label/image fits the entire screen

        self.exit_image = Image.open("Exit.png")
        self.exit_image_Tk = ImageTk.PhotoImage(self.exit_image)

        self.timer_text = customtkinter.CTkLabel(
            self.studi_frame,
            text = "Timer",
            text_color="black",
            font=("Mont Heavy DEMO", 38),
            fg_color="#f6f6f6"
        )
        self.timer_text.place(relx=0.47,rely=0.38)
        self.timer_entry = customtkinter.CTkEntry(
            self.studi_frame,
            placeholder_text="TIMER LENGTH (in minutes)",
            font=("Mont Heavy DEMO", 28),
            width = 395,
            height=65,
            fg_color= "#c7c7c7",
            text_color="black",
            border_width=0,
            justify = CENTER,
        )
        self.timer_entry.place(relx=0.4,rely=0.44)
        self.timer_entry_button = customtkinter.CTkButton(
            self.studi_frame,
            text="APPLY",
            corner_radius=40,
            font=("Mont Heavy DEMO", 35),
            fg_color="#56b873",
            hover_color="#468c5b",
            border_width=0,
            command = self.timer_add
        )
        self.timer_entry_button.place(relx=0.464, rely=0.52)

        self.short_timer_text = customtkinter.CTkLabel(
            self.studi_frame,
            text = "Short Timer",
            text_color="black",
            font=("Mont Heavy DEMO", 38),
            fg_color="#f6f6f6"
        )
        self.short_timer_text.place(relx=0.27,rely=0.585)
        self.short_timer_entry = customtkinter.CTkEntry(
            self.studi_frame,
            placeholder_text="SHORT TIMER LENGTH (in minutes)",
            font=("Mont Heavy DEMO", 28),
            width = 395,
            height=65,
            fg_color= "#c7c7c7",
            text_color="black",
            border_width=0,
            justify = CENTER,
        )
        self.short_timer_entry.place(relx=0.23,rely=0.65)
        self.short_timer_entry_button = customtkinter.CTkButton(
            self.studi_frame,
            text="APPLY",
            corner_radius=40,
            font=("Mont Heavy DEMO", 35),
            fg_color="#56b873",
            hover_color="#468c5b",
            border_width=0,
            command = self.timer_add
        )
        self.short_timer_entry_button.place(relx=0.29, rely=0.725)

        self.long_timer_text = customtkinter.CTkLabel(
            self.studi_frame,
            text = "Short Timer",
            text_color="black",
            font=("Mont Heavy DEMO", 38),
            fg_color="#f6f6f6"
        )
        self.long_timer_text.place(relx=0.58,rely=0.585)
        self.long_timer_entry = customtkinter.CTkEntry(
            self.studi_frame,
            placeholder_text="SHORT TIMER LENGTH (in minutes)",
            font=("Mont Heavy DEMO", 28),
            width = 395,
            height=65,
            fg_color= "#c7c7c7",
            text_color="black",
            border_width=0,
            justify = CENTER,
        )
        self.long_timer_entry.place(relx=0.58,rely=0.65)
        self.long_timer_entry_button = customtkinter.CTkButton(
            self.studi_frame,
            text="APPLY",
            corner_radius=40,
            font=("Mont Heavy DEMO", 35),
            fg_color="#56b873",
            hover_color="#468c5b",
            border_width=0,
            command = self.timer_add
        )
        self.long_timer_entry_button.place(relx=0.58, rely=0.725)

        self.return_button = customtkinter.CTkButton(
            self.studi_frame,
            text="←",
            font = ("Gaco Strong Demo", 75),
            border_width=0,
            width=70,
            fg_color="#8f0401",
            bg_color="#8f0401",
            hover_color="#750401",
            command = self.return_page
        )
        self.return_button.place(relx=0.02,rely=0.01)

        self.exit_button = Button(self.studi_frame, image=self.exit_image_Tk, command=self.exit_program, cursor="hand2",
                                  bg="#8d0401", borderwidth=0, activebackground="#8d0401")
        self.exit_button.place(relx=0.95, rely=0.027)

    def timer_add(self):
        global timer_length
        timer_length = self.timer_entry.get()

    def return_page(self):
        global current_page
        if current_page=="Menu":
            print("MENU")
            self.studi_frame.destroy()
            MenuPage(root)

        elif current_page == "Timer":
            print("TIMER")
            self.studi_frame.destroy()
            TimerPage(root)

        elif current_page == "Tasks":
            print("TASKS")
            self.studi_frame.destroy()
            TasksPage(root)

    def exit_program(self):
        self.studi_frame.destroy()
        exit()

# Runs the program
if __name__ == "__main__":  # Ensures the code only runs when the program is executed
    root = Tk()
    canvas = Canvas(root)
    root.title("Studi")  # Sets the title of the window to "Studi"
    root.attributes("-fullscreen", True)  # Makes the window fullscreen
    studi_instance = MenuPage(root)  # Creates an instance of the MenuPage class
    root.mainloop()  # Starts the window loop until the user closes it
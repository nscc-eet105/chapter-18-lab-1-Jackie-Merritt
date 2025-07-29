#Jackie-Merritt_Chp18-Lab1_7/27/2025

import tkinter
import tkinter.messagebox

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('')

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.title = tkinter.Label(self.top_frame, text='Feet and Inches Converter')

        self.title.pack(side='top')

        self.entry_label1 = tkinter.Label(self.middle_frame, text='Feet: ')
        
        self.feet_entry = tkinter.Entry(self.middle_frame, width=3)
        

        self.entry_label2 = tkinter.Label(self.middle_frame, text='Inches: ')
        
        self.inches_entry = tkinter.Entry(self.middle_frame, width=3)

        self.inches_label = tkinter.Label(self.bottom_middle_frame, text='Inches: ')

        self.value = tkinter.StringVar()
        self.inches_display = tkinter.Label(self.bottom_middle_frame, textvariable=self.value)

        self.convert_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy)

        self.entry_label1.pack(side='left')
        self.feet_entry.pack(side='left')
        self.entry_label2.pack(side='left')
        self.inches_entry.pack(side='left')
        self.inches_label.pack(side='left')
        self.inches_display.pack(side='left')
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_middle_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()

    def convert(self):
        feet = int(self.feet_entry.get())

        inches = int(self.inches_entry.get())

        conv = (feet * 12) + inches

        self.value.set(conv)


if __name__ == '__main__':
    my_gui = My_GUI()

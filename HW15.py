#Author: David Hernandez
#Description: This program calculates windchill from the user's input of fahrenheit temperature and wind speed.

#Imports tkinter to be used in the program.
import tkinter

class windchill_calculator_GUI:
    def __init__(self):

        #This part creates the main window for the program.
        self.main_window = tkinter.Tk()
        self.main_window.title("Windchill Calculator")

        #This section creates five frames to group widgets.
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()

        #Create the widget for frame1.
        self.title_label = tkinter.Label(self.frame1,
                    text='Windchill Calculator',
                    font = ('verdana', 12))

        #Creates the widget for frame2.
        self.prompt_label = tkinter.Label(self.frame2,
                    text='Enter the temperature in degrees Fahrenheit:')
        self.fahrenheit_entry = tkinter.Entry(self.frame2,
                    width=10)

        #Creates the widget for frame3.
        self.prompt_two = tkinter.Label(self.frame3,
                    text='Enter the wind speed in mph:')
        self.wind_speed_entry = tkinter.Entry(self.frame3,
                    width=10)

        #Creates the widget for frame4.
        self.magic_button = tkinter.Button(self.frame4,
                    text='Calculate Windchill',
                    command = self.convert)

        #Creates the widget for frame5.
        self.result = tkinter.Label(self.frame5,
                    text='The windchill temperature is:')

        #Pack all the frame widgets.
        self.title_label.pack()
        self.prompt_label.pack(side='left')
        self.fahrenheit_entry.pack(side='left')
        self.prompt_two.pack(side='left')
        self.wind_speed_entry.pack(side='left')
        self.magic_button.pack()
        self.result.pack()

        #Pack the frames into the main window.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    #This part manages the calculations of windchill by taking the users' input of wind speed and temperature.
    def convert(self):

        #These lines define the variables temperature and wind speed with values input by the user earlier.
        temperature = float(self.fahrenheit_entry.get())
        wind_speed = float(self.wind_speed_entry.get())

        #This section calculates windchill and formats it.
        windchill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
        windchill = ("%.1f" % windchill)

        #These lines remove the last text piece of the GUI and puts it back with the appropriate wind chill result from the calculations.
        self.frame5.pack_forget()
        self.result.pack_forget()
        self.result = tkinter.Label(self.frame5,
                    text='The windchill temperature is: '+str(windchill))
        self.frame5.pack()
        self.result.pack()

#Create an instance of the windchill_calcultor_GUI class.
windchill_calculate = windchill_calculator_GUI()

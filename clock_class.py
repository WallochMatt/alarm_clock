class Alarm:
    def __init__(self, time, set_to):
        self.display_time = time
        self.is_on = False #use switch method to toggle to ture
        self.time_set_to = set_to

    def set_display_time(self):#parameter may be needed
        # time = input("Set the time: ")
        # print(time)
        self.display_time = input("Set the time: ")
        print(self.display_time)

    def switch(self):  #self.is_on showed as True in debugger stepping, works
        choice = int(input("Would you like the alarm clock on? \n ON: 1 \n OFF: 2 \n"))
        if choice == 1:#ON
            self.is_on = True
        if choice == 2:#OFF
            self.is_on = False
 


    def current_alarm_time(self):
        self.time_set_to = input("Set the alarm: ")
        print(self.time_set_to)


    def show_me_time(self):
        print(self.display_time)
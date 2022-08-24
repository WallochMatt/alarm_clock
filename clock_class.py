class Alarm:
    def __init__(self, time):
        self.display_time = time
        self.is_on = False #use switch method to toggle to ture
        self.time_set_to = "5:00"
        pass

    def set_display_time(self):#parameter may be needed
        self.display_time = input("Set the time: ")
        print(self.display_time)

    def switch(self):
        if self.is_on == False:
            choice = int(input("Turn on?: \n ON: 1 \n OFF: 2"))
            if choice == 1: 
                self.is_on = True
            elif choice == 2:
                self.is_on = False


    def current_alarm_time(self):
        self.time_set_to = input("Set the alarm: ")
        print(self.time_set_to)



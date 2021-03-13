from datetime import *
import pickle
import os

def daily_log_checker(type):

    try:
        todays_log = pickle.load(open(type + "_logs/" +date_str +".py", "rb"))
    except (FileNotFoundError):
            os.mkdir(type + "_logs")
    try:
        todays_log = pickle.load(open(type + "_logs/" +date_str +".py", "rb"))
    except (IndexError, IOError, EOFError,):
    
            spawner = open((type + "_logs/" +date_str +".py"), "a")
            spawner.close
            todays_log = []
            pickle.dump(todays_log,(open(type + "_logs/" +date_str +".py", "wb")))    
     
    return todays_log
         
def general_pickler(type, input,):

    def pickle_dumper(obj_to_append, type):
    
        todays_log = pickle.load(open(type + "_logs/" +date_str +".py", "rb"))
        todays_log.append(obj_to_append)
        pickle.dump(todays_log,open(type + "_logs/" +date_str +".py", "wb"))
        
        
    time_obj = datetime.time(now)
    time_str = str(time_obj)
    
    
    obj_to_append = [time_str, input]
    print(obj_to_append)
    pickle_dumper(obj_to_append, type)

#potential_edit: if an input is empty, it shouldn't get entered into the log
now = datetime.now()
date_obj = datetime.date(now)
date_str = str(date_obj)

class Consumptive:
    def __init__(self, name, verb, input_string):
        self.name = name
        self.verb = verb
        self.input_string = input_string
 
    def solicit_input(self):
        response =input(self.input_string)
        if self.name == "weed":
            if response == 1:
                response = "Bowl"
            if response == 2:
                response = "Dose(s) of Oil"
            
        general_pickler(self.name, response)
        return response
    
    def squawker(self):
        daily_log = (daily_log_checker(self.name))
        if len(daily_log) == 0:
            print("You have not {} {} yet today".format(self.verb, self.name))
        if len(daily_log) == 1:
            print("you last {} {} it was {} and you ended it at {}".format(self.verb, self.name, daily_log[-1][1],daily_log[-1][0]))
        if len(daily_log) >= 2:
            print("you last {} {} it was {} and you ended it at {}".format(self.verb, self.name, daily_log[-1][1],daily_log[-1][0]))
            print("and before that you {} {} it was {} and it was at {}".format(self.verb, self.name, daily_log[-2][1],daily_log[-2][0]))


food = Consumptive("food", "eaten", "What did you eat?")     
weed = Consumptive("weed", "consumed", "1 for bowl, 2 for oil.")
wackage = Consumptive("wackage", "beaten", "On a scale of 1-5 rate your experience.")
MEAT = Consumptive("break", "taken", "What were you doing in cyberspace before this break?")
cyber = Consumptive("cyber", "dove", "What were you doing in meatspace prior to this dive?")
caffeine = Consumptive("caffeine", "consumed", "What kind of caffiene did you consume?")       
water = Consumptive("water", "drank", "How do you feel now that you have quafed a container of water?")
consumptive_list = [food, weed, wackage, MEAT, cyber, caffeine,water]

#consumptives in consideration for adding


    
def interface():
    for i in range(0,30):
        print(" ")
    list_pos = 0
    
    for each in consumptive_list:
        str_list_post = str(list_pos)
        print(str_list_post +". " + each.name + " Tracker:")
        daily_log_checker(each.name)
        
        each.squawker()
        
        print("*****************")
        list_pos += 1
    
    
    for i in range(0,5):
        print(" ")
        
        
    selection = input("Select your tracker")     
    selection = int(selection)
    
    consumptive_list[selection].solicit_input()

    
   
        
interface()
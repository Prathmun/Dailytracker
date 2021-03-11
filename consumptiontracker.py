from datetime import *
import pickle


#if an input is empty, it shouldn't get entered into the log
now = datetime.now()
date_obj = datetime.date(now)
date_str = str(date_obj)

class Consumptive:
    def __init__(self, name, verb, input_string):
        sef.name = name
        self.verb = verb
        self.input_string = input_string
 
    def solicit_input():
        response =input(self.input_string)
        general_pickler(self.name, response)
        return response
    
    def squawker():
        daily_log = (daily_log_checker(name))
        if len(daily_log) == 0:
            print("You have not {} {} yet today".format(self.verb, self.name))
        if len(daily_log) == 1:
            print("you last {} {} it was {} and you ended it at {}".format(self.verb, self.name, daily_log[-1][1],daily_log[-1][0]))
        if len(daily_log) >= 2:
            print("you last {} {} it was {} and you ended it at {}".format(self.verb, self.name, daily_log[-1][1],daily_log[-1][0]))
            print("and before that you {} {} it was {} and it was at {}".format(self.verb, self.name, daily_log[-2][1],daily_log[-2][0]))
     
        
def daily_log_checker(type):

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



def cyberspace_squawker():
    daily_log = daily_log_checker("cyberspace")
    if len(daily_log) == 0:
        print("You have not left meatspace yet today")
    if len(daily_log) == 1:
        print("your last meatdance was about {} and you ended it at {}".format(daily_log[-1][1],daily_log[-1][0]))
    if len(daily_log) >= 2:
        print("Before your last entrance to cyberspace you were doing: {} and you entered at {}".format(daily_log[-1][1],daily_log[-1][0]))
        print("and before that you did {} at {}".format(daily_log[-2][1],daily_log[-2][0]))
def break_squawker():
    daily_log = daily_log_checker("break")
    if len(daily_log) == 0:
        print("You have not left cyberspace today")
    if len(daily_log) == 1:
        print("Your last dive was about {} and you ended it at {}".format(daily_log[-1][1],daily_log[-1][0]))
    if len(daily_log) >= 2:
        print("Your last dive was about {} and you ended it at {}".format(daily_log[-1][1],daily_log[-1][0]))
        print("and the one before that was about {} and ended atat {}".format(daily_log[-2][1],daily_log[-2][0]))
def food_squawker():
    daily_log = daily_log_checker("food")
    if len(daily_log) == 0:
        print("You have not eaten anything today")
    if len(daily_log) == 1:
        print("you last ate {} at {}".format(daily_log[-1][1],daily_log[-1][0]))
    if len(daily_log) >= 2:
        print("you last ate {} at {}".format(daily_log[-1][1],daily_log[-1][0]))
        print("and before that you ate {} at {}".format(daily_log[-2][1],daily_log[-2][0]))	
def weed_squawker():
    daily_log = daily_log_checker("weed")
    if len(daily_log) == 0:
        print("You have not gotten stoned today")
    if len(daily_log) == 1:
        print("Your last thc dose was at {} and was {}".format(daily_log[-1][0],daily_log[-1][1]))
    if len(daily_log) >= 2:
        print("Your last thc dose was at {} and was a {}".format(daily_log[-1][0],daily_log[-1][1]))
        print("And before thaty our last thc dose was at {} and was a {}".format(daily_log[-2][0],daily_log[-2][1]))	
def wackage_squawker():
    daily_log = daily_log_checker("wackage")
    if len(daily_log) == 0:
        print("You've not wacked it today")
    if len(daily_log) == 1:
        print("You last wacked it at {} and you rated it a {} out of 5".format(daily_log[-1][0],daily_log[-1][1]))
    if len(daily_log) >= 2:
        print("You last wacked it at {} and you rated it a {} out of 5".format(daily_log[-1][0],daily_log[-1][1]))
        print("and before that you last wacked it at {} and you rated it a {} out of 5".format(daily_log[-2][0],daily_log[-2][1]))
    
def interface():
    for i in range(0,30):
        print(" ")
    #for each in consumptive_list:
        #print(NUMBER NAME tracker)
        #daily log tracker(each)
        #each.squawker()
        #print("*****************")
    print("1. Food tracker")
    daily_log_checker("food")
    food_squawker()
    print("*****************")
    print("2. Weed Tracker")
    daily_log_checker("weed")
    weed_squawker()
    print("*****************")
    print("3. Wackage Tracker")
    daily_log_checker("wackage")
    wackage_squawker()
    print("*****************")
    print("4. MEATTRACKER ") 
    daily_log_checker("break")
    break_squawker()
    print("*****************")
    print("5. Cyber Dive Checkpoint")
    daily_log_checker("cyberspace")
    cyberspace_squawker()
    print("*****************")
    
    
    for i in range(0,5):
        print(" ")
        
        
    selection = input("Select your tracker")     
    selection = int(selection)
    
    #consumptive_list[selection].solicit_input()
    if selection == 1:
        foodstring = input("What did you eat?")
        general_pickler("food", foodstring)
        
    if selection == 2:
        oil_or_bowl = input("1 for bowl, 2 for oil")
        oil_or_bowl = int(oil_or_bowl)
        ### OPEN QUESTION ###
        if oil_or_bowl == 1:
            oil_or_bowl = "Bowl"
        if oil_or_bowl == 2:
            oil_or_bowl = "Dose(s) of Oil"
        general_pickler("weed", oil_or_bowl)	
        
    if selection == 3:
        wackage_quality = input("On a scale of 1-5 rate your experience")
        general_pickler("wackage", wackage_quality)
        
    if selection == 4:
        break_type =input(" Prior to your reemergence into meatspace, we have just one question. What was that dive about?")
        general_pickler("break", break_type)
        
    if selection == 5:
        entrance_activity = input("What were you doing in meatspace before this dive? ")
        general_pickler("cyberspace", entrance_activity)
        
interface()
import matplotlib
from matplotlib import pyplot as plt
import os
import pickle
#Data structure
#folder/file/unpickle[listoflogs][logpairs datetime/input]


   #access prototype

   #try:
    #    todays_log = pickle.load(open(type + "_logs/" +date_str +".py", "rb"))
#todays_log = daily_log_checker("wackage")



def dailycounter(type):
    total_logs = len(os.listdir(path=type+ "_logs"))
    daily_totals = []
    for each in os.listdir(path=type+ "_logs"):
        stringed_each= str(each)
        current_log = pickle.load(open(type + "_logs/" +stringed_each, "rb"))
        daily_counter = 0
        for each in current_log:
            daily_counter += 1
        daily_totals.append(daily_counter)
    return daily_totals, total_logs

    

player_selection_input =input("""Which daily instance chart would you like to see?
1. Food
2. Weed
3. Wackage
4. MEAT
5. Cyberdive

Please type your input below

""")
if player_selection_input == "1":
    selection = "food"
if player_selection_input == "2":
    selection = "weed"
if player_selection_input == "3":
    selection = "wackage"
if player_selection_input == "4":
    selection = "break"
if player_selection_input == "5":
    selection = "cyberspace"
if type(selection) != str:
    print("Invalid selection, try again")
else:
    daily_totals, total_logs = dailycounter(selection)        
    ypoints,xpoints = [ y for y in daily_totals], [ x + 1 for x in range(total_logs)]
    plt.plot(xpoints, ypoints)
    plt.ylabel('Quantity')
    plt.xlabel('Day of data')
    plt.show()
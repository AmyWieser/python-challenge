# Import Modules
import os
import csv
import sys

#create variables
month_counter = 0
total_pl = 0
this_month_pl = 0
prior_month_pl = 0
pl_change = 0
change_listing = []
months = []

# Define csv file
budget_data = os.path.join("Resources", "budget_data.csv")
# Define average function
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return round(total / length,2)

# open csvfile:
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# store the header row so it won't be included in calculations
    csv_header = next(csvreader)

    # Loop through the file
    i = -2
    priormonth = []
    for row in csvreader:
        # Add total months
        month_counter = month_counter + 1
        i=i+1
        months.append(row[0])
        # Calulate the total amount of profit/losses
        total_pl = total_pl + int(row[1])

        # Calculate the change in P/L and store as values in a list
          
        priormonth.append(row[1])
        prior_month_pl= int(priormonth[i])
        #print(f"Prior month PL {prior_month_pl}")  

        this_month_pl = int(row[1])
        #print(f"This Month PL {this_month_pl}")
        
        pl_change = this_month_pl - prior_month_pl
        change_listing.append(pl_change)
        #print(f"Change listing {change_listing}")
        
    #Calculate Avg Change in P/L
    change_listing.pop(0)
    avg_change = average(change_listing)

    #Calculate Greatest Inc in P/L
    greatest_increase = change_listing.index(max(change_listing))+1
    greatest_increase_month = months[greatest_increase]
    greatest_increase_pl = change_listing[change_listing.index(max(change_listing))]
    
    #Calculate Greatest Decr in P/L
    greatest_decrease = change_listing.index(min(change_listing))+1
    greatest_decrease_month = months[greatest_decrease]
    greatest_decrease_pl = change_listing[change_listing.index(min(change_listing))]
   


# Print finacial data
print(f"Total Months: {str(month_counter)}")
print(f"Total P/L: ${str(total_pl)}")
print(f"Average Change in P/L: ${str(avg_change)}")
print(f"Greatest Increase in P/L {greatest_increase_month} ${greatest_increase_pl}")
print(f"Greatest Decrease in P/L {greatest_decrease_month} ${greatest_decrease_pl}")

sys.stdout = open('log.txt', 'w')
print(f"Total Months: {str(month_counter)}")
print(f"Total P/L: ${str(total_pl)}")
print(f"Average Change in P/L: ${str(avg_change)}")
print(f"Greatest Increase in P/L {greatest_increase_month} ${greatest_increase_pl}")
print(f"Greatest Decrease in P/L {greatest_decrease_month} ${greatest_decrease_pl}")




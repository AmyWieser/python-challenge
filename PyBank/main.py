# Import Modules
import os
import csv

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

# open csvfile:
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# store the header row so it won't be included in calculations
    csv_header = next(csvreader)

    # Loop through the file
    for row in csvreader:
        # Add total months
        month_counter = month_counter + 1

        # Calulate the total amount of profit/losses
        total_pl = total_pl + int(row[1])

        # Calculate the change in P/L and store as values in a list
        this_month_pl = int(row[1])
        
        if month_counter > 1:
            this_month_pl = total_pl
            pl_change = pl_change + this_month_pl - prior_month_pl
            change_listing.append(pl_change)
        prior_month_pl = total_pl

        #Calculate Avg Change in P/L
        avg_change = change_listing[1]/(month_counter-1)



    # print (row[1])


# Print finacial data
print(f"Total Months: {str(month_counter)}")
print(f"Total P/L: ${str(total_pl)}")
print(f"Average Change in P/L: ${str(avg_change)}")









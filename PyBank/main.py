# import libraries
import os
import csv

# custom maximum function
def maximum(num_list):
     num = num_list[0]

     for i in num_list:
         if i > num:
              num = i
     return num

# custom minimum function
def minimum(num_list):
     num = num_list[0]

     for i in num_list:
          if i < num:
               num = i
     return num

# csv path
budget_path = os.path.join("Resources", "budget_data.csv")

# variables (so I know what is used)
total_months = 0
total_profit = 0
current_cell = 0
profit_change = 0
max_profit_change = 0
min_profit_change = 0
max_index = 0
min_index = 0
max_date = 0
min_date = 0
avg_change = 0
# arrays for max/min functions later
date_list = []
profit_list = []

with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header (row 0)
    budget_header = next(csvreader)

    # read row 1 for initial values
    row_one = next(csvreader)
    total_months = 1
    # row_one[column 1]
    total_profit += int(row_one[1])
    current_cell = int(row_one[1])

    print()

    # loop for all rows
    for row in csvreader:
         # get date_list value (row[column 1])
         date_list.append(row[0])

         # calculate profit_change and add to array
         profit_change = int(row[1])-current_cell
         #  add current profit_change to profit_list
         profit_list.append(profit_change)
        
         #  set new current_cell
         current_cell = int(row[1])

         #  add to month counter
         total_months += 1

         #  add to profit list
         total_profit += int(row[1])
        #  next iteration
    
    # max_profit_change

    # call maximum function
    max_profit_change = maximum(profit_list)
    # find date index using max_profit_change (both index should be the linked)
    max_index = profit_list.index(max_profit_change)
    # find max date
    max_date = date_list[max_index]

    # min_profit_change
    
    # call min function
    min_profit_change = minimum(profit_list)
    # find date index using min_profit_change (both index should be the linked)
    min_index = profit_list.index(min_profit_change)
    # find max date
    min_date = date_list[min_index]

    # calculate average change
    avg_change = sum(profit_list)/len(profit_list)

    # print statements
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {max_date} (${max_profit_change})")
    print(f"Greatest Decrease in Profits: {min_date}, (${min_profit_change})")

    # output path
    output_path = os.path.join("output", "output.txt")
    # exporting written file
    output_txt = open(output_path, "w")
    # create String Array for output
    output_list = ["Financial Analysis\n", 
                   "----------------------------\n", 
                   f"Total Months: {total_months}\n",
                   f"Total: ${total_profit}\n",
                   f"Average Change: ${avg_change:.2f}\n"
                   f"Greatest Increase in Profits: {max_date} (${max_profit_change})\n",
                   f"Greatest Decrease in Profits: {min_date} (${min_profit_change})\n"]
    # write out array
    output_txt.writelines(output_list)
    # close out text
    output_txt.close
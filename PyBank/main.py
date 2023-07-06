#PyBank

import os
import csv

folder_path = os.path.dirname(os.path.realpath(__file__))
budget_data_csv = os.path.join(folder_path, "Resources", "budget_data.csv")

with open(budget_data_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    row_count = 0
    total_profit_loss = 0
    monthly_profit_loss = [] 
    month_names = []

    for row in csvreader:

        profit_loss = int(row[1])
        month = str(row[0])
        
        row_count += 1
        total_profit_loss += profit_loss

        monthly_profit_loss.append(profit_loss)
        month_names.append(month)
    
    avg_profit_loss = 0
    monthly_change = [] 
    month_name_difference = [] 


    for x in range(1, len(monthly_profit_loss)): # https://www.geeksforgeeks.org/python-check-if-previous-element-is-smaller-in-list/#, referenced for how to check for previous item in list

        current_month = int(monthly_profit_loss[x])
        previous_month = int(monthly_profit_loss[x - 1])
        difference = current_month - previous_month

        current_month = str(month_names[x])

        month_name_difference.append(current_month)
        
        avg_profit_loss += (difference)

        monthly_change.append(difference)

    avg_change = avg_profit_loss / (len(monthly_profit_loss) - 1)

    max_index = monthly_change.index(max(monthly_change)) # https://sparkbyexamples.com/python/get-index-of-max-of-list-in-python/, referenced for how to find index for max and min
    min_index = monthly_change.index(min(monthly_change))
    
    analysis = {
        "Months": row_count,
        "Total": total_profit_loss,
        "Average": round(avg_change, 2),
        "Increase": max(monthly_change),
        "High": month_name_difference[max_index],
        "Decrease": min(monthly_change),
        "Low": month_name_difference[min_index]}
    
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {month_name_difference[max_index]} (${max(monthly_change)})")
    print(f"Greatest Decrease in Profits: {month_name_difference[min_index]} (${min(monthly_change)})") 

output_file = os.path.join(folder_path, "analysis", "budget_summary.txt")

with open(output_file, "w") as datafile: # https://www.pythontutorial.net/python-basics/python-write-text-file/, referenced for how to write to txt file
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("---------------------")
    datafile.write("\n")    
    datafile.write(f"Total Months: {row_count}")
    datafile.write("\n")
    datafile.write(f"Total: ${total_profit_loss}")
    datafile.write("\n")
    datafile.write(f"Average Change: ${round(avg_change, 2)}")
    datafile.write("\n")
    datafile.write(f"Greatest Increase in Profits: {month_name_difference[max_index]} (${max(monthly_change)})")
    datafile.write("\n")
    datafile.write(f"Greatest Decrease in Profits: {month_name_difference[min_index]} (${min(monthly_change)})")

        

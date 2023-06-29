import os
import csv

folder_path = os.path.dirname(os.path.realpath(__file__))
budget_data_csv = os.path.join(folder_path, "Resources", "budget_data.csv")


# function to do stuff

# def do_stuff(financial_data):
    # profit_loss = int(financial_data[1])
    # print(profit_loss)

# read in file as dictionary, is that what the "r" argument is for? Ask in class
with open(budget_data_csv, "r") as csvfile:

    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Establish header
    header = next(csvreader)

    row_count = 0
    total_profit_loss = 0
    monthly_profit_loss = [] # do I need to create a second list to store months?
    month_names = []
    # average_change = []

    for row in csvreader:
        # print(row)

        profit_loss = int(row[1])
        month = str(row[0])
        
        row_count += 1
        total_profit_loss += profit_loss

        monthly_profit_loss.append(profit_loss)
        month_names.append(month)

        # average_change.append(int(monthly_profit_loss - int(monthly_change.index(row - 1))))
    
    avg_profit_loss = 0
    monthly_change = [] 
    month_name_difference = [] # create a second list to store month names


    for x in range(1, len(monthly_profit_loss)): # https://www.geeksforgeeks.org/python-check-if-previous-element-is-smaller-in-list/#, how to check for previous item in list

        current_month = int(monthly_profit_loss[x])
        previous_month = int(monthly_profit_loss[x - 1])
        difference = current_month - previous_month

        current_month = str(month_names[x])

        month_name_difference.append(current_month)

        # save current month name

        # print(current_month)
        # print(previous_month)
        
        avg_profit_loss += (difference)

        monthly_change.append(difference)

        


    avg_change = avg_profit_loss / (len(monthly_profit_loss) - 1)
    # do_stuff(row)

    max_index = monthly_change.index(max(monthly_change)) # https://sparkbyexamples.com/python/get-index-of-max-of-list-in-python/, reference for how to find index for max and min
    # print(month_name_difference[max_index])
    # create variable of min monthly change month
    min_index = monthly_change.index(min(monthly_change))
    # print(month_name_difference[min_index])

    # print(month_name_difference)
    
    analysis = {
        "Months": row_count,
        "Total": total_profit_loss,
        "Average": round(avg_change, 2),
        "Increase": max(monthly_change),
        "High": month_name_difference[max_index],
        "Decrease": min(monthly_change),
        "Low": month_name_difference[min_index]}
    
    # print(f"Total Months: {analysis["Months"]}") print from dictionary
    
    # Store each of these in a dictionary and then call the dictionary to print to terminal and write to file
    print(f"Total Months: {row_count}")
    print(f"Total: ${total_profit_loss}")
    # print(monthly_change)
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {month_name_difference[max_index]} (${max(monthly_change)})") # confirm this is correct
    print(f"Greatest Decrease in Profits: {month_name_difference[min_index]} (${min(monthly_change)})") # confirm this is correct  

# write to file

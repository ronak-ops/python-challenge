import csv
import os

csvpath=os.path.join('/Users/ronnie/Downloads','Pybank','budget_data.csv')

total_amount=0.00
count = 0
average_change = 0.00
first_amount = 0.00
last_amount = 0.00
high_low = {}
diff_amount = 0.00

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
    if csv.Sniffer().has_header:
            next(csvreader)

    for row in csvreader:
        if count == 0:
            first_amount = float(row[1])
            diff_amount = first_amount
        total_amount += float(row[1]) 
        last_amount = float(row[1]) 
        if count > 0:
            diff_amount = last_amount-diff_amount
            high_low.update({row[0]:diff_amount})
            diff_amount = last_amount
        count += 1   
        

    average_change = (last_amount-first_amount)/(count-1)
    key, value = max(high_low.items(), key=lambda x:x[1])
    key_1, value_1 = min(high_low.items(), key=lambda x:x[1])

file1 = open("py_bank.txt","w")
file1.write("Financial Analysis \n")
file1.write("---------------------------- \n")
file1.write("Total Months {0} \n".format(count))
file1.write("Total : ${0} \n".format(total_amount))
file1.write("Average Change: ${0:.2f} \n".format(average_change))
file1.write("Greatest Increase in Profits: {0} (${1}) \n".format(key,value))
file1.write("Greatest Decrease in Profits: {0} (${1}) \n".format(key_1,value_1))
file1.close()

print("Financial Analysis")
print("----------------------------")
print("Total Months {0}".format(count))
print("Total : ${0}".format(total_amount))  
print("Average Change: ${0:.2f}".format(average_change))
print("Greatest Increase in Profits: {0} (${1})".format(key,value))
print("Greatest Decrease in Profits: {0} (${1})".format(key_1,value_1))


          
# Dependencies
import csv
import os

budget_data=os.path.join("budget_data.csv")

# Open and read csv
with open(budget_data) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  #skip the header
  header= next(csvreader)

  #Define the variables and lists
  line_ct=0
  total_ct= 0
  prev = 0
  revchg = []
  skip = []
  finalmax = 0
  finalmin = 9999999
  revchglist = []
# Loop through data
  for row in csvreader:
      #get the line count
      line_ct = line_ct + 1
      #get the total count
      total_ct = (int(row[1])) + total_ct
      #Calculate the revenue change between current and next month
      revchg = int(row[1]) - prev
      prev = int(row[1])
      #Conditional to find the max row and date
      if revchg > finalmax:
          finalmax = revchg
          finaldate = row[0]
      #Conditional to find the min row and data
      if revchg < finalmin:
          finalmin = revchg
          finaldate2 = row[0]
      #Hold the values of the change in the list
      revchglist.append(revchg)
#Calculate the average of the revenue change
newvar = revchglist[1:]
avglist = sum(newvar)/len(newvar) 
avg_str= '${0:,.2f}'.format(avglist)
#Print the output

print ("Financial Analysis")
print('-' * 35)
print("Total Months: " + str(line_ct))
print("Total: $" + str(total_ct))
print("Average Change: " + avg_str)
print("Greatest Increase in Profits: " + (finaldate) + ", " + "($" + str(finalmax) + ")")
print("Greatest Decrease in Profits: " + (finaldate2) + ", " + "($" + str(finalmin) + ")")

# Specify the file to write to
output_path = os.path.join("banknew.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
  csvfile.write("Financial Analysis" +'\n')
  csvfile.write('-' * 35 + '\n')
  csvfile.write("Total Months: " + str(line_ct)+ '\n')
  csvfile.write("Total: $" + str(total_ct) + '\n')
  csvfile.write("Average Change: " + avg_str +'\n')
  csvfile.write("Greatest Increase in Profits: " + (finaldate) + ", " + "($" + str(finalmax) + ")" + '\n')
  csvfile.write("Greatest Decrease in Profits: " + (finaldate2) + ", " + "($" + str(finalmin) + ")"+ '\n')



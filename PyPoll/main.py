# Import dependencies
import csv
import os

# Assign file location with the csv library
poll_data=os.path.join("election_data.csv")

with open(poll_data) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   #skip the header
   header= next(csvreader)

   #Declare Variables
   total_vt = 0
   khan_vt = 0
   correy_vt = 0
   li_vt = 0
   otooley_vt = 0




   for row in csvreader:

       # Count the unique Voter ID's and store in variable  called total_votes
       total_vt +=1
       if row[2] == "Khan":
           khan_vt+=1
       elif row[2] == "Correy":
           correy_vt +=1
       elif row[2] == "Li":
           li_vt +=1
       elif row[2] == "O'Tooley":
           otooley_vt +=1

   khan_perc = (int(khan_vt/total_vt) * 100)
   corr_perc = (int(correy_vt/total_vt) * 100)
   otool_perc = (int(otooley_vt/total_vt) * 100)

print("Election Results")
print("Total Votes:" + str(total_vt))
print("Khan:" + str(khan_vt) + khan_perc) + "%" )
print("Correy:" + (correy_vt) + (corr_perc) + "%")
print("O'Tooley:" + (otooley_vt) + (otool_perc) + "%")
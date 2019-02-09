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
winner= {'Khan':khan_vt,'Correy':correy_vt,'Li':li_vt,'O\'Tooley':otooley_vt}
khan_perc = (khan_vt/total_vt) * 100
corr_perc = (correy_vt/total_vt) * 100
li_perc= (li_vt/total_vt) * 100
otool_perc = (otooley_vt/total_vt) * 100
khan_dis = '{0:.3f}'.format(khan_perc)
correy_dis="{0:.3f}" .format(corr_perc)
li_dis= '{0:.3f}' .format(li_perc)
otool_dis= '{0:.3f}' .format(otool_perc)
key_max=max(winner.keys(),key=(lambda k: winner[k]))
print("Election Results")
print("Total Votes:" + str(total_vt))
print("Khan: " + str(khan_vt)+" " + khan_dis + "%" )
print("Correy: " + str(correy_vt)+" " + correy_dis + "%")
print("Li: " + str(li_vt) + " " + li_dis + "%")
print("O'Tooley: " + str(otooley_vt)+ " " + otool_dis + "%")
print("winner: " + key_max)
# Specify the file to write to
output_path = os.path.join("pollnew.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
    csvfile.write("Election Results\n")
    csvfile.write("Total Votes:" + str(total_vt)+ "\n")
    csvfile.write("Khan: " + str(khan_vt)+" " + khan_dis + "%\n")
    csvfile.write("Correy: " + str(correy_vt)+" " + correy_dis + "%\n")
    csvfile.write("Li: " + str(li_vt) + " " + li_dis + "%\n")
    csvfile.write("O'Tooley: " + str(otooley_vt)+ " " + otool_dis + "%\n")
    csvfile.write('winner: ' + key_max + '\n')


   
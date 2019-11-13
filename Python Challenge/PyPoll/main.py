import csv
import os

csvpath=os.path.join('/Users/ronnie/Downloads','PyPoll','election_data.csv')

total_votes = 0
vote_khan = 0
khan_per = 0.000
vote_correy = 0
correy_per = 0.000
vote_li = 0
li_per = 0.000
vote_tooley = 0
tooley_per = 0.000
vote_dict = {}

with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
      
        if row[2] == "Khan":
          vote_khan +=1
    
        if row[2] == "Correy":
            vote_correy +=1

        if row[2] == "Li":
             vote_li +=1

        if row[2] == "O'Tooley":
             vote_tooley +=1


total_votes =  vote_khan + vote_correy + vote_li + vote_tooley
khan_per = (vote_khan/total_votes)*100
correy_per = (vote_correy/total_votes)*100
li_per = (vote_li/total_votes)*100
tooley_per = (vote_tooley/total_votes)*100

vote_dict.update({"Khan":khan_per, "Correy":correy_per, "Li":li_per,"O'Tooley":tooley_per})

winner_key,winner_value = max(vote_dict.items(), key=lambda x:x[1])

# Write to file:

file1 = open("py_poll.txt","w")
file1.write("Election Results \n")
file1.write("------------------------- \n")
file1.write("Total Votes: {0} \n".format(total_votes) )
file1.write("------------------------- \n")
file1.write("Khan: {0:.3f}% ({1}) \n".format(khan_per,vote_khan))
file1.write("Correy: {0:.3f}% ({1}) \n".format(correy_per,vote_correy))
file1.write("Li: {0:.3f}% ({1}) \n".format(li_per,vote_li))
file1.write("O'Tooley: {0:.3f}% ({1}) \n".format(tooley_per,vote_tooley))
file1.write("------------------------- \n")
file1.write("Winner: {} \n".format(winner_key))
file1.write("-------------------------")
file1.close

#Print output to console:

print("Election Results")
print("-------------------------")
print("Total Votes: {0}".format(total_votes))
print("-------------------------")
print("Khan: {0:.3f}% ({1})".format(khan_per,vote_khan))
print("Correy: {0:.3f}% ({1})".format(correy_per,vote_correy))
print("Li: {0:.3f}% ({1})".format(li_per,vote_li))
print("O'Tooley: {0:.3f}% ({1})".format(tooley_per,vote_tooley))
print("-------------------------")
print("Winner: {}".format(winner_key))
print("-------------------------")


import os 
import csv
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile)
    csvheader=next(csvreader)

    # find total votes 
    csvlist=list(csvreader)
    total_votes=len(csvlist)
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

# print out candidates' voting information 
def candidate_info (candidate_name): 
 total_cast=0 
 for row in csvlist:
  if row[2] == candidate_name: 
   total_cast = total_cast+1
   cast_percent=round((total_cast/total_votes)*100,3)
   candidate_voting=f'{candidate_name}: {cast_percent}% ({total_cast})'
 print(candidate_voting)
candidate_info ("Charles Casper Stockham")
candidate_info ("Diana DeGette")
candidate_info ("Raymon Anthony Doane")
print('-------------------------')
# find the winner 
list2=[]
for row in csvlist:
 list2.append(row[2])
 # count winner votes 
c_voter=list2.count("Charles Casper Stockham")
d_voter=list2.count("Diana DeGette")
r_voter=list2.count("Raymon Anthony Doane")
comapre=[c_voter,d_voter,r_voter]
if max(comapre)== c_voter:
   print("Winner: Charles Casper Stockham")
elif max(comapre) == d_voter:
   print("Winner: Diana DeGette")
else:
   print("Raymon Anthony Doane")
print('-------------------------')
  
   

    

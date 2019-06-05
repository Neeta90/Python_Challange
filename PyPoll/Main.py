import os
import csv
#import numpy as np 
#from collections import defaultdict
#uniques = defaultdict(int)
PyPoll = "election_data.csv"
total_votes = 0
#candidate_name = []
Candidatename = []
votes = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(PyPoll, newline="", encoding="utf-8")as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile)
   #print(f"Header: {csv_header}")
   for row in csvreader:
     # Totalvotes.append(row[0])
      total_votes = total_votes+1
      name =row[2]
      if name not in Candidatename:
         Candidatename.append(name)
         print(name)

   for cname in Candidatename:
      csvfile.seek(0,os.SEEK_SET)

      poll_header = next(csvfile)

      for cntvote in csvreader:
         if cname == cntvote[2]
            cvotes = cvotes+1
      votes 
      print(cvotes)

 


print ("Election Results")
print("-------------------------------------")
#print(f"Total votes: {len(Total_votes)}")
print(total_votes)
print("-------------------------------------")

#print(candidate_name)
   
#print(Candidate_name, sep = ":\n")
#print(f"Candidatename[0]: {len(votes)}")

#print(f"Total votes: {len(votes)}")
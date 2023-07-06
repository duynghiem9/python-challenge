# import libraries
import os
import csv

def percentage(total, num_list):
    percent_num = 0
    new_list = []
    # loop through list
    for i in num_list:
        # calculate percent
        percent_num = (i/total)*100
        percent_num = round(percent_num, 3)
        new_list.append(percent_num)
    return new_list

def maximum(num_list):
     num = num_list[0]

     for i in num_list:
         if i > num:
              num = i
     return num

# csv path
csv_path = os.path.join("Resources", "election_data.csv")

# set variables

# since candidates and count aren't defined, the data should be stored in arrays
candidate_list = []
votes_count_list = []
vote_percent_list = []

candidate_index = 0
total_votes = 0
winning_votes = 0
winning_index = 0
winning_candidate = ""

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header
    csv_header = next(csvreader)

    # loop starting at row 1, not 0
    for row in csvreader:
        # add to vote counter
        total_votes += 1

        # create if statement to determine if I need to add candidates into candidate_list
        if row[2] not in candidate_list:
            # add candidate into candidate list
            candidate_list.append(row[2])
            # add new index in vote_count_list and set to 1
            votes_count_list.append(1)
        # if the name is in candidate_list
        else:
            # find index of candidate
            candidate_index = candidate_list.index(row[2])
            # add to vote_count_list to respective index
            votes_count_list[candidate_index] += 1
    # figure out Vote Percentage
    vote_percent_list = percentage(total_votes, votes_count_list)

    # figure out popular vote
    winning_votes = maximum(votes_count_list)
    # finding index
    winning_index = votes_count_list.index(winning_votes)
    # find winning name using winning index
    winning_candidate = candidate_list[winning_index]

    # printing
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------\n")
    
    # loop for candidate stats
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {vote_percent_list[i]}% ({votes_count_list[i]})\n")
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------\n")

    # start outputting
    # output path
    output_path = os.path.join("output", "output.txt")
    # open output file
    output_txt = open(output_path, "w")

    # break input into separate pieces, part 1 and part 3
    output_p1 = ["Election Results\n",
                 "-------------------------\n",
                 f"Total Votes: {total_votes}\n"
                 "-------------------------\n"]
    output_p3 = ["-------------------------\n",
                 f"Winner: {winning_candidate}\n",
                 "-------------------------\n"]
    # start writing
    # part 1
    output_txt.writelines(output_p1)

    # part 2: loop through and write individually
    for i in range(len(candidate_list)):
        output_txt.write(f"{candidate_list[i]}: {vote_percent_list[i]}% ({votes_count_list[i]})\n")
    
    # part 3
    output_txt.writelines(output_p3)

    # close
    output_txt.close
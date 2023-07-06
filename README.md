python-challenge

PyBank to do list:
-    The total number of months included in the dataset

-    The net total amount of "Profit/Losses" over the entire period

-   The changes in "Profit/Losses" over the entire period, and then the average of those changes
 
-    The greatest increase in profits (date and amount) over the entire period

-    The greatest decrease in profits (date and amount) over the entire period

pseudo-code:

	-set variables
		-month counter
		-current cell variable
		-profits/loss
	-lists
		-date_list
		-profit list
	
	-set initial variables (first row that is not header):
	
	-loop through file
		-add date
		-calculate and add profit change
		-change current cell
		-month counter
		-total profit
	
	-get max change
	-get index
	-get month using index
	
	-get min change
	-get index
	-get month using index
	
	-print everything
	
	-export everything to txt file

PyPoll to do list:


-    The total number of votes cast

-    A complete list of candidates who received votes

-    The percentage of votes each candidate won

-    The total number of votes each candidate won

-    The winner of the election based on popular vote

pseudo-code:

 	-set variables (need to have arrays for candidates and votes
 	-loop through sheet
 		-add to vote counter for total
 		-check if something is not in the candidate list
			-add candidate to candidate list
			-add the vote count on the same index
 		-if it is on there
			-get the index using name
			-add to vote count using index
	
 	-vote percentage:
		-make function
			-parameters (total votes, vote_count_list)
			-make a new list
			-loop through vote_count_list
				-calculate percentage
				-format the percentage
				-add it to new list
			-return new list
	
 	-winning candidate:
		-maximum of votes in vote_count_list
		-find index with the maximum
		-look for candidates using same index
	
 	-print everything	
  		-use loop to do candidates in fstring
 	-export everything	
  		-use loop to do candidates in fstring


   

Resources:
https://stackoverflow.com/questions/17513438/csvreader-next-function

https://www.geeksforgeeks.org/writing-to-file-in-python/#

https://stackoverflow.com/questions/70189722/start-loop-from-certain-number-to-n-number-in-python

https://stackoverflow.com/questions/14448692/how-to-find-the-maximum-number-in-a-list-using-a-loop

https://stackoverflow.com/questions/21359883/python-find-the-minimum-using-for-loops

https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/

https://stackoverflow.com/questions/11888525/how-to-export-a-file-into-a-different-directory-using-python

https://stackoverflow.com/questions/56410671/converting-from-float-to-percentage

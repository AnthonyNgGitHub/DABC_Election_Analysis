# The data we need to retrieve

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# 2. Declare a new list for candidates.
candidate_options =[]

# 3. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #4. Add to the total vote count.
        total_votes += 1

        #5. Print the candidate name from each row
        candidate_name = row[2]

        #6. If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #7. Add candidate_name to the candidate_options list using append()
            candidate_options.append(candidate_name)

            #8. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #9. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#10. Save the results to our text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the election results to our text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 7. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 8. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 9. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.

        # Determine winning vote count and candidate

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        #  To do: print out the winning candidate, vote count and percentage to terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the candidate results to our text file.
    txt_file.write(winning_candidate_summary)
    


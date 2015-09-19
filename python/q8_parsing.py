#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import pandas as pd

def read_data(data):
    return pd.read_csv(data)

def get_min_score_difference(parsed_data):
    """
    """
    differences = parsed_data.Points - parsed_data['Goals Allowed']
    return min(abs(differences))

def get_team(parsed_data):
    """Returns the team with the minimum score difference. 
    """
    parsed_data['differences'] = parsed_data.Points - parsed_data['Goals Allowed']
    
    # .values[0] necessary to return a pure string rather than the array or dataframe
    return parsed_data[parsed_data.differences == index_value].Team.values[0]
    
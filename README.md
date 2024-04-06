# WorldCup23_Mentorness


This Python code utilizes the pandas, matplotlib, and seaborn libraries for data manipulation, visualization, and exploration of the World Cup 2023 cricket data (assuming the data is stored in a CSV file named "CWC23_all_innings.csv").

1. **Data Loading and Exploration **
   - Imports the necessary libraries: pandas (`pd`), matplotlib (`plt`), and seaborn (`sns`).
   - Reads the CSV data into a Pandas DataFrame named `data`.
   - Prints the first few rows (`data.head()`) and basic information about the data (`data.info()`) to understand the data structure and content.
  
   - ![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/c3019f1a-a413-407b-bb45-056b2dd7b9ea)


2. **Team Performance Analysis Function :**
   - Defines a function `calculate_team_performance(data)` that calculates various team performance metrics.
     - Groups data by team (`groupby("team")`) to analyze performance for each team.
     - Calculates the number of matches played by each team (`team_matches`).
     - Iterates through unique teams (`for team in data["team"].unique()`).
     - Filters data for the current team (`team_data = data[data["team"] == team]`).
     - Calculates team-specific metrics like total runs scored and wickets taken for batting and bowling, respectively.
     - Calculates additional metrics (batting average, bowling average, etc.) with error handling to avoid division by zero.
   - Calls the `calculate_team_performance` function with a copy of the data (`data.copy()`) to avoid modifying the original data and stores the results in a DataFrame named `team_performance_df`.
  
   -![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/1fba4a67-3e80-4eb6-8ce5-c385d67191cf)
    
   


4. **Team Performance Analysis and Visualization :**
   - Prints a summary of the team performance (`print("Team Performance Summary:")`).
   - Displays the `team_performance_df` DataFrame containing various team metrics.
   - Creates a bar chart to visualize runs scored vs wickets taken for each team (`team_performance_df.plot(kind="bar", x="team", y=["runs", "wkts"])`).
   - Sorts teams by most runs scored (descending order) and displays the top 5 teams (`top_run_scorers_df`).
   - Sorts teams by fewest wickets lost (ascending order) and displays the top teams (`least_wickets_lost_df`).
   - Extracts team names and runs/wickets data for the top run scorers and least wickets lost teams.
   - Creates separate bar charts to visualize top teams by runs scored and fewest wickets lost.
    ![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/a3ac7d80-a286-4c2c-b1a4-1eb4f6a3d06b)
    ![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/40924c09-e2a9-4544-92bb-08e6730ebaa8)
5. **Player Performance Analysis (lines 123-239):**
   - Filters data for batters (`batting_df = data[data['bat_or_bowl'] == 'bat']`) and bowlers (`bowling_df = data[data['bat_or_bowl'] == 'bowl']`).
   - Calculates batting statistics (`batting_stats`) like total runs, average strike rate, and number of not outs grouped by player.
   - Calculates bowling statistics (`bowling_stats`) like total wickets taken and average economy rate grouped by player.
   - Creates a subtitled figure to visualize top run-scorers and wicket-takers using Seaborn (`sns.barplot`).
   - Merges batting and bowling statistics for each player into a single DataFrame (`player_stats`) using pandas merge.
   - Calculates a new metric, "overall impact", by summing runs and wickets for each player.
   - Sorts players by overall impact (descending order) and displays the top 10 most impactful players (`top_impact_players`).
   - Creates a bar chart to visualize the top impact players using Seaborn.
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/0e19c7f9-d36e-491e-ad20-0991a234078b)
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/73d4dcd5-ecca-41a2-97e2-c2ca6faa77a8)


6. **Opposition and Ground Analysis :**
   - Groups data by team and opposition (`groupby(['team', 'opposition'])`) to analyze performance against different opponents.
   - Calculates win percentage (`win_pct`) based on the assumption that "not_out" indicates a win for a team.
   - Provides an example loop to iterate through unique teams (`unique_teams`) and print the win percentage against each opponent for a specific team (`selected_team`). You can modify this loop to iterate through all teams.
   - Creates a bar chart to visualize the win percentage for a chosen team against each opponent.
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/2dd60902-5828-4bab-8f7d-6acaa52dc909)
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/557f375c-f334-401a-851c-c616c5b43553)
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/1d5c8e5d-ada7-484a-a430-e6938b72b7f5)
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/7337307e-a252-4509-8a08-d5f6aaec5da0)
![image](https://github.com/shehababdo/WorldCup23_Mentorness/assets/92190446/75300e00-2ec9-44f7-8b39-0961dd41378a)

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv("E:\Mentorness Internship\world cup\CWC23_all_innings.csv")
data.info()
data.head()


def calculate_team_performance(data):
  """
  Calculates team performance metrics with filtering by bat_or_bowl.

  Args:
      data: Pandas DataFrame containing match data.

  Returns:
      Pandas DataFrame with team performance statistics.
  """

  # Count matches played by each team
  team_matches = data.groupby("team").size().to_frame(name="matches")

  # Initialize empty dictionary to store team performance data
  team_performance = {}

  # Iterate through unique teams
  for team in data["team"].unique():
    team_data = data[data["team"] == team]
    team_performance[team] = {
        "team": team,
        "runs": team_data[team_data["bat_or_bowl"] == "bat"]["runs"].sum(),
        "wkts": team_data[team_data["bat_or_bowl"] == "bowl"]["wkts"].sum(),
        "bb_bf": team_data["bb_bf"].sum(),
        "matches": team_matches.loc[team]["matches"]  # Access matches from team_matches
    }

  # Calculate remaining metrics with error handling
  for team, stats in team_performance.items():
    stats["balls_faced"] = stats["bb_bf"] if stats["bb_bf"] > 0 and stats["runs"] > 0 else 0
    stats["balls_bowled"] = stats["bb_bf"] if stats["bb_bf"] > 0 and stats["wkts"] > 0 else 0
    stats["batting_avg"] = stats["runs"] / stats["matches"] if stats["matches"] > 0 else 0
    stats["bowling_avg"] = stats["wkts"] / stats["matches"] if stats["matches"] > 0 else 0
    stats["balls_faced_per_match"] = stats["balls_faced"] / stats["matches"] if stats["matches"] > 0 else 0
    stats["economy_rate"] = stats["balls_bowled"] * 6 / stats["runs"] if stats["runs"] > 0 else 0


    if stats["balls_faced"] > 0:
      stats["strike_rate"] = (stats["runs"] / stats["balls_faced"]) * 100

  # Convert team_performance dictionary to DataFrame
  
  team_performance_df = pd.DataFrame.from_dict(team_performance, orient="index")
  return team_performance_df

# Get team performance data
team_performance_df = calculate_team_performance(data.copy())  # Copy data to avoid modifying original

# Print and visualize team performance
print("Team Performance Summary:")
print(team_performance_df)


team_performance_df.plot(kind="bar", x="team", y=["runs", "wkts"])
plt.title("Team Performance - Runs vs Wickets")
plt.ylabel("Runs/Wickets")
plt.show()


# Sort by most runs scored (descending order)
top_run_scorers_df = team_performance_df.sort_values(by="runs", ascending=False)

# Sort by fewest wickets lost (ascending order)
least_wickets_lost_df = team_performance_df.sort_values(by="wkts", ascending=True)

# Print results (example for top run scorers)
print("Top Teams by Runs Scored:")
print(top_run_scorers_df.head(5))  # Display top 5 teams


# Extract team names and runs scored from the sorted DataFrame
teams = top_run_scorers_df["team"].to_list()
runs_scored = top_run_scorers_df["runs"].to_list()

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(teams, runs_scored)
plt.xlabel("Teams")
plt.ylabel("Runs Scored")
plt.title("Top Teams by Runs Scored (Bar Chart)")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
plt.grid(axis='y')  # Add gridlines for better readability
plt.tight_layout()
plt.show()


# Extract team names and wickets lost from the sorted DataFrame
teams = least_wickets_lost_df["team"].to_list()
wickets_lost = least_wickets_lost_df["wkts"].to_list()

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(teams, wickets_lost)
plt.xlabel("Teams")
plt.ylabel("Wickets Lost")
plt.title("Teams with Fewest Wickets Lost (Bar Chart)")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability
plt.grid(axis='y')  # Add gridlines for better readability
plt.tight_layout()
plt.show()


# Filter data for batting and bowling separately
batting_df = data[data['bat_or_bowl'] == 'bat']
bowling_df = data[data['bat_or_bowl'] == 'bowl']

# Calculate batting statistics
batting_stats = batting_df.groupby('player').agg({
    'runs': 'sum',
    'sr': 'mean',  # Strike rate
    'not_out': 'sum'
}).reset_index()

# Calculate bowling statistics
bowling_stats = bowling_df.groupby('player').agg({
    'wkts': 'sum',
    'econ': 'mean'  # Economy rate
}).reset_index()

# Visualize top run-scorers and wicket-takers
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
sns.barplot(x='runs', y='player', data=batting_stats.nlargest(10, 'runs'), palette='viridis')
plt.title('Top Run-Scorers in World Cup 2023')

plt.subplot(2, 1, 2)
sns.barplot(x='wkts', y='player', data=bowling_stats.nlargest(10, 'wkts'), palette='coolwarm')
plt.title('Top Wicket-Takers in World Cup 2023')

plt.tight_layout()
plt.show()


# Combine batting and bowling statistics for each player
player_stats = pd.merge(batting_stats, bowling_stats, on='player', how='outer')

# Calculate overall impact (runs + wickets)
player_stats['overall_impact'] = player_stats['runs'] + player_stats['wkts']

# Sort players by overall impact (descending order)
top_impact_players = player_stats.sort_values(by='overall_impact', ascending=False)

# Print top impact players
print("Top Impact Players:")
print(top_impact_players.head(10))  # Display top 10 players
top_eltop=top_impact_players.head(10)
# Visualize impact players
plt.figure(figsize=(10, 6))
sns.barplot(x='overall_impact', y='player', data=top_impact_players.nlargest(10, 'overall_impact'), palette='coolwarm')
plt.title('Top Impact Players in World Cup 2023')
plt.xlabel('Overall Impact')
plt.ylabel('Player')
plt.tight_layout()
plt.show()


# Group data by team and opposition
opposition_performances = data.groupby(['team', 'opposition'])[['runs', 'wkts', 'not_out']].mean()

# Calculate win percentage (assuming 'not_out' indicates a win)
opposition_performances['win_pct'] = opposition_performances['not_out']

# Example: Print win percentage vs. each opponent for Team A
unique_teams = team_performance_df['team'].unique()

# Loop through each team
for team in unique_teams:

  selected_team = team
  team_opp_win_pct = opposition_performances.loc[selected_team, 'win_pct']

  plt.figure(figsize=(10, 6))  # Adjust figure size as needed
  plt.bar(team_opp_win_pct.index, team_opp_win_pct.values)
  plt.xlabel("Opposition")
  plt.ylabel("Win Percentage")
  plt.title(f"Win Percentage vs. Each Opposition ({selected_team})")
  plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
  plt.tight_layout()
  plt.show()



print(data.columns)
data['ground'].dtypes
print(data['opposition'].dtypes)


# Identify players who consistently perform well (modify as needed)
for name in top_eltop :
    player_name = name
    player_data = data[data['player'] == player_name]

    # Average runs scored by player against each opponent
    player_opp_avg_runs = player_data.groupby('opposition')['runs'].mean()
    print(f"\n{name} - Average Runs Scored vs. Each Opposition:")
    print(player_opp_avg_runs)

    # Explore player performance variations across grounds (modify as needed)
    player_ground_performance = player_data.groupby('ground')[['runs', 'wkts']].mean()
    print(f"\n{name} - Average Performance by Ground:")
    print(player_ground_performance)

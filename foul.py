import csv
import matplotlib.pyplot as plt


"""
Generates Types of Outcomes or Start Types of Plays
"""


def generateTypeChart(data_analyze):
    for row in data_analyze:
        if data_analyze.index(row) != 0:
            narrowed.append(row)

    types = [entry[9] for entry in narrowed]
    type_counts = {}

    for category in types:
        type_counts[category] = type_counts.get(category, 0) + 1

    # Extract the start types and their corresponding counts

    type_labels = list(type_counts.keys())
    type_values = list(type_counts.values())

    # Create a bar chart
    plt.bar(type_labels, type_values)

    # Add labels and a title
    plt.xlabel("Start Type")
    plt.ylabel("Count")
    plt.title("Count of Start Types")

    # Display the chart
    plt.show()


def generateWinsChart(csv_reader, off_wins, def_wins):
    labels = ["Defensive Team Wins", "Offensive Team Wins"]
    wins = [def_wins, off_wins]

    plt.bar(labels, wins)
    plt.xlabel("Game Outcomes")
    plt.ylabel("Number of Games")
    plt.title("Defensive Team vs. Offensive Team Wins")
    plt.show()


if __name__ == "__main__":
    off_win_data = []
    def_win_data = []
    narrowed = []

    off_wins = 0
    def_wins = 0

    # Open the CSV file for reading
    with open("chances.csv", "r") as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            if row[5] != row[-1]:
                off_win_data.append(row)
                off_wins += 1
            # Each row is a list of values
            else:
                def_win_data.append(row)
                def_wins += 1

    generateWinsChart(csv_reader, off_wins, def_wins)
    generateTypeChart(off_win_data)
    generateTypeChart(def_win_data)

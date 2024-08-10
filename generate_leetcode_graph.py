import requests
import matplotlib.pyplot as plt

# Function to fetch LeetCode stats
def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    return response.json()

# Generate a graph from LeetCode stats
def generate_graph(data):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    problems_solved = data['recent_problems_solved']

    plt.figure(figsize=(10, 5))
    plt.plot(days, problems_solved, marker='o')
    plt.title('LeetCode Progress Over the Week')
    plt.xlabel('Day')
    plt.ylabel('Problems Solved')
    plt.grid(True)
    plt.savefig('leetcode_progress.png')

# Replace with your LeetCode username
username = "Naveed"
data = fetch_leetcode_stats(username)
generate_graph(data)

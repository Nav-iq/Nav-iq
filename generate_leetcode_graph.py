import os
import requests
import matplotlib.pyplot as plt

# Function to fetch LeetCode stats
def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Generate a graph from LeetCode stats
def generate_graph(data):
    if data is None:
        print("No data to generate graph.")
        return

    # Ensure the images directory exists
    if not os.path.exists('images'):
        os.makedirs('images')

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    problems_solved = data.get('recent_problems_solved', [0]*7)

    plt.figure(figsize=(10, 5))
    plt.plot(days, problems_solved, marker='o')
    plt.title('LeetCode Progress Over the Week')
    plt.xlabel('Day')
    plt.ylabel('Problems Solved')
    plt.grid(True)
    plt.savefig('leetcode_progress.png')
    plt.close()

# Replace with your LeetCode username
username = "NaveedIqbal"
data = fetch_leetcode_stats(username)
generate_graph(data)

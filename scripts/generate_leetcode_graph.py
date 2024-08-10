import requests
import matplotlib.pyplot as plt

def fetch_problems_solved(username):
    url = f"https://leetcode.com/u/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 403:
        print("403 Forbidden: Access Denied")
        return None
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return None
    
    # Placeholder for actual scraping logic
    problems_solved = [5, 3, 4, 2, 7, 6, 5]  # Example static data

    return problems_solved

def generate_graph(problems_solved):
    if not problems_solved:
        print("No valid data to generate graph.")
        return
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    plt.figure(figsize=(10, 5))
    plt.plot(days, problems_solved, marker='o')
    plt.title('LeetCode Progress Over the Week')
    plt.xlabel('Day')
    plt.ylabel('Problems Solved')
    plt.grid(True)
    plt.savefig('images/leetcode_progress.png')
    plt.close()

username = "NaveedIqbal"
problems_solved = fetch_problems_solved(username)
generate_graph(problems_solved)

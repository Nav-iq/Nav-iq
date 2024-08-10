import requests

leetcode_username = "your_leetcode_username"
url = f"https://leetcode-stats-api.herokuapp.com/{leetcode_username}"

response = requests.get(url)
data = response.json()

with open('README.md', 'w') as f:
    f.write(f"# LeetCode Stats\n\n")
    f.write(f"- **Total Solved:** {data['totalSolved']}\n")
    f.write(f"- **Easy:** {data['easySolved']} / {data['totalEasy']}\n")
    f.write(f"- **Medium:** {data['mediumSolved']} / {data['totalMedium']}\n")
    f.write(f"- **Hard:** {data['hardSolved']} / {data['totalHard']}\n")

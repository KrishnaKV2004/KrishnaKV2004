import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# GitHub repo details
OWNER = "your-username"  # Replace with your GitHub username
REPO = "your-repo"       # Replace with your repository name
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

# Fetch data from GitHub API
def fetch_github_data():
    headers = {"Accept": "application/vnd.github.v3+json"}
    stats = {}

    # Fetch stars
    stars = requests.get(API_URL).json().get("stargazers_count", 0)
    stats["Stars"] = stars

    # Fetch contributors
    contributors = requests.get(f"{API_URL}/contributors").json()
    stats["Contributors"] = len(contributors)

    # Fetch PRs and Issues
    prs = requests.get(f"{API_URL}/pulls").json()
    issues = requests.get(f"{API_URL}/issues").json()
    stats["PRs"] = len(prs)
    stats["Issues"] = len(issues)

    return stats

# Generate Activity Chart
def generate_activity_chart(stats):
    plt.figure(figsize=(10, 6))
    categories = list(stats.keys())
    values = list(stats.values())
    plt.bar(categories, values, color=['red', 'orange', 'yellow', 'blue'])
    plt.title("Last 28 Days Stats")
    plt.savefig("activity_chart.png")

if __name__ == "__main__":
    stats = fetch_github_data()
    generate_activity_chart(stats)

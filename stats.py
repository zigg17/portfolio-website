from datetime import datetime
from dateutil.relativedelta import relativedelta
from github import Github

# Function to calculate age in years, months, and days
def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    current_date = datetime.now()
    age_difference = relativedelta(current_date, birth_date)
    return age_difference.years, age_difference.months, age_difference.days

# Function to fetch stats from GitHub
def fetch_github_stats(github_token):
    g = Github(github_token)
    user = g.get_user()

    # Get the number of repositories
    repositories = user.get_repos().totalCount

    # Initialize counters
    commits = 0
    lines_written = 0  # This would typically require additional work
    pull_requests = 0

    # Loop through repositories
    for repo in user.get_repos():
        commits += repo.get_commits().totalCount
        pull_requests += repo.get_pulls().totalCount
        
        # Example of how you might count lines of code (not supported directly by GitHub API)
        # You'd typically need to clone the repo and count the lines using a script.

    # Return the fetched data
    return repositories, commits, lines_written, pull_requests

# Function to update the stats file
def update_stats_file(file_path, birth_date, repositories, commits, lines_written, pull_requests, programming_languages, natural_languages):
    years, months, days = calculate_age(birth_date)
    
    # Prepare the content
    content = f"""
 __   __  _  _____   ___ _ ___ __ _   ___ ___ 
|_ \ /  \| |/ / __| |_  | | __/ _] | | __| _ \
 _\ | /\ |   <| _|   / /| | _| [/\ |_| _|| v /
/___|_||_|_|\_\___| |___|_|___\__/___|___|_|_\

--------------------------------------------------
 Time in Existence: {years} years, {months} months, {days} days.
--------------------------------------------------
 Repositories: {repositories}
--------------------------------------------------
 Commits: {commits}
--------------------------------------------------
 Lines Written: {lines_written}
--------------------------------------------------
 Pull Requests: {pull_requests}
--------------------------------------------------
 Programming Languages: {', '.join(programming_languages)}
--------------------------------------------------
 Natural Languages: {', '.join(natural_languages)}
--------------------------------------------------
"""

    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
birth_date = "2000-05-16"
file_path = "ascii.txt"

# Your GitHub personal access token
github_token = "your_github_token_here"

# Fetch stats from GitHub
repositories, commits, lines_written, pull_requests = fetch_github_stats(github_token)

# Placeholder programming and natural languages
programming_languages = ["Python", "Shell"]
natural_languages = ["English", "Spanish"]

# Update the stats file
update_stats_file(file_path, birth_date, repositories, commits, lines_written, pull_requests, programming_languages, natural_languages)



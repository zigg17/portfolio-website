import os
import json
from github import Github, GithubException

def count_lines_in_notebook(file_content):
    lines = 0
    try:
        notebook_json = json.loads(file_content.decoded_content.decode('utf-8'))
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                lines += len(cell['source'])
    except Exception as e:
        print(f"Error processing notebook file: {e}")
    return lines

def count_lines_by_language(repo, languages, excluded_dirs=None, excluded_extensions=None, max_files=1000, max_depth=3):
    if excluded_dirs is None:
        excluded_dirs = ['venv', 'node_modules', '__pycache__']
    if excluded_extensions is None:
        excluded_extensions = ['.png', '.jpg', '.gif', '.zip', '.exe']

    lines_by_language = {lang: 0 for lang in languages}
    file_count = 0
    total_lines = 0

    try:
        contents = repo.get_contents("")
        while contents:
            if file_count >= max_files:
                print(f"Reached maximum file limit of {max_files} for repository '{repo.name}'.")
                break
            file_content = contents.pop(0)
            current_depth = file_content.path.count('/') 
            if current_depth > max_depth:
                print(f"Skipping {file_content.path} due to exceeding depth limit.")
                continue
            file_count += 1
            if file_content.type == "dir":
                if any(excluded_dir in file_content.path for excluded_dir in excluded_dirs):
                    print(f"Skipping directory: {file_content.path}")
                    continue  
                print(f"Entering directory: {file_content.path}")
                try:
                    contents.extend(repo.get_contents(file_content.path))
                except GithubException as e:
                    print(f"Error entering directory {file_content.path}: {e}")
                    continue
            else:
                file_extension = os.path.splitext(file_content.path)[1]
                if file_extension in excluded_extensions:
                    print(f"Skipping file with excluded extension: {file_content.path}")
                    continue  
                for lang, extensions in languages.items():
                    if file_extension in extensions:
                        try:
                            if file_extension == ".ipynb":
                                lines = count_lines_in_notebook(file_content)
                            else:
                                lines = len(file_content.decoded_content.decode('utf-8').splitlines())
                            lines_by_language[lang] += lines
                            total_lines += lines
                        except UnicodeDecodeError:
                            print(f"Skipping file due to encoding issues: {file_content.path}")
                        except Exception as e:
                            print(f"Error processing file {file_content.path}: {e}")
    except GithubException as e:
        print(f"Error counting lines in {repo.name}: {e}")
    
    for lang, lines in lines_by_language.items():
        print(f"Repository '{repo.name}' has {lines} lines of code in {lang}.")
    
    return lines_by_language, total_lines

def fetch_github_stats(github_token, languages, max_files_per_repo=1000, max_depth=3):
    g = Github(github_token)
    user = g.get_user()

    repositories = 0
    total_lines_of_code = 0
    total_commits = 0
    lines_by_language_total = {lang: 0 for lang in languages}

    for repo in user.get_repos():
        if not repo.fork:
            repositories += 1
            print(f"Processing repository {repositories}: '{repo.name}'...")
            total_commits += repo.get_commits().totalCount  # Count total commits
            repo_lines_by_language, repo_total_lines = count_lines_by_language(repo, languages, max_files=max_files_per_repo, max_depth=max_depth)
            total_lines_of_code += repo_total_lines
            for lang in languages:
                lines_by_language_total[lang] += repo_lines_by_language[lang]

    lines_by_language_total = dict(sorted(lines_by_language_total.items(), key=lambda item: item[1], reverse=True))

    return repositories, total_commits, total_lines_of_code, lines_by_language_total

def update_stats_file(file_path, repositories, total_commits, total_lines_of_code, lines_by_language_total):
    content = f"Total Repositories: {repositories}\n"
    content += f"Total Commits: {total_commits}\n"
    content += f"Total Lines Committed: {total_lines_of_code}\n"
    content += "Lines Committed by Language:\n"
    for lang, lines in lines_by_language_total.items():
        content += f" - {lang}: {lines} lines\n"
    
    with open(file_path, 'w') as file:
        file.write(content)

file_path = "ascii.txt"

github_token = os.getenv("GITHUB_TOKEN")

languages = {
    "Python": [".py"],
    "HTML": [".html", ".htm"],
    "Shell": [".sh"],
    "IPython": [".ipynb"],
    "C++": [".cpp", ".h", ".hpp"],
    "Markdown": [".md"] 
}

repositories, total_commits, total_lines_of_code, lines_by_language_total = fetch_github_stats(github_token, languages, max_files_per_repo=1000, max_depth=3)

update_stats_file(file_path, repositories, total_commits, total_lines_of_code, lines_by_language_total)

# This script uses the subprocess module to execute Git commands. The run_git_command function handles the execution of Git commands and prints the 
# output or errors. The script provides several functions to perform different actions in the version control system. For example, clone_repository 
# clones a repository from a given URL, create_branch creates a new branch, switch_branch switches to a specific branch, merge_branch merges changes 
# from a source branch, resolve_conflicts opens the configured merge tool to resolve conflicts, and generate_commit_history and generate_code_changes 
# generate reports on commit history and code changes, respectively.

import subprocess

# Function to execute Git commands
def run_git_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding="utf-8")
        output = result.stdout.strip()
        if output:
            print(output)
        error = result.stderr.strip()
        if error:
            print(error)
    except Exception as e:
        print(f"Error executing Git command: {str(e)}")

# Clone a repository
def clone_repository(repo_url, destination_dir):
    command = f"git clone {repo_url} {destination_dir}"
    run_git_command(command)

# Create a new branch
def create_branch(branch_name):
    command = f"git branch {branch_name}"
    run_git_command(command)

# Switch to a branch
def switch_branch(branch_name):
    command = f"git checkout {branch_name}"
    run_git_command(command)

# Merge changes from a branch
def merge_branch(source_branch):
    command = f"git merge {source_branch}"
    run_git_command(command)

# Resolve merge conflicts
def resolve_conflicts():
    command = "git mergetool"  # Opens the configured merge tool to resolve conflicts
    run_git_command(command)

# Generate a report on commit history
def generate_commit_history():
    command = "git log --oneline --graph"
    run_git_command(command)

# Generate a report on code changes
def generate_code_changes():
    command = "git diff"
    run_git_command(command)

# Example usage
repo_url = "https://github.com/example/repo.git"
destination_dir = "path/to/destination"
branch_name = "feature-branch"
source_branch = "development"

# Clone the repository
clone_repository(repo_url, destination_dir)

# Switch to the repository directory
os.chdir(destination_dir)

# Create a new branch
create_branch(branch_name)

# Switch to the new branch
switch_branch(branch_name)

# Make changes to the code

# Commit the changes

# Merge changes from the source branch
switch_branch(source_branch)
merge_branch(branch_name)

# Resolve conflicts if any
resolve_conflicts()

# Generate reports
generate_commit_history()
generate_code_changes()

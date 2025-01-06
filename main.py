import os
import random
import string
from datetime import datetime, timedelta  # Ensure this line is present and correct
import subprocess
import time

# GitHub repo details
REPO_PATH = r"C:\Users\ektho\Documents\Playgrounds\QuantumLeapForLunch"  # Change this to the path where your repo is cloned
REMOTE_URL = "git@github.com:CrazyCat556/QuantumLeapForLunch.git"  # Use SSH or HTTPS URL

def generate_random_content(length=100):
    """Generate random content for the file."""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

def make_random_changes(file_path):
    """Make random changes to the content of a file."""
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    # Ensure there's content to modify
    if not content:
        content = [generate_random_content()]
    
    # Modify existing content
    for _ in range(random.randint(1, 10)):  # Random number of changes
        line_index = random.randint(0, len(content) - 1)
        content[line_index] = generate_random_content() + '\n'
    
    # Add or remove lines
    if random.choice([True, False]):
        content.append(generate_random_content() + '\n')
    else:
        if len(content) > 1:
            content.pop(random.randint(0, len(content) - 1))
    
    with open(file_path, 'w') as file:
        file.writelines(content)

def generate_random_file():
    """Generate a new random file in the repository."""
    filename = f"random_file_{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}.py"
    file_path = os.path.join(REPO_PATH, filename)
    with open(file_path, 'w') as file:
        file.write(generate_random_content(200))
    return filename

def git_push():
    """Execute Git commands to commit and push changes."""
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", "."], check=True)
        commit_message = f"Automated changes {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing to GitHub: {e}")

def main():
    print("Starting QuantumSimulation Automation...")
    
    # Daily changes to existing files
    files_to_change = ['__init__.py', 'quantum_simulator.py', 'visualization.py']
    for file in files_to_change:
        file_path = os.path.join(REPO_PATH, file)
        if os.path.exists(file_path):
            print(f"Making changes to {file}...")
            make_random_changes(file_path)
        else:
            print(f"File {file} not found, skipping.")
    
    # Weekly random file generation
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    if today.date() == start_of_week.date():
        for _ in range(3):
            new_file = generate_random_file()
            print(f"Generated new file: {new_file}")
    
    # Commit and push changes
    git_push()
    
    print("Automation complete.")

if __name__ == "__main__":
    main()
import os
import random
import string
from datetime import datetime
import subprocess

# GitHub repo details
REPO_PATH = r"C:\Users\ektho\Documents\Playgrounds\QuantumLeapForLunch"  # Change this to the path where your repo is cloned
REMOTE_URL = "git@github.com:CrazyCat556/QuantumLeapForLunch.git"  # Use SSH or HTTPS URL

def generate_random_content():
    """Generate random content for the file."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(random.randint(10, 100)))

def make_changes():
    """Create or modify files with random content."""
    for i in range(30):  # 30 changes
        filename = f"random_file_{i}.txt"
        with open(os.path.join(REPO_PATH, filename), 'w') as f:
            f.write(generate_random_content())

def git_push():
    """Execute Git commands to commit and push changes."""
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Automated random changes {datetime.now()}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)  # Assuming 'main' is your branch name
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    make_changes()
    git_push()
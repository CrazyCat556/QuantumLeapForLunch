import os
import random
import string
from datetime import datetime, timedelta
import subprocess
import time
import json

#123

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
    """Generate a new file in the repository with a quantum or programming related name and structure."""
    quantum_terms = ['qubit', 'entanglement', 'superposition', 'coherence', 'teleportation', 'gate', 'circuit', 'measurement', 'state', 'wavefunction']
    programming_terms = ['function', 'class', 'module', 'script', 'algorithm', 'data', 'logic', 'parser', 'compiler', 'interpreter']
    
    term1 = random.choice(quantum_terms + programming_terms)
    term2 = random.choice(quantum_terms + programming_terms)
    unique_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    
    # Define possible folder structures
    folder_structures = [
        'src',
        'tests',
        'utils',
        'algorithms',
        'quantum',
        'classical',
        'examples',
        'docs'
    ]
    
    # Randomly choose a folder
    folder = random.choice(folder_structures)
    folder_path = os.path.join(REPO_PATH, folder)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created new folder: {folder}")
    
    filename = f"{term1}_{term2}_{unique_id}.py"
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, 'w') as file:
        file.write(generate_random_content(200))
    
    return os.path.join(folder, filename)

def git_push(commit_message):
    """Execute Git commands to commit and push changes with the provided commit message."""
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", "."], check=True)
        
        # Check if there are changes to commit
        status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        if status_result.stdout.strip():
            # There are changes, proceed with commit
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(f"Changes pushed with commit message: '{commit_message}'")
        else:
            # No changes to commit
            print("No changes to commit, skipping commit and push.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing to GitHub: {e}")

def main():
    print("Starting QuantumSimulation Automation...")
    
    # Daily changes to existing files
    files_to_change = ['__init__.py', 'quantum_simulator.py', 'visualization.py']
    changes_made = False
    
    for file in files_to_change:
        file_path = os.path.join(REPO_PATH, file)
        if os.path.exists(file_path):
            print(f"Making changes to {file}...")
            make_random_changes(file_path)
            changes_made = True
    
    # Commit existing files with varied messages
    generic_commit_messages = [
        "Updated code for better performance",
        "Fixed minor bugs",
        "Added new functionality",
        "Refactored existing code",
        "Improved documentation",
        "Enhanced error handling",
        "Optimized quantum operations",
        "Added unit tests",
        "Cleaned up codebase",
        "Implemented new feature"
    ]
    
    if changes_made:
        for file in files_to_change:
            time.sleep(random.randint(1, 5))  # Simulate time passing between commits
            commit_message = random.choice(generic_commit_messages)
            git_push(commit_message)
    
    # Try to generate a new file
    try:
        new_file = generate_random_file()
        print(f"Generated new file: {new_file}")
        
        # Commit the new file
        time.sleep(random.randint(1, 5))  # Simulate time passing before commit
        commit_message = random.choice(generic_commit_messages)
        git_push(commit_message)
    except Exception as e:
        # If file generation fails, we'll just ensure some changes were made
        if not changes_made:
            print("Failed to generate new file and no existing files were changed. Exiting.")
            return
        print(f"Failed to generate new file due to: {e}. Committing existing changes instead.")

    print("Automation complete.")
    print(f"Today is: {datetime.now().date()}")

if __name__ == "__main__":
    main()
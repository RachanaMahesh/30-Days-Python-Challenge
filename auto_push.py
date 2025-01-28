import os
import subprocess

# Path to your local Git repository
base_dir = r"C:\Users\User\FY25\Python\30-Days-Python-Challenge"

def get_latest_folder():
    # List all folders in the repository that start with "Day-"
    folders = [f for f in os.listdir(base_dir) if f.startswith("Day-") and os.path.isdir(os.path.join(base_dir, f))]
    
    # Sort folders numerically by extracting the number (e.g., Day-01 -> 1)
    folders.sort(key=lambda x: int(x.split("-")[1]))
    
    # Return the latest folder
    return folders[-1] if folders else None

def push_to_git():
    try:
        # Navigate to the repository folder
        os.chdir(base_dir)

        # Get the latest folder to push
        folder_to_push = get_latest_folder()

        if not folder_to_push:
            print("No 'Day-XX' folder found to push.")
            return

        # Full path of the folder to push
        folder_path = os.path.join(base_dir, folder_to_push)

        # Add the folder to the Git staging area
        subprocess.run(["git", "add", folder_path], check=True)

        # Commit the changes with a message
        commit_message = f"Added solutions for {folder_to_push}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push the changes to the remote repository
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        print(f"Changes for '{folder_to_push}' pushed successfully to GitHub!")

    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    push_to_git()

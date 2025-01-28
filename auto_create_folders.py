import os

# Base directory (update this to your local repository path)
base_dir = r"C:\Users\User\FY25\Python\30-Days-Python-Challenge"

# Function to determine the next folder
def get_next_folder():
    # List all items in the base directory
    existing_folders = [f for f in os.listdir(base_dir) if f.startswith("Day-") and os.path.isdir(os.path.join(base_dir, f))]
    
    # Sort folders numerically by extracting the number (Day-XX)
    existing_folders.sort(key=lambda x: int(x.split("-")[1]))
    
    if existing_folders:
        # Get the number from the last folder and increment
        last_day = int(existing_folders[-1].split("-")[1])
        next_day = last_day + 1
    else:
        # If no folders exist, start with Day-01
        next_day = 1
    
    # Format the folder name as Day-XX
    return f"Day-{next_day:02d}"

# Create the next folder
def create_folder():
    next_folder = get_next_folder()
    folder_path = os.path.join(base_dir, next_folder)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{next_folder}' created successfully!")
    else:
        print(f"Folder '{next_folder}' already exists.")

# Run the script
if __name__ == "__main__":
    create_folder()

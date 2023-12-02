import os
import shutil

def organize_downloads_folder(folder_path):
    # Define categories and their associated file extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.doc', '.xls'],
        'Exe Files': ['.exe', '.msi', '.app'],
        # Add more categories if needed
    }

    # Create folders for each category
    for category in categories:
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

    # Organize files in the downloads folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Check the file extension and move to the corresponding category folder
            for category, extensions in categories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination_folder = os.path.join(folder_path, category)
                    shutil.move(file_path, destination_folder)
                    print(f"Moved {filename} to {category} folder.")

# Replace 'path_to_downloads_folder' with the actual path to your downloads folder
organize_downloads_folder('path_to_downloads_folder')

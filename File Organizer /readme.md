# File Organizer

## Overview

File Organizer is a Python script designed to simplify the management of your files by categorizing them within a specified folder. This tool intelligently organizes files based on their types, making it easier to locate and maintain a structured file system.

## Features

- **Automatic Organization:** The script categorizes files into folders such as Images, Videos, Documents, and Exe Files.
- **Customization:** Tailor the script to your preferences by modifying categories and file extensions.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/gauravsingh-02/Python/File Organizer.git
1. Navigate to the project directory.

   ```bash
    cd File Organizer
2. Run the script.

   ```bash
    python organizer.py /path/to/target/folder
Replace /path/to/target/folder with the actual path to the folder you want to organize.

Customization
1. Tailor the script to your needs by adjusting the organize_files function in organizer.py. Modify categories and file extensions as needed.

   ```python
    # Define categories and their associated file extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.doc', '.xls'],
        'Exe Files': ['.app'],  # macOS uses .app for applications
        # Add more categories if needed
    }

Feel free to use, modify, and enhance this tool for your unique project needs. Happy coding! 🚀

import os
import shutil
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".bat", ".sh"],
    "Others": [],
}


def organize_files(directory):
    directory = Path(directory)
    if not directory.exists():
        logging.error(f"Directory '{directory}' does not exist.")
        return

    for file in directory.iterdir():
        if file.is_file():
            file_moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    move_file(file, directory / category)
                    file_moved = True
                    break
            if not file_moved:
                move_file(file, directory / "Others")

    logging.info("File organization completed successfully.")


def move_file(file, destination_folder):
    destination_folder.mkdir(exist_ok=True)
    new_location = destination_folder / file.name
    shutil.move(str(file), str(new_location))
    logging.info(f"Moved: {file} -> {new_location}")


if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    organize_files(target_directory)
    print("File organization complete. Check logs for details.")

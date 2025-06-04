import os
import shutil

File_Types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
}

def get_category(filename):
    _, ext = os.path.splitext(filename.lower())
    for category, extensions in File_Types.items():
        if ext in extensions:
            return category
    return "Others"

def organize_folders(folder_path):
    if not os.path.isdir(folder_path):
        print(f"The path {folder_path} is invalid.")
        return
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            category = get_category(file)
            category_folder = os.path.join(folder_path, category)

            if not os.path.exists(category_folder):
                os.mkdir(category_folder)

            shutil.move(file_path, os.path.join(category_folder, file))
            print(f"Moved: {file} -> {category_folder}/")
    print("Organizing completed.")

def main():
    folder = input("Enter the path of the folder to organize: ")
    organize_folders(folder)

if __name__ == "__main__":
    main()
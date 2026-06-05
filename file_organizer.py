import os
import shutil

folder_path = input("Enter the folder path to organize: ")

try:
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
    else:
        file_types = {
            "Images": [".jpg", ".jpeg", ".png"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Videos": [".mp4", ".mkv"],
            "Python_Files": [".py"]
        }

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                moved = False

                for folder_name, extensions in file_types.items():
                    if file_name.lower().endswith(tuple(extensions)):
                        new_folder = os.path.join(folder_path, folder_name)
                        os.makedirs(new_folder, exist_ok=True)

                        shutil.move(file_path, os.path.join(new_folder, file_name))
                        print(f"Moved {file_name} to {folder_name}")
                        moved = True
                        break

                if not moved:
                    other_folder = os.path.join(folder_path, "Others")
                    os.makedirs(other_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(other_folder, file_name))
                    print(f"Moved {file_name} to Others")

except Exception as e:
    print("An error occurred:", e)
    
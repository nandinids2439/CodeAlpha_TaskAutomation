
import os
import shutil

folder_path = input("Enter the folder path to organize: ")

if not os.path.isdir(folder_path):
    print("Folder does not exist!")
else:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if extension:
                folder_name = extension[1:].upper() + " Files"
            else:
                folder_name = "Other Files"

            destination = os.path.join(folder_path, folder_name)
            os.makedirs(destination, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(destination, filename)
            )

    print("Files organized successfully!")

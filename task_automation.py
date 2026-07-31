import os
import shutil

# Source and destination folders
source_folder = "source"
destination_folder = "destination"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpg files
for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(file, "moved successfully.")

print("All JPG files have been moved.")
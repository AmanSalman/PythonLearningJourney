import os

# Define the directory path
directory_path = r"C:\Users\Aman\Desktop\photos"

# Change to the specified directory
os.chdir(directory_path)

# List all files in the directory
file_list = os.listdir()

# Print the current working directory and save it
saved_path = os.getcwd()
print(saved_path)

# Create translation table to remove digits
translation_table = str.maketrans('', '', '0123456789')

# Rename files by removing digits
for file_name in file_list:
    print(file_name)
    new_name = file_name.translate(translation_table)  # Use the translation table to remove digits
    os.rename(file_name, new_name)
print(file_list)
# Change back to the original directory
os.chdir(saved_path)

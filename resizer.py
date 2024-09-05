import os
from PIL import Image

# Define the paths
source_folder = '/Users/jakeziegler/Desktop/images'  # Folder where the original images are stored
destination_folder = 'static/resized_images'  # Folder where the resized images will be saved

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Set the desired resize dimensions
new_size = (800, 800)  # Resize images to 800x600, or whatever dimensions you want

# Get all the image files from the source folder
all_files = [f for f in os.listdir(source_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Prompt the user to either process all files or select specific ones
choice = input(f"There are {len(all_files)} image(s) in the folder. Do you want to process all files? (yes/no): ").strip().lower()

if choice == 'no':
    print("\nAvailable files:")
    for idx, file in enumerate(all_files):
        print(f"{idx + 1}. {file}")
    
    # Ask user to select specific files
    selected_indices = input("Enter the numbers of the files you want to resize (comma-separated): ").strip().split(',')
    files_to_resize = [all_files[int(idx) - 1] for idx in selected_indices]
else:
    # Resize all files
    files_to_resize = all_files

# Loop over the selected files and resize
for filename in files_to_resize:
    img_path = os.path.join(source_folder, filename)
    
    # Get original file size
    original_size = os.path.getsize(img_path)
    
    # Open the image file
    with Image.open(img_path) as img:
        # Prompt for resizing
        resize_choice = input(f"Do you want to resize {filename} to {new_size}? (yes/no): ").strip().lower()
        
        if resize_choice == 'yes':
            # Resize the image
            img = img.resize(new_size)
        
        # Save the resized image
        destination_path = os.path.join(destination_folder, filename)
        img.save(destination_path)
        
        # Get new file size
        new_file_size = os.path.getsize(destination_path)
        
        # Compare and print file sizes
        print(f"Original: {filename} - {original_size / 1024:.2f} KB")
        print(f"Resized: {filename} - {new_file_size / 1024:.2f} KB")
        
        print(f"File {filename} has been resized.\n")

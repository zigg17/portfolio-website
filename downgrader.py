import os
from PIL import Image

# Define the paths
source_folder = 'static/images'  # Folder where the original images are stored
destination_folder = 'static/compressed_images'  # Folder where the optimized images will be saved

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Set the desired quality
new_quality = 10  # JPEG quality from 1 (worst) to 95 (best), 85 is typically a good balance

# Get all the image files from the source folder
all_files = [f for f in os.listdir(source_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Prompt the user to either process all files or select specific ones
choice = input(f"There are {len(all_files)} image(s) in the folder. Do you want to process all files? (yes/no): ").strip().lower()

if choice == 'no':
    print("\nAvailable files:")
    for idx, file in enumerate(all_files):
        print(f"{idx + 1}. {file}")
    
    # Ask user to select specific files
    selected_indices = input("Enter the numbers of the files you want to compress (comma-separated): ").strip().split(',')
    files_to_compress = [all_files[int(idx) - 1] for idx in selected_indices]
else:
    # Compress all files
    files_to_compress = all_files

# Loop over the selected files and compress
for filename in files_to_compress:
    img_path = os.path.join(source_folder, filename)
    
    # Get original file size
    original_size = os.path.getsize(img_path)
    
    # Open the image file
    with Image.open(img_path) as img:
        # Compress without resizing
        destination_path = os.path.join(destination_folder, filename)
        img.save(destination_path, optimize=True, quality=new_quality)
        
        # Get new file size
        new_size = os.path.getsize(destination_path)
        
        # Compare and print file sizes
        print(f"Original: {filename} - {original_size / 1024:.2f} KB")
        print(f"Compressed: {filename} - {new_size / 1024:.2f} KB")
        
        if new_size < original_size:
            print(f"File {filename} is smaller after compression.\n")
        else:
            print(f"File {filename} is not smaller after compression.\n")

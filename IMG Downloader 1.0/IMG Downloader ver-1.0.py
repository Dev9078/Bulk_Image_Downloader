import os
import requests

# Get base URL, range, and file extension from user
base_url = input("Enter the base URL (e.g., https://img.ragalahari.com/gallery/kajalpink/kajalpink): ")
start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))
file_extension = input("Enter the file extension (e.g., .jpg, .aspx): ")

# Ask for directory path or create a new folder
folder_choice = input("Enter the folder name to save images or press Enter to create a new folder: ")
if not folder_choice:
    folder_choice = 'downloaded_images'
folder_path = os.path.join(os.getcwd(), folder_choice)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Created new folder: {folder_path}")

# Function to download images and rename if needed
def download_image(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        original_filename = url.split('/')[-1]
        # Change extension if the original is .aspx
        if file_extension == '.aspx':
            filename = os.path.join(folder, original_filename.replace('.aspx', '.jpg'))
        else:
            filename = os.path.join(folder, original_filename)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")

# Generate image URLs and download images
for i in range(start_number, end_number + 1):
    image_url = f"{base_url}{i}{file_extension}"
    download_image(image_url, folder_path)

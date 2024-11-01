# first install these packages using,
# pip install aiohttp aiofiles tqdm
import os
import asyncio
import aiohttp
from aiofiles import open as aio_open
from tqdm import tqdm

# Get base URL, range, and file extension from user
base_url = input("Enter the base URL : ")
# (e.g., https://img.ragalahari.com/gallery/kajalpink/kajalpink)
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

# Function to download images
async def download_image(session, url, folder):
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                filename = os.path.join(folder, url.split('/')[-1])
                async with aio_open(filename, 'wb') as f:
                    await f.write(await response.read())
                return True
    except Exception:
        pass
    return False

# Main function to handle concurrent downloads
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(start_number, end_number + 1):
            image_url = f"{base_url}{i}{file_extension}"
            tasks.append(download_image(session, image_url, folder_path))
        
        # Use tqdm to show a progress bar
        results = []
        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Downloading"):
            results.append(await f)
        
        successful_downloads = sum(results)
        print(f"\nDownloaded {successful_downloads} out of {len(tasks)} images.")

# Run the main function
asyncio.run(main())
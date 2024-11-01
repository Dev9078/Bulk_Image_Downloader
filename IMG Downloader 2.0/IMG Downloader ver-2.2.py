import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def download_image(url, folder):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        filename = os.path.join(folder, url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        return f"Downloaded: {filename}"
    except requests.exceptions.RequestException:
        return f"Failed to download: {url}"

def main():
    base_url = input("Enter the base URL: ")
    # (e.g., https://img.ragalahari.com/gallery/kajalpink/kajalpink)
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))

    folder_choice = input("Enter the folder name to save images or press Enter to create a new folder: ")
    if not folder_choice:
        folder_choice = 'downloaded_images'
    folder_path = os.path.join(os.getcwd(), folder_choice)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created new folder: {folder_path}")

    urls = [f"{base_url}{i}.jpg" for i in range(start_number, end_number + 1)]
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(download_image, url, folder_path) for url in urls]
        
        with tqdm(total=len(urls), desc="Downloading", unit="image") as pbar:
            for future in as_completed(futures):
                result = future.result()
                if "Downloaded" in result:
                    pbar.update(1)
                else:
                    pbar.write(result)

if __name__ == "__main__":
    main()
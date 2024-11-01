#this program can be fetch multiple image src on the given url
import requests
from bs4 import BeautifulSoup

# Prompt the user for the name of the text file
file_name = input("Enter the filename to save the image URLs (e.g., image_urls.txt): ")

# Open the specified text file to save the image URLs
with open(file_name, 'w') as file:
    while True:
        # Prompt the user for the URL
        url = input("Enter the URL of the .aspx page (or type 'done' to finish): ")

        # Break the loop if the user is done
        if url.lower() == 'done':
            break
        
        response = requests.get(url)

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags
        images = soup.find_all('img')

        # Iterate over each image tag to get the 'src' attribute
        for img in images:
            img_src = img.get('src')
            file.write(img_src + '\n')

print(f"Image URLs have been saved to {file_name}")
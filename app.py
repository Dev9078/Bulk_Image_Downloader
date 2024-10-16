from flask import Flask, request, render_template
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/download', methods=['POST'])
def download_images():
    base_url = request.form['base_url']
    start_number = int(request.form['start_number'])
    end_number = int(request.form['end_number'])
    folder_name = request.form['folder_name']
    
    if not folder_name:
        folder_name = 'downloaded_images'
    
    folder_path = os.path.join(os.getcwd(), folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created new folder: {folder_path}")

    def download_image(url, folder):
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(folder, url.split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")

    for i in range(start_number, end_number + 1):
        image_url = f"{base_url}{i}.jpg"
        download_image(image_url, folder_path)
    
    return "Download complete! Check the folder."

if __name__ == '__main__':
    app.run(debug=True)
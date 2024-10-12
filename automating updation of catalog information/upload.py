#!/usr/bin/env python3

import requests
import glob

imgPath = 'supplier-data/images/*.jpeg'
imgList = glob.glob(imgPath)

url = "http://localhost/upload/"

for path in imgList:
    try:
        with open(path, 'rb') as opened:    
            r = requests.post(url, files={'file': opened})
            if r.status_code in (200, 201):  # Accept both 200 and 201 as success
                print(f"Successfully uploaded {path}")
            else:
                print(f"Failed to upload {path}. Status code: {r.status_code}")  
    except Exception as e:
        print(f"An error occurred while uploading {path}: {e}")

import os
from PIL import Image
import glob

imgPath = 'supplier-data/images/*.tiff'
savePath = 'supplier-data/images'

imgList = glob.glob(imgPath)
for path in imgList:
    try:
        with Image.open(path) as img:
            # Resize the image
            imgResized = img.resize((600, 400))
            # Create the new file name by changing the extension to .jpeg
            newFilename = os.path.splitext(os.path.basename(path))[0] + '.jpeg'
            print(newFilename)
            # Convert to RGB to ensure compatibility with JPEG and save
            imgResized = imgResized.convert("RGB")
            imgResized.save(os.path.join(savePath, newFilename))
    except Exception as e:
        print(f"Error processing file {path}: {e}")

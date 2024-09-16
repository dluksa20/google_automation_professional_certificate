#!/usr/bin/env python3

from PIL import Image
import os
from tqdm import tqdm


def modifyImage(source_path: str, save_path: str):
    """
    Processes images from the source directory, applies transformations, and saves them to the target directory.

    Parameters:
    source_path (str): Path to the directory containing the source images.
    save_path (str): Path to the directory where modified images will be saved.

    The function performs the following operations on each image:
    - Opens the image and converts it to RGB mode.
    - Rotates the image by -90 degrees and resizes it to 128x128 pixels.
    - Saves the processed image as a JPEG file in the save directory.
    """
    
    for filename in tqdm(os.listdir(source_path), desc='Processing images'):
        input_path = os.path.join(source_path, filename)
        output_path = os.path.join(save_path, f'{os.path.splitext(filename)[0]}')

        try:
            # Open the image and convert it to RGB mode
            with Image.open(input_path).convert('RGB') as img:
                # Rotate, resize, and convert image
                res_img = img.rotate(-90).resize((128, 128))  # Rotate and resize
                # Save the image as JPEG
                res_img.save(output_path, format='JPEG')
        except (OSError, IOError) as e:
            print(f"Error processing file {filename}: {e}")


def main(test: bool = False):
    """
    Main function to process images and optionally test the output.

    Parameters:
    test (bool): If True, performs a test to check if a specific output image is saved correctly.

    The function:
    - Creates the save directory if it does not exist.
    - Calls modifyImage to process and save images from the source directory.
    - Optionally tests the saved image if `test` is True.
    """
    
    source_path = 'images'  # Source images path
    save_path = 'opt/icons'  # Save path of new images

    # Create save directory if it does not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)  # Use os.makedirs to create intermediate directories
        # Call method to modify images
    modifyImage(source_path, save_path)

    # Test script to check if the output image is in required shape and format
    if test:
        test_image_path = 'opt/icons/ic_add_location_black_48dp'
        try:
            test = Image.open(test_image_path)
            print(test.format, test.size)
        except (OSError, IOError) as e:
            print(f"Error opening test image: {e}")


if __name__ == '__main__':
    main(test=True)

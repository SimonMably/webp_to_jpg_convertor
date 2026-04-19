import os
import sys
from pathlib import Path

from PIL import Image

# TODO: convert_images()


def convert_image() -> None:
    """Convert a specified image with WEBP file format to an image with JPG file format."""
    folder = Path("C:\\Users\\Simon\\Desktop\\stuff\\imgs")

    selected_img = input(
        "Type the file name of the image that you want to convert (don't include file extension): "
    )
    with Image.open(f"{folder}\\{selected_img}.webp") as image:
        image.save(f"{folder}\\{selected_img}.jpg")

    print("Image successefully converted")

    delete_webp_image(f"{folder}\\{selected_img}.webp")
    print("webp file deleted")


def convert_images() -> None:
    """From a specified folser, convert all images with WEBP file format to JPG file format"""
    # TODO: Rework the below to convert all images from a s
    # image = Image.open("sample.webp")
    # image.save("sample.jpg")

    # Access folder of choice
    # TODO: Choose between creating a cli and inputting folder name or hardcode folder name
    folder = Path("C:\\Users\\Simon\\Desktop\\stuff\\imgs")

    # Doing things with webp files specifically in folder
    for webp_file in folder.glob("*,webp"):
        # TODO: Figure out what to do here
        pass


def delete_webp_image(img) -> None:
    """_summary_

    Arguments:
    img -- webp image that will be deleted after conversion/
    """
    img_to_delete = Path(img)
    img_to_delete.unlink()


if __name__ == "__main__":
    option = int(input("Select option (type number): "))
    if option == 1:
        convert_image()
    elif option == 2:
        convert_images()
    elif option == 3:
        running = False
    else:
        print("Choose an option by typing 1, 2, or 3")

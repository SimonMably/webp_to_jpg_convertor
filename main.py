from pathlib import Path

from PIL import Image, UnidentifiedImageError


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
    """From a specified folder, convert all images with WEBP file format to JPG file format"""
    folder = Path("C:\\Users\\Simon\\Desktop\\stuff\\imgs")

    # In folder, select all files with .webp file extention
    for webp_file in folder.glob("*.webp"):
        try:
            with Image.open(webp_file) as image:
                # .stem removes file extention
                img_name = Path(webp_file).stem
                image.save(f"{folder}\\{img_name}.jpeg", format="JPEG", mode="RGB")
                print(f"{image} converted")
                delete_webp_image(webp_file)
                print(f"{img_name}.webp deleted")
        except UnidentifiedImageError:
            delete_webp_image(webp_file)


def delete_webp_image(img) -> None:
    """
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

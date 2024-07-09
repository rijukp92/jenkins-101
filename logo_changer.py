import os
import re
import shutil
from PIL import Image

# Directory where PNG files are located
directory = r".\logos"
light_directory = r".\logos\light"

icon_filename = ''
logo_filename = ''

icons = ["icon-40x40.png",
         "icon-72x72.png",
         "icon-96x96.png",
         "icon-128x128.png",
         "icon-130x130.png",
         "icon-144x144.png",
         "icon-152x152.png",
         "icon-192x192.png",
         "icon-384x384.png",
         "logo-square.png"
         ]

logos = ["logo-mt.png",
         "logo-nav.png",
         "logo-splash.png",
         "logo-footer.png"
         ]


def has_dark_and_light_logos(directory):
    logo_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            filepath = os.path.join(directory, filename)

            # Load the image using PIL
            image = Image.open(filepath)

            # Retrieve the width and height of the image
            width, height = image.size

            # Check if it is a 250x90 logo
            if width == 250 and height == 90:
                logo_count += 1
            else:
                pass

            # Close the image file
            image.close()

    return logo_count


def move_brightest_logo(directory):
    light_folder = os.path.join(directory, "light")
    if not os.path.exists(light_folder):
        os.makedirs(light_folder)

    brightest_logo_filepath = None
    brightest_logo_brightness = -1  # Initialize to a value less than 0 and 255

    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            filepath = os.path.join(directory, filename)

            # Load the image using PIL
            image = Image.open(filepath)

            # Retrieve the width and height of the image
            width, height = image.size

            # Check if it is a 250x90 logo
            if width == 250 and height == 90:
                # Analyze the brightness of the logo
                brightness = sum(image.convert("L").getdata()) / (width * height)

                # Compare brightness and update the brightest logo
                if brightness > brightest_logo_brightness:
                    brightest_logo_brightness = brightness
                    brightest_logo_filepath = filepath

            # Close the image file
            image.close()

    if brightest_logo_filepath:
        new_filename = os.path.join(light_folder, "light-logo.png")
        shutil.move(brightest_logo_filepath, new_filename)
        light_logo = os.path.join(light_folder, "light-logo.png")
        print(f"Current directory: {os.getcwd()}")
        for logo in logos:
            copy_logo = os.path.join(light_directory, logo)
            shutil.copy(light_logo, copy_logo)

# Move the logo with the highest brightness to the 'light' folder
# Check if two logos exist


if has_dark_and_light_logos(directory) == 2:
    # Move the light logo to the 'light' folder
    move_brightest_logo(directory)


def defining_logo_icon(directory):

    global icon_filename, logo_filename

    icon_filename = ''
    logo_filename = ''

    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            filepath = os.path.join(directory, filename)

            image = Image.open(filepath)
            width, height = image.size

            image.close()
            if width == 512 and height == 512:
                icon_filename = f"icon-{width}x{height}.png"
                try:
                    os.rename(filepath, os.path.join(directory, icon_filename))
                except FileExistsError as e:
                    print("FileExistsError: Ignoring logo_changer.py script due to existing files.")
            if width == 250 and height ==90:
                logo_filename = "logo.png"
                try:
                    os.rename(filepath, os.path.join(directory, logo_filename))
                except FileExistsError as e:
                    print("FileExistsError: Ignoring logo_changer.py script due to existing files.")


def generate_images(directory):
    og_icon_file = os.path.join(directory, icon_filename)
    og_logo_file = os.path.join(directory, logo_filename)

    for icon in icons:
        copy = os.path.join(directory, icon)
        try:
            shutil.copy(og_icon_file, copy)

            dimensions = re.findall(r'\b\d+x\d+\b', icon)
            if dimensions:

                new_width, new_height = map(int, dimensions[0].split('x'))
                # new_height = [int(s) for s in re.findall(r'\b\d+\b', copy)]

                image = Image.open(copy)
                resized_image = image.resize((new_width, new_height))
                resized_image.save(copy)
                image.close()
        except FileExistsError as e:
            print("File exists, skipping...")
        except FileNotFoundError as e2:
            print("FileNotFound, skipping...")

    for logo in logos:
        copy_logo = os.path.join(directory, logo)
        shutil.copy(og_logo_file, copy_logo)

    try:
        logo_square = os.path.join(directory, "logo-square.png")
        square_image = Image.open(logo_square)
        square_width, square_height = [142, 102]
        resized_square = square_image.resize((square_width, square_height))
        resized_square.save(logo_square)
        square_image.close()

        icon_40 = os.path.join(directory, "icon-40x40.png")

        sys_icon = os.path.join(directory, "system-icon.png")
        shutil.copy(icon_40, sys_icon)

        favicon = os.path.join(directory, "favicon.ico")
        shutil.copy(icon_40, favicon)
    except FileNotFoundError as e:
        print("FileNotFound, skipping...")


defining_logo_icon(directory)
generate_images(directory)
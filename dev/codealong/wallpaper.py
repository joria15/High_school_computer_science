"""
author: Anthony Antczak
date: 09/06/2024
A fancy wallpaper engine
"""

# Tell python I want to be able to acces the internet
import time
import urllib.request
# Tell python I want to be able to modify windows parameters
import ctypes
    #ask "lorem picsum" to send over the data of a photo
    url = f"https://picsum.photos/{width}/{height}"
    response = urllib.request.urlopen(url)

    # Step 2: Save (Write) that image to our computer
    file = open(image_name, mode="wb")
    file.write(response.read())

    file.close()

# Step 3: Make that image the windows wallpaper
def set_wallpaper(image_name):

# Tell python I want to be able to lookup folders in the operating system
import os
# Step 1: Download a random image from the internet
def download_image(width, height):
    cwd = os.getcwd()
    wallpaper_path = os.path.join(cwd, image_name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

    image = "temp.jpg"
    user_width = input("Enter the width of the desired wallpaper: ")
    user_height = input("Enter the height of the desired wallpaper: ")
    interval = int("input(How often (in minutes) should I change the wallpaper: ")
    download_image(user_width, user_height, image)
    set_wallpaper(image)

    time.sleep(interval )
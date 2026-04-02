from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow App")

image_paths = [r"A:\College\Screenshot 2025-12-16 131425.png",
               r"A:\College\A1.png",
               r"A:\College\viva maths 2.png"] #Add your image paths here

#Resizing images to fit in the window
image_size=(1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3) #Change the duration of each image in seconds
        
slideshow = cycle(photo_images)
def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()
        
play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()
root.mainloop()
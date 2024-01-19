#importing the necessary libraries
from moviepy.editor import ImageSequenceClip
import os
from PIL import Image
# Set the path to your images
images_folder = r'C:/Users/ADMIN/Documents/from desktop/images'

# Set the output path for your GIF
output_gif = 'animation.gif'

# Set the frame rate (in frames per second)
frame_rate = 100

target_width, target_height = 640, 480
# Iterate through images and resize
for image_file in os.listdir(images_folder):
    image_path = os.path.join(images_folder, image_file)
    img = Image.open(image_path)
    img_resized = img.resize((target_width, target_height))
    img_resized.save(image_path)

# Specify the names of your images
image_names = ['tom.jpg', 'jerry2.jpg']

# Get the full paths of the images
image_paths = [os.path.join(images_folder, img) for img in image_names]

# Create ImageSequenceClip from the list of image files
clip = ImageSequenceClip(images_folder, fps=frame_rate)

# Write the GIF file
clip.write_gif(output_gif, fps=frame_rate)

print("GIF creation complete.")
print(image_paths)

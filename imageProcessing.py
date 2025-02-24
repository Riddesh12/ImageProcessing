import numpy as np
from PIL import Image

def read_image(file_path):

    image = Image.open(file_path)
    return np.array(image), image.mode

def save_image(image_array, mode, save_path):
   
    image = Image.fromarray(image_array.astype('uint8'), mode)
    image.save(save_path)

def invert_colors(image_array):
   
    return 255 - image_array

def grayscale(image_array):

    if len(image_array.shape) == 3:
        return np.dot(image_array[..., :3], [0.2989, 0.587, 0.114])
    return image_array

def adjust_brightness(image_array, value):
   
    return np.clip(image_array + value, 0, 255)

def main():
    input_path ='./Project/imageTesting.png'
    output_path = 'processed_image.png'

   
    image_array, mode = read_image(input_path)

 
    inverted_image = invert_colors(image_array)
    grayscale_image = grayscale(image_array)
    brighter_image = adjust_brightness(image_array, 50)

    save_image(inverted_image, mode, 'inverted_' + output_path)
    save_image(grayscale_image, 'L', 'grayscale_' + output_path)
    save_image(brighter_image, mode, 'brighter_' + output_path)

    print("Images saved: inverted, grayscale, and brighter versions.")

if __name__ == "__main__":
    main()

import cv2
import numpy as np
import os


def get_dark_channel(img, size):

    b, g, r = cv2.split(img)
    min_img = cv2.min(cv2.min(r, g), b)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    dark_channel = cv2.erode(min_img, kernel)
    return dark_channel


def get_atmospheric_light(img, dark_channel):

    h, w = img.shape[:2]
    img_size = h * w
    num_pixels = int(max(img_size * 0.001, 1))

    dark_vec = dark_channel.reshape(img_size)
    img_vec = img.reshape(img_size, 3)

    indices = dark_vec.argsort()[img_size - num_pixels::]
    atmo_light = np.mean(img_vec[indices], axis=0)
    return atmo_light


def extract_fog_mask(image_path, output_path, block_size, sensitivity, blur_sigma):

    print(f"Processing in progress: {image_path} ...")
    if not os.path.exists(image_path):
        print(f"Error: Unable to find the input file {image_path}")
        return

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to decode the image file {image_path}")
        return

    img_float = img.astype('float32') / 255.0

    dark_channel = get_dark_channel(img_float, block_size)

    A = get_atmospheric_light(img_float, dark_channel)

    norm_img = img_float / (A + 1e-6)
    dark_channel_norm = get_dark_channel(norm_img, block_size)
    transmission = 1 - sensitivity * dark_channel_norm

    fog_density = 1 - transmission

    if blur_sigma > 0:
        fog_density = cv2.GaussianBlur(fog_density, (0, 0), sigmaX=blur_sigma)


    fog_final = np.clip(fog_density * 255, 0, 255).astype('uint8')
    cv2.imwrite(output_path, fog_final)
    print(f"Successfully saved as: {output_path}")

if __name__ == '__main__':

    input_image = r'1.jpg'
    output_image = r'1.png'


    current_block_size = 20
    current_blur_sigma = 7
    current_sensitivity = 0.65

    extract_fog_mask(
        input_image,
        output_image,
        block_size=current_block_size,
        sensitivity=current_sensitivity,
        blur_sigma=current_blur_sigma
    )
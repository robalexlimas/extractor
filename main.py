import cv2, os
import numpy as np
import matplotlib.pyplot as plt

def read_images():
    path_dir = os.getcwd()
    path_images = os.path.join(path_dir, 'images')
    full_path_images = []
    images_name = os.listdir(path_images)
    for image in images_name:
        full_path_images.append(os.path.join(path_images, image))
    return full_path_images


def main():
    images = read_images()
    for image in images:
        img = cv2.imread(image)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        threshold_low = (30, 100, 60)
        threshold_high = (85, 255, 190)
        mask = cv2.inRange(img_hsv, threshold_low, threshold_high)
        img_mask = cv2.bitwise_and(img, img, mask=mask)
        plt.subplot(1, 3, 1)
        plt.imshow(mask, cmap='gray')
        plt.subplot(1, 3, 2)
        plt.imshow(img_mask)
        plt.subplot(1, 3, 3)
        plt.imshow(img)
        plt.show()




if __name__ == '__main__':
    main()
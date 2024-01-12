import time
import cv2
import numpy as np

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

n = generated_number
img = cv2.imread("H:/Download/Assignment1/chapter1.jpg")

modified_img = np.clip(img + n, 0, 255).astype(np.uint8)

save_path = 'H:/Download/Assignment 1 2023 .pdf/chapter1out.png'
cv2.imwrite(save_path, modified_img)

red_sum = np.sum(modified_img[:, :, 0])
print(red_sum)

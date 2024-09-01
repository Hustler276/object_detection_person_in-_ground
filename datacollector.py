import os
import time
import uuid
import cv2

IMAGE_PATH = "Collected_images"

labels = ["face"]
number_of_images = 30

for label in labels:
    image_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(image_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print("Collecting images")
    time.sleep(5)

    for imag_num in range(number_of_images):
        ret , frame = cap.read()
        imagename = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()

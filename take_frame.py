import cv2
import numpy as np

def calculate_brightness(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    average_brightness = np.mean(gray_image)
    return average_brightness


def adjust_brightness(image):
    brightness = calculate_brightness(image)
    print(f'Average brightness: {brightness}')

    # Define dynamic threshold and scale factor
    max_brightness = 250
    brightness_threshold = 0.8 * max_brightness  # 80% of max brightness

    if brightness > brightness_threshold:
        excess_brightness = brightness - brightness_threshold
        scale_factor = max(0.4, 1 - (excess_brightness / max_brightness)) 
        adjusted_image = cv2.convertScaleAbs(image, alpha=scale_factor, beta=0)
        return adjusted_image
        
    else:
        print("Image brightness is acceptable.")
        return image


def compute_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var


def capture_and_save_sharpest_frame(cap, num_frames=5, save_path="sharpest_image.jpg"):
    quality_frame = None
    highest_sharpness = 0
   
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            continue

        sharpness = compute_sharpness(frame)
        if sharpness > highest_sharpness:
            highest_sharpness = sharpness
            quality_frame = frame

    if quality_frame is not None:
        quality_frame=adjust_brightness(quality_frame)
        cv2.imwrite(save_path, quality_frame)
        print(f"Sharpest image saved as {save_path}")
    else:
        print("Error: No frames captured.")



# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture and save the sharpest frame
capture_and_save_sharpest_frame(cap, num_frames=5)

cap.release()

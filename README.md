# Best_Image_Grab

This project is developed for autonomous drones equipped with a camera that has a low FPS value. The project captures five frames to eliminate distorted images caused by camera vibrations and other factors. By then analyzing and selecting the sharpest frame and adjusting the brightness, it ensures that the images are clear and free from distortions.

## Features

- **Sharpness Analysis:** Analyzes the sharpness of each frame captured by the camera.
- **Best Frame Selection:** Identifies the sharpest frame among the five captured.
- **Brightness Adjustment:** Adjusts the brightness of the selected sharpest frame.


## Requirements
- Python 3.x
- OpenCV
- NumPy

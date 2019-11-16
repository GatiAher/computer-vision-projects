# computer-vision-projects

Made for the purpose of storing my small open-cv computer vision projects.

## Set-Up

run: `pip install -r requirements.txt` in your shell

## 'cv_identify_boundary_box.py'

### Overview

This project was created to explore reorienting text skew using computer vision. Given an image containing a rotated block of text at an unknown angle, it computes the text skew by computing a bounding box, and then reorients the text.

It creates the boundary box (1) converting the image to black background, white text, (2) grab the (x, y) coordinates of all pixel values that are white, and (3) using cv2.minAreaRect function to compute a rotated bounding box that contains all the points.

Heavily Relied on Tutorial: https://www.pyimagesearch.com/2017/02/20/text-skew-correction-opencv-python/

'images' folder has three pictures, each of the same word ('विमान', Marathi for airplane) rotated a different amount.`pic1.png` = 80 deg, `pic2.png` = 337.4 deg, `pic3.png` = 4.3 deg (according to the rotation tool in Google Slides)

### Run

Run in shell with: `python cv_identify_boundary_box.py --image images/pic2.png`
Where `images/pic2.png` can be replaced with any image


### Expected Output

Two images both with red bounding boxes drawn on them. One is the original skewed text input image, the other is the rotated image.








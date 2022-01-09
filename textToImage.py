'''IMPORT THE REQUIRED LIBRARIES'''
import os
import cv2
import textwrap

# Path to the directory containing Images of Handwritten Characters
DIR = r'C:\Users\kalai\Documents\NITT & W Collab Workshop\Data_new\charset'

'''Fucntion: To adjust the space between each letter in a line'''
def crop(img, cropX = 10, cropY = 10):
    cropped = img[cropY:img.shape[0]-cropY, cropX:img.shape[1]-cropX]
    return cropped

'''Function: To rescale the Output Image to our requirements'''
def rescale(img, scale_x = 0.75, scale_y = 0.75):   
    resized = cv2.resize(img, None, fx = scale_x, fy = scale_y)
    return resized

'''Function: Converts line to Image'''
def lineToImg(line):
    char_images = []            # List to store Ordered images
    for letter in line:
        if ord(letter) > 127:   # Remove the Non-ascii characters
            letter = ' '
        ascii = ord(letter)
        path = os.path.join(DIR, str(ascii)+".jpg")
        char_img = cv2.imread(path)
        #img = cv2.resize(char_img, (200, 150))  # Can be used if the images in the DIR are not of same size
        char_images.append(crop(char_img, 32))   # Cropping to reduce width and arranging it in char_images list
    img_h = cv2.hconcat(char_images)             # Horizontally concatenating tha ordered images to form line Image
    return img_h


# Lists to store the Images of Lines and Paragraphs
line_img = []
para_imgs = []

# Opening the text file which is to be conveted to Image of our Handwriting
f = open("OCR_output.txt",'r')
lines = f.read().splitlines()    # Reading and Splitting into Paragraphs

# Set the required line width (No of characters in each line)
lineWidth = 45

# Creating a textwrap instance
wrapper = textwrap.TextWrapper(width=lineWidth, initial_indent=' ', subsequent_indent=' ')

for i in lines:
    line_list = wrapper.wrap(text=i)     # Seperates paras into lines each of atmost 'lineWidth' long
    if len(line_list) == 0:              # To identify empty lines
        line_list = ' '                  # Empty line should consist of blank spaces so adding spaces
    for line in line_list:
        while len(line) != lineWidth:    # Adding spaces at the end to make all lines of equal width
            line = line + ' '          
        line_img.append(lineToImg(line)) # Appends the converted line Image to line Images list
    img_v = cv2.vconcat(line_img)        # Concatenates the Images of lines vertically to form the paragraph
    para_imgs.append(img_v)              # Append the formed para to the list
    line_img.clear()                     # Clear the line_img list to use for next paragraph
image = cv2.vconcat(para_imgs)           # Vertically concatenates all the paragraphs to form the final Image

rescaled = rescale(image, 0.25, 0.24)    # Adjust width and Height of the final Image

cv2.imshow('Handwritten', rescaled)      # Shows the Final Image
cv2.imwrite('Handwritten.jpg', rescaled) # Saving in the same directory
cv2.waitKey(0)

print('----SUCCESSFULLY CONVERTED----')


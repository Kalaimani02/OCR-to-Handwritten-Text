# OCR-to-Handwritten-Text
Converting Text in image to Text of our Handwriting

# Function
    It takes an image as an input, for example a screenshot of some content in any website. 
    Then it will convert that text to the image of our handwriting.

# Requirements
    We need a charset which contains images of all the characters handwritten and 
    named by their ASCII values

# Explaination
   This program has 2 parts. 
1. First we do OCR on the input image using tesseract and then save the output in a textfile (OCR_output.txt). 
2. Then we use the textwrapper module to wrap the text in the textfile according to our requirements. Then the program identifies the corresponding letter in our charset and concatenates it to produce the final Image, which is the text in out hand writing.

# Input Image
![OCR_input3](https://user-images.githubusercontent.com/89019323/148694325-46e94d2e-34dc-4a88-a65b-83c92f4f0b03.jpg)

# Output Image
![Handwritten](https://user-images.githubusercontent.com/89019323/148694348-788db46e-cd76-49a6-9cda-9ec497dab3d8.jpg)

We can also use the textToImage.py seperately alone. We can copy text from internet and paste it the OCR_output.txt Then the program will convert it to the text of our Handwriting.

# Result from copied text
![Handwritten](https://user-images.githubusercontent.com/89019323/148694474-9b6d16ba-9bc6-4311-b2ab-6ae1bcc4052e.jpg)

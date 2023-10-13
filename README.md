# EyeLight - An Optical Character Recognition (OCR) Powered Web Application

## Introduction

EyeLight is a web application that harnesses the power of Optical Character Recognition (OCR) to extract text from images. This project showcases the seamless integration of various technologies, including Streamlit, OpenCV, EasyOCR, gTTS (Google Text-to-Speech), and GitHub Actions, to create a user-friendly and efficient OCR tool. With EyeLight, users can upload images containing text, extract that text, and even listen to it in audio form.


## Key Features:

Image Upload: EyeLight provides users with a simple interface to upload images. Supported formats include JPG, PNG, and JPEG.

Text Extraction: Once an image is uploaded, users can click the "Extract Text" button to initiate the OCR process. EyeLight employs the EasyOCR library, which is powered by deep learning, to accurately identify and extract text from the image.

Text-to-Speech: One of the standout features of EyeLight is the ability to convert the extracted text into audio. This is made possible through the gTTS (Google Text-to-Speech) library. Users can listen to the extracted text by clicking on the generated audio file.

Restart Functionality: EyeLight ensures user convenience by including a "Start Again" button. This allows users to reset the app to its initial state for processing additional images or text extraction.


## Technology Stack:

EyeLight relies on a diverse set of technologies:

Streamlit: This Python library simplifies the creation of web applications with minimal effort, enabling developers to design interactive and visually appealing user interfaces.

OpenCV: OpenCV (Open Source Computer Vision Library) is employed for image processing. It is used to display uploaded images and highlight the recognized text.

EasyOCR: EasyOCR is a deep learning-based library for OCR. In EyeLight, it plays a pivotal role in accurately recognizing and extracting text from images.

gTTS (Google Text-to-Speech): gTTS is used for converting extracted text into audio. It facilitates a user-friendly and inclusive experience for those who prefer listening to the content.

## Running Code

```bash
git clone https://github.com/Aligitrepo/image_text_to_voice.git
```
For running this project we need to install streamlit opencv-python easyocr torch gTTS numpy

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```

## Conclusion:

EyeLight is a example of how the integration of multiple technologies can result in a powerful and user-friendly application. By combining Streamlit, OpenCV, EasyOCR, gTTS, and GitHub Actions, it provides an intuitive and efficient platform for text extraction and text-to-speech conversion. Whether it's for digitizing printed content or providing accessibility options, EyeLight stands as a versatile solution that can be accessed directly on GitHub.

This project demonstrates the capabilities of OCR technology and how it can be leveraged to enhance user experiences by making information more accessible. EyeLight is a valuable addition to the growing landscape of AI-powered web applications, serving users with efficiency and accessibility in mind.










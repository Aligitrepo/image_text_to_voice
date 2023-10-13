import streamlit as st
import os
import cv2
import easyocr
import numpy as np
from torch.cuda import is_available
from gtts import gTTS
import io


class Reader:
    def __init__(self, is_cuda=False):
        self.reader = easyocr.Reader(['en'], gpu=is_cuda, model_storage_directory=os.path.join('models'),
                                     download_enabled=True)

    def __call__(self, img):
        return self.extract_text(img)

    def extract_text(self, img, show_text=False, show_confidence=False):
        result = self.reader.readtext(img)

        extracted_text = []

        for text in filter(lambda x: x[-1] > .45, result):
            box, acc_text, confidence = text

            img = cv2.rectangle(img, [int(i) for i in box[0]], [int(i) for i in box[2]], (0, 255, 0),
                                2)

            if show_text and show_confidence:
                img_text = f'{acc_text} - ({"{:.3f}".format(confidence)}%)'

            elif show_text:
                img_text = acc_text

            elif show_confidence:
                img_text = f'CONF: ({"{:.3f}".format(confidence)}%)'

            if show_text or show_confidence:
                img = cv2.putText(
                    img,
                    img_text,
                    (int(box[0][0]), int(box[0][1] - 3)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=.5,
                    color=(168, 90, 50),
                    thickness=2
                )

            extracted_text.append(acc_text)

        return extracted_text, img



st.set_page_config(layout="wide")
st.title("EyeLight")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        reader = Reader()
        img = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
        text, extracted_image = reader.extract_text(img, show_text=True, show_confidence=True)

        st.subheader("Extracted Text")
        st.write(" ".join(text))
        text = ' '.join(text)
        tts = gTTS(text)
        tts.save("output.mp3")
        audio_file = open("output.mp3", 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')
        # Add a "Start Again" button
        if st.button("Start Again"):
            st.experimental_rerun()
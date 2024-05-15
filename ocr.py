import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("Easy OCR - Extract Text from Images")

#subtitle
st.markdown("Image Reader")
st.markdown("")
#image uploader
image = st.file_uploader(label = "Show me your image",type=['png','jpg','jpeg'])


@st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) 
    st.image(input_image) 

    with st.spinner("🤖 AI in action hold tight <3"):
        result = reader.readtext(np.array(input_image))
        result_text = []
        for text in result:
            result_text.append(text[1])
        st.write(result_text)
    st.balloons()
else:
    st.write("Show me image")

st.caption("Developed by the greatest AI enginner of century @CHIRAG")






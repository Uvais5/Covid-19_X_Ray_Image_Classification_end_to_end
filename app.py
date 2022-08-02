import streamlit as st 
import numpy as np 
import tensorflow as tf 
import keras 
from keras.layers import *
from keras.models import *
from keras.preprocessing import image
from PIL import Image
import base64
#stremalit title
st.title("Covid-19 cheast X_Ray Classification 🤢")

#streamlit uploader function
uploaded_files = st.file_uploader(label="Choose a X_Ray", type=["png","jpg","jpeg"])
predict = "❌Plase Enter the X_Ray image first❌❌❌"
#Load the model i save  and images to classify 
model = load_model("CNN_model1.h5")

if uploaded_files is not None:# if image is upload then this function called 
    show_image = Image.open(uploaded_files)# Our uploaded images first show to the app how 
    st.image(show_image)
    image_data = uploaded_files.read()# we read our image  to use this function 
    test_image = show_image.resize((224,224))# we resize the images
    test_image = image.img_to_array(test_image)# we convert image to array
    test_image = np.expand_dims(test_image,axis = 0)# The expand_dims() function is used to expand the shape of an array
    result = model.predict(test_image)# Now we predict the image
    if result [0][0] == 1:# if  predict 0 then we found covid if 1 we found normal
        predict = 'Normal'
        new_prediction = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Normal</p>'
    else:
        predict = 'Covid'
        new_prediction1 = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">Covid-19</p>'
        
else:# if we dont upload the image we see this message
    st.write("Please Enter the image🖼️")
# Streamlite button for Classification
if st.button("Test The X_Ray"): # our button name 
    if predict == "Normal": # if our predict veriable gave normal then we need to show image and normal msg
        st.write(predict)# this every time button click and image is upload so message is pop up
        st.markdown(new_prediction, unsafe_allow_html=True)
        image = Image.open('no covid.jpg')# this is image to show up for normal sigh
        st.image(image)
        nor = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">THis X_Ray image is Normal</p>'
        st.markdown(nor,unsafe_allow_html=True)
    else:
        st.write(predict) # predict variable is gave covid then we need to show covid Sign image and message
        st.markdown(new_prediction1, unsafe_allow_html=True)
        image = Image.open('covid-19.png')
        st.image(image)
        cov = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">THis X_Ray image have a covid-19</p>'
        st.markdown(cov,unsafe_allow_html=True)
        
#This is extra feature to resize the streamlit button and all
k = st.markdown("""
<style>
div.stButton > button:first-child {
padding: 15px 300px;
}
</style>""", unsafe_allow_html=True)
############################################
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
.stApp {
  background-image: url("data:image/png;base64,%s");
  background-size: cover;
}
</style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('Covid.jpg')
#########################################

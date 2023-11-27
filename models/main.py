import streamlit as st
import tensorflow as tf
import cv2
import numpy as np

# Load the pre-trained model
model = tf.keras.models.load_model("Trained_Malaria.model") 
category = ['Uninfected', 'Parasitized']


def prepare_image(image):
    # Convert the Image object to a NumPy array
    img_array = np.array(image)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    img_array = img_array / 255.0
    new_array = cv2.resize(img_array, (224, 224))  # Resnet expects 224x224 images
    return new_array.reshape(-1, 224, 224, 3)

def main():
    st.title("Detecting Image Cells that contain Malaria or not")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Classify"):
            prepared_image = prepare_image(image)
            prediction = model.predict(prepared_image)
            predicted_category_index = np.argmax(prediction)
            predicted_category = category[predicted_category_index]
            st.success(f"Prediction: {predicted_category}")

if __name__ == "__main__":
    main()

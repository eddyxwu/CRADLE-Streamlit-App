import streamlit as st

# st.set_page_config(page_title="My contrail app", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
# st.subheader("Hi I'm eddy!")
# st.title("A high schooler working on an ambitious project")
# st.write("I want to find ways to prevent contrails with AI and ML")
# st.write("This is a test")

def main():
    st.set_page_config(page_title="Camera and File Uploader App", page_icon=":camera:", layout="wide")
    st.title("Camera and File Uploader App")

    # Take a picture using the camera
    st.header("Take a Picture")
    captured_image = st.camera_input("take a picture of a contrail!")

    # Upload an image
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if captured_image is not None:
        st.image(captured_image, caption="Captured Image", use_column_width=True)

if __name__ == "__main__":
    main()
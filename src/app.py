from pathlib import Path

import streamlit as st
from src.operations import Operations
from PIL import Image
from streamlit_drawable_canvas import st_canvas


def main():
    st.set_page_config('Digit recognition')
    st.title("Handwritten Digit Recognition")

    image_option = st.selectbox(
        "Choose a digit",
        list(range(10)),
        help="Select a digit to display its image."
    )

    selected_image = Path("images", "digits").joinpath(f"{image_option}.png")
    image = Image.open(selected_image)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("Draw the digit:")
        canvas = st_canvas(
            fill_color="black",
            stroke_width=10,
            stroke_color="rgb(0, 0, 0)",
            background_color="white",
            update_streamlit=True,
            height=150,
            width=150,
            drawing_mode="freedraw",
            display_toolbar=True,
            key="canvas"
        )

    with col2:
        st.write("Selected digit:")
        st.image(image, caption='Selected digit', use_column_width="never", width=150)

    with col3:
        if st.button("Compare"):
            score, label = Operations.calculate_similarity(
                canvas.image_data,
                image_option)
            st.header(f'Result: {label}')
            st.markdown(f"Score: {score}")

if __name__ == "__main__":
    main()

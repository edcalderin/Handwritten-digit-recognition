from pathlib import Path
from typing import Tuple

import numpy as np
import streamlit as st
from array_numbers import numbers_dict
from label_scores import LabelScores
from operations import Operations
from PIL import Image
from streamlit_drawable_canvas import st_canvas


def calculate_similarity(image_data: np.ndarray,
                         image_option: int) -> Tuple[float, str]:
    """Process cosine similarity and return a label representation according the score.

    Args:
        image_data (np.ndarray): Drawable canvas by user.
        image_option (int): Selected image option between 0 and 9.

    Returns:
        Tuple[float, str]: A tuple containing the cosine similarity score with a label
        corresponding to one of the following categories: Excellent, Good or Bad.
    """
    processed_canvas = Operations.process_canvas(image_data)
    original_image = np.array(numbers_dict.get(image_option))
    similarity: float =  Operations.cosine_similarity(original_image, processed_canvas)
    similarity = round(similarity, 4)

    label = LabelScores.BAD
    if similarity > 0.7:
        label = LabelScores.EXCELLENT
    elif similarity > 0.4:
        label = LabelScores.GOOD

    return similarity, label.value

def main():
    st.title("Handwritten Number Detector")

    image_option = st.selectbox(
        "Choose a number",
        list(range(10)),
        help="Select a number to display its image."
    )

    selected_image = Path("images", "numbers").joinpath(f"{image_option}.png")
    image = Image.open(selected_image)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("Draw the number:")
        canvas = st_canvas(
            fill_color="lightblue",  # Change fill color
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
        st.write("Selected number:")
        st.image(image, caption='Selected number', use_column_width="never", width=150)

    with col3:
        if st.button("Compare"):
            score, label = calculate_similarity(canvas.image_data, image_option)
            st.header(f'Result: {label}')
            st.markdown(f"Score: {score}")

if __name__ == "__main__":
    main()

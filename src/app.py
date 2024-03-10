from typing import Tuple
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np
from pathlib import Path
from array_numbers import numbers_dict
from operations import Operations

def calculate_similarity(canvas, image_option: int) -> Tuple[float, str]:
    """Process cosine similarity and return a label representation according the score.

    Args:
        canvas (_type_): Drawable canvas by user.
        image_option (int): Selected image option between 0 and 9.

    Returns:
        Tuple[float, str]: Tuple with cosine similarity score and a label equivalent either to: Excellent, Good or Bad.
    """       
    processed_canvas = Operations.process_canvas(canvas.image_data)
    original_image = np.array(numbers_dict.get(image_option))
    similarity: float =  Operations.cosine_similarity(original_image, processed_canvas)
    similarity = round(similarity, 4)
    
    label: str = 'Bad'
    if similarity > 0.7:
        label = 'Excellent'
    elif similarity > 0.4:
        label = 'Good'
    
    return similarity, label
    
def onchange_select():
    st.session_state.canvas_data = None

def main():
    st.title("Handwritten Number Detector")

    image_option = st.selectbox(
        "Choose a number",
        list(range(10)),
        help="Select a number to display its image.",
        on_change=onchange_select
    )

    selected_image = Path("images/numbers").joinpath(f"{image_option}.png")
    image = Image.open(selected_image)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.write("Draw the number:")
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
        st.write("Selected number:")
        st.image(image, caption='Selected number', use_column_width="never", width=150)

    with col3:
        if st.button("Compare"):
            score, label = calculate_similarity(canvas, image_option)
            st.subheader(label)
            st.markdown(f"Score: {score}")

if __name__ == "__main__":
    main()

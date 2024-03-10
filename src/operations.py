import numpy as np
from PIL import Image

class Operations:
    """Class with isolated methods to process data."""
    
    @staticmethod
    def cosine_similarity(matrix_1: np.ndarray, matrix_2: np.ndarray) -> float:
        """Calculate the cosine similarity score.

        Args:
            matrix_1 (np.ndarray): Bi-dimensional Numpy array
            matrix_2 (np.ndarray): Bi-dimensional Numpy array

        Returns:
            float: Value between 0 and 1
        """        
        dot_product: float = np.dot(matrix_1.flatten(), matrix_2.flatten())
        norm_product: float = np.linalg.norm(matrix_1) * np.linalg.norm(matrix_2)
        
        # If user did not drawed on the canvas area
        if norm_product == 0:
            return 0
        return dot_product / norm_product
    
    @staticmethod
    def process_canvas(canvas) -> np.ndarray:
        """Convert a four-channel canvas image to 1 channel.

        Args:
            canvas: Drawable canvas by user.

        Returns:
            np.ndarray: Numpy array representation
        """        
        img = Image.fromarray(canvas.image_data)
        one_channel_img = np.array(img.convert("L"))
        # Turn white pixels into black and viceversa.
        return 255 - one_channel_img

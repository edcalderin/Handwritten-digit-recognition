import numpy as np
from PIL import Image

class Operations:
    
    @staticmethod
    def cosine_similarity(matrix_1: np.ndarray, matrix_2: np.ndarray) -> float:
        """Calculate the cosine similarity

        Args:
            matrix_1 (np.ndarray): Bi-dimensional Numpy array
            matrix_2 (np.ndarray): Bi-dimensional Numpy array

        Returns:
            float: Value between 0 and 1
        """        
        dot_product: float = np.dot(matrix_1.flatten(), matrix_2.flatten())
        norm_product: float = np.linalg.norm(matrix_1) * np.linalg.norm(matrix_2)
        return dot_product / norm_product
    
    @staticmethod
    def process_canvas(canvas) -> np.ndarray:
        """Convert a drawable canvas to one-channel image

        Args:
            canvas: Canvas

        Returns:
            np.ndarray: Numpy array representation
        """        
        img = Image.fromarray(canvas.image_data)
        return 255 - np.array(img.convert("L"))

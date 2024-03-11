from typing import Tuple

import numpy as np
from PIL import Image

from src.array_digits import digits_dict
from src.label_scores import LabelScores


class Operations:
    """Class with isolated methods to process data."""

    def _cosine_similarity(self, matrix_1: np.ndarray, matrix_2: np.ndarray) -> float:
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

    def _process_canvas(self, image_data: np.ndarray) -> np.ndarray:
        """Convert a four-channel canvas image to 1 channel.

        Args:
            image_data (np.ndarray): Drawable canvas by user.

        Returns:
            np.ndarray: Numpy array representation
        """
        img = Image.fromarray(image_data)
        one_channel_img = np.array(img.convert("L"))
        # Turn white pixels into black and viceversa.
        return 255 - one_channel_img

    @classmethod
    def calculate_similarity(cls,
                             image_data: np.ndarray,
                             image_option: int) -> Tuple[float, str]:
        """User representation of cosine similarity.
        Return the cosine similarity value along with a category according the score
        corresponding to one of the following: Excellent, Good or Bad.

        Args:
            image_data (np.ndarray): Drawable canvas by user.
            image_option (int): Selected image option between 0 and 9.

        Returns:
            Tuple[float, str]: A tuple containing the cosine similarity score and its
            category.
        """
        processed_canvas = cls._process_canvas(cls, image_data)
        original_image = np.array(digits_dict.get(image_option))
        similarity: float =  cls._cosine_similarity(cls,
                                                    original_image,
                                                    processed_canvas)
        similarity = round(similarity, 4)

        label = LabelScores.BAD
        if similarity > 0.7:
            label = LabelScores.EXCELLENT
        elif similarity > 0.4:
            label = LabelScores.GOOD

        return similarity, label.value

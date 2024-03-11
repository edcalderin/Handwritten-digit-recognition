import numpy as np

from src.array_digits import digits_dict
from src.label_scores import LabelScores
from src.operations import Operations

operations = Operations()

class TestCosineSimilarity:

    def test_complete_similarity(self):
        m1 = np.eye(2)
        m2 = m1.copy()
        cosine_similarity: float = operations._cosine_similarity(m1, m2)
        assert round(cosine_similarity, 2) == 1

    def test_no_similarity(self):
        m1 = np.random.randn(4, 4)
        m2 = np.random.randn(4, 4) * 0.5
        cosine_similarity: float = operations._cosine_similarity(m1, m2)
        assert cosine_similarity < 0.9

    def test_matrix_with_zeros(self):
        m1 = np.eye(2)
        m2 = np.zeros((2, 2))
        cosine_similarity: float = operations._cosine_similarity(m1, m2)
        assert cosine_similarity == 0

class TestProcessCanvas:

    def test_process_canvas(self):
        input_shape = 3, 3
        n_channels: int = np.random.randint(2, 4)

        # Generating a random matrix of (input_shape x n_channels) with values
        # from 0 to 255 and type uint8
        image_data = np.random.randint(0,
                                       255,
                                       (*input_shape, n_channels),
                                       dtype='uint8')

        result = operations._process_canvas(image_data)
        assert result.shape == input_shape

class TestCalculateSimilarity:

    def test_case_excellent(self):
        digit: int = np.random.randint(0, 9)
        array_digit = np.array(digits_dict[digit], dtype='uint8')
        array_digit = np.expand_dims(array_digit, 2)
        array_digit = np.repeat(array_digit, 4, axis=2)
        array_digit = 255 - array_digit

        score, label = operations.calculate_similarity(array_digit, digit)

        assert score == 1
        assert label == LabelScores.EXCELLENT.value

    def test_case_bad(self):
        digit: int = np.random.randint(0, 9)
        array_digit = np.array(digits_dict[digit])
        image = np.ones((*array_digit.shape, 3), dtype='uint8') * 255

        score, label = operations.calculate_similarity(image, digit)

        assert score == 0
        assert label == LabelScores.BAD.value

import numpy as np
from src.operations import Operations

class TestCosineSimilarity:
    
    def test_complete_similarity(self):
        A = np.eye(2)
        B = A.copy()
        cosine_similarity: float = Operations.cosine_similarity(A, B)
        assert round(cosine_similarity, 2) == 1
    
    def test_no_similarity(self):
        A = np.random.randn(2,2)
        B = np.random.randn(2,2)*0.5
        cosine_similarity: float = Operations.cosine_similarity(A, B)
        assert cosine_similarity < 0.9

    def test_matrix_with_zeros(self):
        A = np.eye(2)
        B = np.zeros((2,2))
        cosine_similarity: float = Operations.cosine_similarity(A, B)
        assert cosine_similarity == 0

class TestProcessCanvas:
    
    def test_process_canvas(self):
        input_shape = 3,3
        n_channels: int = np.random.randint(1, 4)

        # Generating a random matrix of (input_shape x n_channels) with values from 0 to 255 and type uint8
        image_data = np.random.randint(0, 255, (*input_shape, n_channels), dtype='uint8')

        result = Operations.process_canvas(image_data)
        assert result.shape == input_shape

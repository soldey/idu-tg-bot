import torch
from sentence_transformers import SentenceTransformer


class VectorizerService:
    def __init__(self, model_name: str):
        # Load or create a SentenceTransformer model.
        model = SentenceTransformer(model_name)
        # Get device like 'cuda'/'cpu' that should be used for computation.
        if torch.cuda.is_available():
            model = model.to(torch.device("cuda"))
        print(model.device)
        self.model = model

    def embed(self, prompt: str):
        return self.model.encode(prompt)



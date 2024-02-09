from langchain.embeddings.huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name="thenlper/gte-large")
    return embedding_model
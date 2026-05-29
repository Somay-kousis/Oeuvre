from langchain_voyageai import VoyageAIEmbeddings
from app.config import VOYAGE_API_KEY

def get_embeddings():
    return VoyageAIEmbeddings(
        voyage_api_key=VOYAGE_API_KEY,
        model="voyage-4-lite",
    )
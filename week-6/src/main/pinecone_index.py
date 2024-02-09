from pinecone import Pinecone
import pinecone
import os

key = os.getenv('PINECONE_API_KEY')
client = Pinecone(api_key=key)

index_name = 'trng-index'
def get_index(index_name:str):
    index = client.Index(index_name)
    return index
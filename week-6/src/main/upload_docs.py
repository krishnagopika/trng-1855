# This script is used to create vector embeds and upload them to pinecone db.
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone

load_dotenv()

loader = TextLoader("C:/TrainingMaterial/generative-ai/genai-material/trng-1855/trng-git-repo/trng-1855/week-6/src/assets/brightspeed-sales.txt")
pages = loader.load_and_split()

embeddings_model = HuggingFaceEmbeddings(
    model_name="thenlper/gte-large",
    encode_kwargs={"normalize_embeddings": True},
)
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
documents = text_splitter.split_documents(pages)

# specify your Pineocne Index name
index= "trng-index"
    
Pinecone.from_documents(documents, embeddings_model, index_name=index)


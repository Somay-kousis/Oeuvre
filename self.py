from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

loader = DirectoryLoader(
    "data",
    glob="*.md",
    loader_cls=TextLoader
)

docs = loader.load()

print(len(docs))

for doc in docs[:3]:
    print(doc.metadata)

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap =200 )
chunks = splitter.split_documents(docs)

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

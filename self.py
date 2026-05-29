from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_voyageai import VoyageAIEmbeddings
import os
from dotenv import load_dotenv
from supabase import create_client
from langchain_community.vectorstores import SupabaseVectorStore
import time

load_dotenv()


loader = DirectoryLoader(
    "data",
    glob="*.md",
    loader_cls=TextLoader
)

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size = 1600, chunk_overlap =200 )
chunks = splitter.split_documents(docs)

embedding = VoyageAIEmbeddings(
    voyage_api_key=os.getenv("VOYAGE_API_KEY"),
    model="voyage-4-lite"
)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

vectorstore = SupabaseVectorStore(
    client=supabase,
    embedding=embedding,
    table_name="documents",
    query_name="match_documents",
)

batch_size = 8

for i in range(0, len(chunks), batch_size):
    batch = chunks[i:i + batch_size]

    vectorstore.add_documents(batch)

    print(f"Uploaded {i + len(batch)} / {len(chunks)}")

    time.sleep(25)

print("Uploaded chunks", len(chunks))
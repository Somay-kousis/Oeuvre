import time
from app.loader import load_and_split_docs
from app.vectorstore import get_vectorstore

def ingest_docs():
    chunks = load_and_split_docs()
    vectorstore = get_vectorstore()

    print(f"Total chunks: {len(chunks)}")

    batch_size = 8

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        vectorstore.add_documents(batch)

        print(f"Uploaded {i + len(batch)} / {len(chunks)}")

        time.sleep(10)

    print("Uploaded chunks:", len(chunks))

if __name__ == "__main__":
    ingest_docs()
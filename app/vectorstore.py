from supabase import create_client
from langchain_community.vectorstores import SupabaseVectorStore

from app.config import SUPABASE_URL, SUPABASE_SERVICE_KEY, TABLE_NAME, QUERY_NAME
from app.embeddings import get_embeddings

def get_vectorstore():
    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_SERVICE_KEY,
    )

    return SupabaseVectorStore(
        client=supabase,
        embedding=get_embeddings(),
        table_name=TABLE_NAME,
        query_name=QUERY_NAME,
    )
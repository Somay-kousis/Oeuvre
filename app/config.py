import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")

TABLE_NAME = "documents"
QUERY_NAME = "match_documents"
COLLECTION_NAME = "self_memory"
# users/utils.py
from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_document_to_supabase(file_obj, filename):
    bucket_name = "documents"
    file_bytes = file_obj.read()
    result = supabase.storage.from_(bucket_name).upload(filename, file_bytes)
    
    if result.get("error"):
        raise Exception(result["error"]["message"])

    public_url = supabase.storage.from_(bucket_name).get_public_url(filename)["publicURL"]
    return public_url
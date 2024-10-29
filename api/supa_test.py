import hashlib
from supabase import create_client, Client


#Supabase data connectio: URL, KEY 
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9sdGVrYmt4c2xrcXloY2diaGZ6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2NjMsImV4cCI6MjA0NTc0MjY2M30.lanFMkuumBz5xphltzydvn2fXD_OOq2nGJZRxJ7glNE"
SUPABASE_URL = "https://oltekbkxslkqyhcgbhfz.supabase.co"

# Connect to Supebase Client

supabase: Client = create_client(SUPABASE_URL,SUPABASE_KEY)

# Get an save data function
def save_data(e, p):
    #Insert into user model
    enc_pass = hashlib.sha256(p.encode()).hexdigest()

    response = supabase.table('users').insert({"email": e, "password": enc_pass}).execute()
    if response.data:
        print(f"User has been save successfully: {response.data}") 
    elif response.error:
        print(f"Error saving user: {response.error}")
    
# Main
email = input("User e-mail: ")
passwd = input("User password: ")
save_data(email, passwd)
import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENAI_API_KEY")
print(f"Chave carregada: {key[:10]}...{key[-4:] if key else 'NADA'}")
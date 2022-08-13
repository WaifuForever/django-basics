import dotenv
import os

dotenv.load_dotenv()

PORT = int(os.getenv("PORT", "5000"))
CLIENT = os.getenv("CLIENT", "*")
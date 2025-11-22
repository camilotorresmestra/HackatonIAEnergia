import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# ---------- Gemini ----------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set")

genai.configure(api_key=GEMINI_API_KEY)

# ---------- ElevenLabs ----------
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
if not ELEVENLABS_API_KEY or not ELEVENLABS_VOICE_ID:
    raise ValueError("ELEVENLABS_API_KEY or ELEVENLABS_VOICE_ID are not set")

# ---------- Supabase (Optional) ----------
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Only initialize supabase_client if credentials are provided
supabase_client = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        from supabase import create_client
        supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
    except ImportError:
        print("Warning: supabase-py not installed. Database features will not be available.")

# ---------- App constants ----------
# Railway provides PORT environment variable
PORT = int(os.getenv("PORT", "8000"))
BASE_PUBLIC_URL = os.getenv("BASE_PUBLIC_URL", f"http://localhost:{PORT}")

# Audio directory for generated TTS files
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)
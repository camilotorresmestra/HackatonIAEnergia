# HackatonIAEnergia

Domu Walkie-Talkie Voice Backend - A FastAPI application for voice-based car sales interactions.

## Features

- WebSocket-based voice communication
- Audio transcription using Google Gemini
- Text-to-speech using ElevenLabs
- Intent analysis for Spanish conversations
- Car sales conversation handling

## Deployment to Railway

### Prerequisites

1. A Railway account (https://railway.app)
2. API keys for:
   - Google Gemini API
   - ElevenLabs API

### Deployment Steps

1. **Fork or clone this repository**

2. **Create a new project on Railway**
   - Go to https://railway.app/new
   - Select "Deploy from GitHub repo"
   - Select this repository

3. **Configure environment variables**
   
   In your Railway project settings, add the following environment variables:
   
   ```
   GEMINI_API_KEY=your_gemini_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ELEVENLABS_VOICE_ID=your_voice_id
   BASE_PUBLIC_URL=https://your-app.railway.app
   ```
   
   Optional (if using database features):
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```

4. **Deploy**
   - Railway will automatically detect the `Procfile` and `railway.json`
   - The application will build and deploy automatically
   - The `PORT` environment variable is automatically set by Railway

5. **Access your application**
   - Railway will provide a public URL (e.g., `https://your-app.railway.app`)
   - Update `BASE_PUBLIC_URL` environment variable with this URL

## Local Development

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/camilotorresmestra/HackatonIAEnergia.git
   cd HackatonIAEnergia
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

5. **Access the application**
   - Health check: http://localhost:8000/health
   - WebSocket endpoint: ws://localhost:8000/ws/voice

## API Endpoints

### HTTP Endpoints

- `GET /health` - Health check endpoint
- `GET /audio/{filename}` - Serve generated audio files

### WebSocket Endpoints

- `WS /ws/voice` - Voice communication endpoint
  - Receives audio blobs (WebM format)
  - Returns JSON with transcription, intent, reply text, and audio URL

## Project Structure

```
.
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration and environment variables
│   ├── ws_routes.py         # WebSocket routes
│   ├── models.py            # Pydantic models
│   ├── gemini_service.py    # Google Gemini integration
│   ├── elevenlabs_service.py # ElevenLabs TTS integration
│   ├── sentiment.py         # Intent analysis
│   ├── utils.py             # Utility functions
│   └── database.py          # Database operations (optional)
├── audio/                   # Generated audio files directory
├── requirements.txt         # Python dependencies
├── Procfile                 # Railway/Heroku deployment config
├── railway.json             # Railway-specific configuration
└── .env.example             # Example environment variables

```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server
- **Google Gemini** - Audio transcription and AI response generation
- **ElevenLabs** - Text-to-speech conversion
- **WebSockets** - Real-time bidirectional communication

## License

This project is part of HackatonIAEnergia.
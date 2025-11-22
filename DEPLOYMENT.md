# Railway Deployment Guide

## Quick Start

This application is configured to deploy seamlessly on Railway with minimal setup.

### 1. Prerequisites

- A Railway account (https://railway.app)
- GitHub account with access to this repository
- API Keys:
  - Google Gemini API Key
  - ElevenLabs API Key
  - ElevenLabs Voice ID

### 2. Deploy to Railway

#### Option A: Deploy from GitHub (Recommended)

1. **Login to Railway**: Visit https://railway.app and sign in with GitHub

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your repositories
   - Select this repository

3. **Configure Environment Variables**:
   Railway will automatically detect the configuration files. Add these environment variables:
   
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key
   ELEVENLABS_API_KEY=your_actual_elevenlabs_key
   ELEVENLABS_VOICE_ID=your_actual_voice_id
   BASE_PUBLIC_URL=https://your-app-name.up.railway.app
   ```

4. **Deploy**:
   - Railway will automatically build and deploy your application
   - The build process uses `nixpacks.toml` and `Procfile`
   - `PORT` is automatically provided by Railway

5. **Get Your URL**:
   - Once deployed, Railway provides a public URL
   - Update the `BASE_PUBLIC_URL` environment variable with this URL
   - Railway will automatically redeploy with the new configuration

#### Option B: Deploy via Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Link to your project (or create new)
railway link

# Set environment variables
railway variables set GEMINI_API_KEY=your_key
railway variables set ELEVENLABS_API_KEY=your_key
railway variables set ELEVENLABS_VOICE_ID=your_voice_id

# Deploy
railway up
```

### 3. Verify Deployment

Once deployed, test your endpoints:

```bash
# Health check
curl https://your-app.railway.app/health

# Should return: {"status":"ok"}
```

### 4. Optional: Add Supabase Database

If you want to use the database features:

1. Add a Supabase project in Railway or use external Supabase
2. Add environment variables:
   ```env
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```

## Configuration Files Explained

### Procfile
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
- Tells Railway how to start the application
- Uses the PORT environment variable provided by Railway

### nixpacks.toml
```toml
[phases.setup]
nixPkgs = ["python312"]

[phases.install]
cmds = ["pip install -r requirements.txt"]

[start]
cmd = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
```
- Configures the build process
- Specifies Python version
- Defines install and start commands

### railway.json
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```
- Specifies Nixpacks as the builder
- Configures automatic restart on failure

## Monitoring and Logs

### View Logs
In Railway dashboard:
1. Select your project
2. Click on "Logs" tab
3. View real-time application logs

### Monitor Performance
Railway provides:
- CPU usage metrics
- Memory usage metrics
- Network usage
- Request metrics

## Common Issues and Solutions

### Issue: Application fails to start
**Solution**: Check that all required environment variables are set correctly:
```bash
railway variables
```

### Issue: Audio files not accessible
**Solution**: Ensure BASE_PUBLIC_URL is set to your Railway deployment URL:
```bash
railway variables set BASE_PUBLIC_URL=https://your-app.railway.app
```

### Issue: WebSocket connection fails
**Solution**: Verify your client is connecting to the correct WebSocket URL:
```
wss://your-app.railway.app/ws/voice
```

### Issue: Port binding error
**Solution**: Railway automatically sets the PORT variable. Don't override it manually.

## Updating Your Deployment

Railway automatically deploys when you push to your connected GitHub branch:

```bash
git add .
git commit -m "Update feature"
git push origin main
```

Railway will:
1. Detect the push
2. Build the new version
3. Deploy with zero downtime
4. Rollback automatically if health checks fail

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `GEMINI_API_KEY` | Yes | Google Gemini API key | `AIza...` |
| `ELEVENLABS_API_KEY` | Yes | ElevenLabs API key | `sk_...` |
| `ELEVENLABS_VOICE_ID` | Yes | ElevenLabs voice ID | `21m00...` |
| `BASE_PUBLIC_URL` | Yes | Your Railway deployment URL | `https://app.railway.app` |
| `PORT` | No | Auto-set by Railway | `8000` |
| `SUPABASE_URL` | No | Supabase project URL | `https://xyz.supabase.co` |
| `SUPABASE_KEY` | No | Supabase API key | `eyJh...` |

## Cost Estimation

Railway pricing (as of 2024):
- **Free tier**: $5 of usage per month
- **Pro plan**: $20/month + usage
- Typical usage for this app: ~$0.10-0.50/day depending on traffic

## Support

For Railway-specific issues:
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway

For application issues:
- Check application logs in Railway
- Review GitHub Issues
- Contact repository maintainers

## Next Steps

After deploying:
1. ✅ Test the health endpoint
2. ✅ Test WebSocket connection
3. ✅ Monitor logs for errors
4. ✅ Set up custom domain (optional)
5. ✅ Configure monitoring alerts (optional)

Happy deploying! 🚀

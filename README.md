# West Midlands Multibank - Booking System

A simple slot booking system for the West Midlands Multibank collection service.

## Project Structure

```
multibank-booking/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── models.py           # Database models (coming soon)
├── frontend/
│   └── index.html          # Web interface
└── README.md               # This file
```

## Local Development Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Server

```bash
# From the backend directory
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

### 3. View the App

- **API Root**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs (automatic Swagger docs)
- **Frontend**: http://127.0.0.1:8000/app
- **Slots API**: http://127.0.0.1:8000/api/slots
- **Stock API**: http://127.0.0.1:8000/api/stock

## Deployment

### Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Railway will automatically detect it's a Python app and deploy

### Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect this repository
5. Use these settings:
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

## Current Features

✅ View available booking slots
✅ See current stock availability
✅ Mobile-responsive interface
✅ Clean API with automatic documentation

## Coming Soon

- 📝 Booking form with partner name and reference
- 💾 SQLite database for real data storage
- 📧 Email confirmations
- 🔐 Admin dashboard for warehouse staff
- 📊 Booking history and reporting

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Plain HTML/CSS/JavaScript (no framework needed)
- **Database**: SQLite → PostgreSQL (migration path ready)
- **Hosting**: Railway or Render (free tier)

## Contact

Built for West Midlands Multibank by WhatsOn.Agency

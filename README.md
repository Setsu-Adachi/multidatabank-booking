# Multidatabank - Booking System

A simple slot booking system for the West Midlands Multibank collection service.
**[📱 View Design Mockup](docs/multidatabank-glide-mockup.html)** - See the complete visual design for the Glide app

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

## Deployment Options

### Glide App (Recommended - No Code Required)

Build a no-code mobile app using Glide that connects to your Google Sheets:

1. Go to [glideapps.com](https://glideapps.com)
2. Sign up with your Google account
3. Create "New App from Google Sheets"
4. Connect your Multibank booking spreadsheet
5. Configure partner booking interface and admin dashboard
6. Publish and share with partners

**Cost:** Free tier available, £25/month for premium features
**Best for:** Quick deployment with existing Google Sheets workflow

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

**Recommended: Glide No-Code App**
- **Frontend**: Glide mobile app builder
- **Database**: Google Sheets (existing workflow)
- **Hosting**: Glide platform (free/paid tier)

**Alternative: Custom Python Backend**
- **Backend**: FastAPI (Python)
- **Frontend**: Plain HTML/CSS/JavaScript (no framework needed)
- **Database**: SQLite → PostgreSQL (migration path ready)
- **Hosting**: Railway or Render (free tier)

## Contact

Built for Multidatabank by WhatsOn.Agency

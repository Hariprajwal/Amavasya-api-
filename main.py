from fastapi import FastAPI
from datetime import datetime
from amavasya import is_amavasya, get_amavasya_dates, next_amavasya
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Amavasya API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Amavasya API running"}


@app.get("/amavasya/today")
def today():

    today = datetime.now()

    return {
        "date": today.strftime("%Y-%m-%d"),
        "is_amavasya": is_amavasya(today.date())
    }


@app.get("/amavasya/next")
def next_amav():

    data = next_amavasya()

    return {
        "date": data["date"].strftime("%Y-%m-%d"),
        "days_until": data["days_until"],
        "about": data["about"]
    }


@app.get("/amavasya/year/{year}")
def amavasya_year(year: int):

    dates = get_amavasya_dates(year)

    return {
        "year": year,
        "total": len(dates),
        "dates": [
            {
                "date": d["date"].strftime("%Y-%m-%d"),
                "about": d["about"]
            }
            for d in dates
        ]
    }


@app.get("/amavasya/check/{date}")
def check_date(date: str):

    dt = datetime.strptime(date, "%Y-%m-%d")

    return {
        "date": date,
        "is_amavasya": is_amavasya(dt.date())
    }
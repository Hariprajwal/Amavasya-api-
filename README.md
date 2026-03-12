# Amavasya-api-
# 🌑 Amavasya API

A lightweight **public API to calculate Amavasya (New Moon) dates according to the Hindu Panchang system** using astronomical calculations.

This project computes Amavasya based on **Sun–Moon angular difference (Tithi calculation)** and determines the observance day according to traditional Hindu calendar rules.

It provides endpoints to check:

- If today is Amavasya
- The next upcoming Amavasya
- All Amavasya dates for a specific year
- Whether a specific date is Amavasya

---

# 🔗 Live Links

### 🌐 API
https://amavasya-api.onrender.com/

### 🖥️ Web Interface
https://amavasya.vercel.app/

---

# ✨ Features

- 🌑 Accurate Amavasya calculation using **astronomical math**
- 📅 Full year Amavasya calendar
- 🔍 Check Amavasya for any date
- ⏳ Find next upcoming Amavasya
- 🕉️ Includes **short spiritual descriptions**
- ⚡ Fast REST API
- 🌍 Public and free to use

---

# 🧠 How the Calculation Works

In the Hindu calendar, **Amavasya corresponds to the 30th Tithi**.

A Tithi is determined by the angular difference between the **Moon and Sun**.

```
Angle = (Moon Longitude − Sun Longitude) % 360
```

Each Tithi spans **12 degrees**.

| Tithi | Angle Range |
|------|-------------|
| 29 (Chaturdashi) | 336° – 348° |
| **30 (Amavasya)** | **348° – 360°** |

The **Amavasya observance day** is defined as:

> The day when the Amavasya tithi is present at **sunrise**.

Astronomical calculations are performed using:

- **Swiss Ephemeris**
- Python
- FastAPI backend

---

# 📡 API Endpoints

## 1️⃣ Check Today

```
GET /amavasya/today
```

Example:

```
https://amavasya-api.onrender.com/amavasya/today
```

Response:

```json
{
  "date": "2026-03-18",
  "is_amavasya": false
}
```

---

## 2️⃣ Next Amavasya

```
GET /amavasya/next
```

Example:

```
https://amavasya-api.onrender.com/amavasya/next
```

Response:

```json
{
  "date": "2026-04-17",
  "days_until": 29,
  "about": "Vaishakha Amavasya – important for prayers and charity."
}
```

---

## 3️⃣ Full Year Calendar

```
GET /amavasya/year/{year}
```

Example:

```
https://amavasya-api.onrender.com/amavasya/year/2026
```

Response:

```json
{
 "year": 2026,
 "total": 12,
 "dates": [
  {
   "date": "2026-01-18",
   "about": "Magha Amavasya – auspicious for holy baths and charity."
  },
  {
   "date": "2026-02-16",
   "about": "Phalguna Amavasya – spiritual cleansing before Holi."
  }
 ]
}
```

---

## 4️⃣ Check Specific Date

```
GET /amavasya/check/{date}
```

Example:

```
https://amavasya-api.onrender.com/amavasya/check/2026-03-18
```

Response:

```json
{
 "date": "2026-03-18",
 "is_amavasya": true
}
```

---

# 🧪 Interactive API Docs

FastAPI automatically provides a testing interface:

```
https://amavasya-api.onrender.com/docs
```

You can test every endpoint directly from the browser.

---

# 🛠 Tech Stack

- **Python**
- **FastAPI**
- **Swiss Ephemeris**
- **Pytz**
- **Render (Deployment)**
- **Vercel (Frontend)**

---

# 📂 Project Structure

```
amavasya-api
│
├── main.py          # API server
├── amavasya.py      # astronomical calculations
├── requirements.txt
└── README.md
```

---

# 🌍 Possible Integrations

This API can be integrated with:

- Telegram bots
- Calendar apps
- Panchang apps
- Reminder services
- Religious event trackers
- Spiritual mobile apps

---

# 🚀 Future Improvements

Planned additions:

- Ekadashi API integration
- Purnima calculation
- Full Hindu Panchang API
- Festival calendar endpoints
- Multi-timezone calculations

---

# 🧑‍💻 Author

Hari Prajwal

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository  
🔗 Share it with others  
🚀 Build something using the API

---

🕉️ *May this tool help people stay connected with sacred lunar traditions.*

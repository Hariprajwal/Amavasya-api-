import swisseph as swe
from datetime import datetime, timedelta
import pytz

IST = pytz.timezone("Asia/Kolkata")

# Short descriptions for Amavasya months
AMAVASYA_INFO = {
    1: "Magha Amavasya – considered very auspicious for charity and holy baths.",
    2: "Phalguna Amavasya – associated with spiritual cleansing before Holi.",
    3: "Chaitra Amavasya – beginning of new lunar spiritual cycles.",
    4: "Vaishakha Amavasya – important for prayers and charity.",
    5: "Jyeshtha Amavasya – Vat Savitri fasting observed by many devotees.",
    6: "Ashadha Amavasya – devoted to ancestors and spiritual reflection.",
    7: "Shravana Amavasya – sacred during the holy month of Shravan.",
    8: "Bhadrapada Amavasya – connected with Pitru rituals.",
    9: "Ashwin Amavasya – known as Mahalaya Amavasya for ancestor offerings.",
    10: "Kartika Amavasya – Diwali Amavasya, one of the most sacred nights.",
    11: "Margashirsha Amavasya – prayers for peace and prosperity.",
    12: "Pausha Amavasya – considered ideal for spiritual introspection."
}


def get_tithi(dt):
    utc = dt.astimezone(pytz.UTC)

    jd = swe.julday(
        utc.year,
        utc.month,
        utc.day,
        utc.hour + utc.minute / 60
    )

    sun = swe.calc_ut(jd, swe.SUN)[0][0]
    moon = swe.calc_ut(jd, swe.MOON)[0][0]

    angle = (moon - sun) % 360

    return int(angle / 12) + 1


def is_amavasya(date):

    sunrise = IST.localize(
        datetime(date.year, date.month, date.day, 6, 0)
    )

    tithi = get_tithi(sunrise)

    return tithi == 30


def get_amavasya_dates(year):

    results = []

    current = datetime(year, 1, 1).date()
    end = datetime(year, 12, 31).date()

    while current <= end:

        if is_amavasya(current):

            results.append({
                "date": current,
                "about": AMAVASYA_INFO.get(current.month, "Sacred new moon day for reflection and prayer.")
            })

        current += timedelta(days=1)

    return results


def next_amavasya():

    today = datetime.now(IST).date()

    for i in range(60):

        check = today + timedelta(days=i)

        if is_amavasya(check):

            return {
                "date": check,
                "days_until": (check - today).days,
                "about": AMAVASYA_INFO.get(check.month)
            }

    return None
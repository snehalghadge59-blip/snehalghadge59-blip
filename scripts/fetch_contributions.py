import os
import json
import re
import requests
from bs4 import BeautifulSoup

USERNAME = "snehalghadge59-blip"
URL = f"https://github.com/users/{USERNAME}/contributions"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_contributions():
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch contributions HTML: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    days = []
    
    # Map for Tooltips if present
    tooltips = {}
    for tt in soup.find_all("tool-tip"):
        target_id = tt.get("for")
        if target_id:
            tooltips[target_id] = tt.get_text().strip()
    
    # Parse days
    day_tds = soup.find_all("td", class_="ContributionCalendar-day")
    
    for td in day_tds:
        date_str = td.get("data-date")
        if not date_str:
            continue
            
        level = int(td.get("data-level", 0))
        td_id = td.get("id", "")
        
        count = 0
        tooltip_text = tooltips.get(td_id, "")
        
        # Try extracting count from tooltip or aria-label
        if tooltip_text:
            match = re.search(r"(\d+)\s+contribution", tooltip_text)
            if match:
                count = int(match.group(1))
        elif td.get("aria-label"):
            match = re.search(r"(\d+)\s+contribution", td.get("aria-label"))
            if match:
                count = int(match.group(1))
        elif level > 0:
            # Fallback estimation if count text isn't parsed
            count = level * 2

        days.append({
            "date": date_str,
            "count": count,
            "level": level
        })

    # Sort days by date
    days.sort(key=lambda d: d["date"])

    # Calculate streaks and stats
    total_contributions = sum(d["count"] for d in days)
    
    best_day_count = 0
    best_day_date = ""
    for d in days:
        if d["count"] > best_day_count:
            best_day_count = d["count"]
            best_day_date = d["date"]
            
    # Calculate streak
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    
    for d in days:
        if d["count"] > 0 or d["level"] > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
    # Reverse to find current streak from latest date back
    for d in reversed(days):
        if d["count"] > 0 or d["level"] > 0:
            current_streak += 1
        else:
            break

    data = {
        "username": USERNAME,
        "total_contributions": total_contributions,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": {
            "date": best_day_date,
            "count": best_day_count
        },
        "days": days
    }

    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully scraped {len(days)} days with {total_contributions} total contributions!")

if __name__ == "__main__":
    fetch_contributions()

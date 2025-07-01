import requests #use snake case 3mar
from tabulate import tabulate

def getLog(log_id, username=None):
    #find and print
    url = f"https://logs.tf/api/v1/log/{log_id}"
    resp = requests.get(url, timeout=5)
    if resp.status_code != 200:
        print(f"eror: HTTP {resp.status_code}") #200 success
        return

    payload = resp.json()
    data = payload.get("log", payload)

    #read scores
    blu_score = data["teams"]["Blue"]["score"]


    red_score = data["teams"]["Red"]["score"]



    #makes rows


    rows = []
    for steamid, stats in data["players"].items():
        disp_name = data["names"].get(steamid, "<unknown>")


        if username and disp_name.lower() != username.lower():
            continue

        team = {2: "BLU", 3: "RED"}.get(stats.get("team"), stats.get("team"))
        rows.append([
            team,
            disp_name,
            stats.get("kills", 0),
            stats.get("assists", 0),
            stats.get("deaths", 0),
            stats.get("dmg", 0),
            stats.get("dpm", 0), #i know its less clean like this but it helps me see
            stats.get("dt",  0),
            stats.get("dtpm", 0),
            stats.get("cpc", 0),          #gets
            stats.get("headshots", 0),    # headshots
        ])

    if not rows:
        msg = f"error for this log, log:{log_id}"
        if username:
            msg += f" matching user “{username}”." #not likely tbh but failcase cant hurt

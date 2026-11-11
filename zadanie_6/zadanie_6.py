from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://www.mimuw.edu.pl/"
dzisiaj = requests.get(url + "pl/wydarzenia/current-date/").json()["current_date"]
adres = (
    f"{url}pl/wydarzenia/events/?init_date={dzisiaj}"
    "&start_offset=0&end_offset=11&query_type=A"
)
odpowiedz = requests.get(adres).json()

wydarzenia = []
for wydarzenie in odpowiedz["events"]:
    pola = {pole["label"]: pole for pole in wydarzenie["data"]}
    tytul = pola.get("Tytuł", pola["main_title"])
    link = tytul["link"] or pola.get("Seminarium", {}).get("link") or url
    termin = pola["Od"]["text"].split()

    wydarzenia.append({
        "tytuł": BeautifulSoup(tytul["text"], "html.parser").get_text(" ", strip=True),
        "url": urljoin(url, link),
        "data": termin[0],
        "godzina": termin[1] if len(termin) > 1 else "",
    })

dane = pd.DataFrame.from_dict(wydarzenia)
dane.to_csv(Path(__file__).with_name("wydarzenia.csv"), index=False)
print(dane.sample(5)[["tytuł", "url", "data"]].to_string(index=False))

import requests

def get_lines(author):
    url = f"https://poetrydb.org/author/{author}/lines.json"
    yanit = requests.get(url)
    if yanit.status_code == 200:
        lines = yanit.json()
        print(lines)
    else:
        print("Hata:", yanit.status_code)


get_lines("Percy Bysshe Shelley")

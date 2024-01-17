#%%
import json
import urllib.parse
from pathlib import Path

docs = Path("docs")
audio = docs / "audio"
baseURL = "https://yongfu.name/formcorpFulltextAudio/audio/"

# Map filename to url
m = {}
for fp in audio.glob("*"):
    url = baseURL + urllib.parse.quote(fp.name)
    m[fp.name] = url

# Write docs/map.json
with open(docs / "map.json", "w", encoding="UTF-8") as f:
    json.dump(m, f, ensure_ascii=False, indent=4)

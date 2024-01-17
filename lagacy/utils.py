#%%
import os
import json
import pathlib
import requests
from pydub import AudioSegment


def split_audio(start, end, fp, outdir: pathlib.Path):
    try:
        audio = AudioSegment.from_file(fp, format="mp3")
        s, e = start*1000, end*1000
        audio[s:e].export(outdir / os.path.basename(fp), format="mp3")
    except:
        print(f"Failed with audio {fp}, {start}, {end}")


def get_doc(fp):
    base_url = 'https://yongfu.name/glossParser'
    path = requests.utils.quote(fp)
    url = f"{base_url}/{path}.json"
    resp = requests.get(url)
    if str(resp.status_code).startswith("2"):
        return json.loads(resp.content)
    raise Exception(f"Request failed with {resp.status_code} ({url})")


def get_audio_range(doc):
    first, last = None, None
    use_dft = [True, True]

    idx1 = 0
    while first is None:
        idx1 += 1
        first = doc["glosses"][idx1][1]['iu_a_span'][idx1]
    idx2 = -1
    while last is None:
        idx2 -= 1
        last = doc["glosses"][idx2][1]['iu_a_span'][idx2]
    
    if idx1 != 1:
        print(f"Warning: use {idx1} IU for start time")
    if idx2 != -2:
        print(f"Warning: use {idx2} IU for end time")
    
    return first, last



#%% Test
# fp = 'videos/SaiNr-holiday_kalaeh a _oemaw.mp3'
# audio = AudioSegment.from_file(fp, format="mp3")

# audio.export("SaiNr-holiday_kalaeh a _oemaw.mp3", format="mp3")

import json

with open("SaiNr-holiday_kalaeh a _oemaw.json") as f:
    d = json.load(f)


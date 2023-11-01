#%%
import os
import json
import pathlib
import requests
from tqdm import tqdm
from utils import *

AUDIO = pathlib.Path('videos/')
TEMP = pathlib.Path('ignore/')
OUTDIR = pathlib.Path('docs/')

## Get audio files & full text JSON paths
url = 'https://yongfu.name/glossParser/all_lang.json'
resp = requests.get(url)
data = json.loads(resp.content)

audio_files = { (x['meta']['video'], x['file']) for x in data if 'video' in x['meta'] and x['meta']['video'] != 'None' }
audio_files = list(audio_files)
exists = [ x for x in audio_files if (AUDIO / x[0]).exists() ]
no_exists = [ x for x in audio_files if not (AUDIO / x[0]).exists() ]

#%%
for fn_mp3, fp_json in tqdm(exists):
    if (TEMP / fn_mp3).exists(): continue
    doc = get_doc(fp_json)
    audio_cut_rng = get_audio_range(doc)
    split_audio(*audio_cut_rng, AUDIO / fn_mp3, outdir=TEMP)

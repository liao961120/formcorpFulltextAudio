Full Text Audio
===============

As of 2023/11/01, NTU Formosan Corpus only has full text audio files for stories. Hence, this repo needs updating (according to the current status) only when there are newly annotated text.grid files and audio files (which needs splitting).

The main purpose of this repo is to serve the map (`docs/map.json`) between full text audio links (hosted on Google Drive) and the corresponding full text filenames for  <https://corpus.linguistics.ntu.edu.tw>. To do so, simply [download](https://drive.google.com/file/d/1aMM_68YsbiwvQsxKEVwLqXGWDJOyWmvm/view?usp=sharing) and extract `form-corp-data.json.zip` (password-protected) and then execute:

```bash
python google_api.py
```

#%%
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build


def main():
    # Setup GDrive API
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = 'form-corp-data.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=credentials)
    drive = Drive(drive_service)


    audio_files = drive.list_all_children()
    files = {}
    for file in audio_files:
        nm =  file['name']
        url = f'https://drive.google.com/uc?export=open&id={file["id"]}'
        files[nm] = url

    with open("docs/map.json", "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False, indent=True)
    
    print(f"Saved {len(audio_files)} audio filename map (docs/map.json).")


# https://github.com/lopentu/keke/blob/master/dialogue/chatai/bin/download_data.py
class Drive():

    def __init__(self, service):
        self.service = service
        self.folders = {}  # {id: {id, name, parents, modifiedTime} }
        self.file_content = {}  # {id: content}
        self.id = '1gjrp6x6Gh9Gi1Q31A6dCV3cbbsnpDnc1'

    
    def list_all_children(self):
        all_audio, next_page = self.list_child(self.id)
        while next_page != "":
            audio, next_page = self.list_child(self.id, next_page)
            all_audio += audio
        
        return all_audio

    def list_child(self, id_, pageToken=""):
        q = f"'{id_}' in parents"
        resp = self.service.files().list(q=q,
                                    spaces='drive',
                                    corpora='allDrives',
                                    fields='nextPageToken, files(id, name, mimeType)',
                                    includeItemsFromAllDrives=True,
                                    supportsAllDrives=True,
                                    pageToken=pageToken).execute()

        return resp.get('files', []), resp.get('nextPageToken', "")



if __name__ == "__main__":
    main()
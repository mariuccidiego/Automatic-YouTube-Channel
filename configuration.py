import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'Upload Testing',
        'description': 'Hello World Description',
        'tags': ['Travel', 'video test', 'Travel Tips']
    },
    'status': {
        'privacyStatus': 'public',
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('ciao.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

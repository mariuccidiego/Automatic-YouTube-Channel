import os
import datetime
import time
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

video_folder_path = 'video'
upload_times = ["12:00:00", "14:00:00", "16:00:00", "18:00:00", "20:00:00", "21:00:00"]
time_tolerance = datetime.timedelta(minutes=5)
min_upload_interval = datetime.timedelta(minutes=10)

last_uploaded_filename = 'last_uploaded.txt'
if os.path.exists(last_uploaded_filename):
    with open(last_uploaded_filename, 'r') as f:
        last_uploaded_number = int(f.read())
else:
    last_uploaded_number = 0

while True:
    try:
        current_time = datetime.datetime.now().time()
        print(f"Current time: {current_time}")

        for upload_time in upload_times:
            target_time = datetime.datetime.strptime(upload_time, "%H:%M:%S").time()

            start_time = datetime.datetime.combine(datetime.datetime.now().date(), target_time) - time_tolerance
            end_time = datetime.datetime.combine(datetime.datetime.now().date(), target_time) + time_tolerance

            print(f"Checking upload window for time: {target_time}")

            if start_time.time() <= current_time <= end_time.time():
                video_files = [f for f in os.listdir(video_folder_path) if f.endswith(".mp4")]

                if video_files:
                    next_video_number = last_uploaded_number + 1
                    next_video_filename = f"{next_video_number}.mp4"

                    if next_video_filename in video_files:
                        video_path = os.path.join(video_folder_path, next_video_filename)

                        upload_date_time = datetime.datetime.now().replace(
                            hour=target_time.hour, minute=target_time.minute, second=target_time.second
                        ).isoformat() + '.000Z'

                        video_title = f"Meme found on internet #{next_video_number} #trend #tiktok #edit #shorts #trending #meme #fyp #cool #funny #memes"
                        video_description = video_title
                        video_category = 42
                        video_tags = ["meme", "shorts", "tiktok"]

                        print("Uploading video...")
                        request_body = {
                            'snippet': {
                                'categoryI': video_category,
                                'title': video_title,
                                'description': video_description,
                                'tags': video_tags
                            },
                            'status': {
                                'privacyStatus': 'public',
                                'selfDeclaredMadeForKids': False,
                            },
                            'notifySubscribers': False
                        }

                        mediaFile = MediaFileUpload(video_path)

                        try:
                            response_upload = service.videos().insert(
                                part='snippet,status',
                                body=request_body,
                                media_body=mediaFile
                            ).execute()

                            print(f"Uploaded {next_video_filename} at {upload_date_time}")

                            last_uploaded_number = next_video_number
                            with open(last_uploaded_filename, 'w') as f:
                                f.write(str(last_uploaded_number))

                            print("Sleeping for the minimum upload interval...")
                            time.sleep(min_upload_interval.total_seconds())
                            print("Resuming...")

                        except HttpError as http_error:
                            print(f"HTTP Error occurred: {http_error}")

        print("Sleeping for a minute before checking again...")
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")

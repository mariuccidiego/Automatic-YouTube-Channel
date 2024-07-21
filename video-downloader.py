import os
import csv
from pytube import YouTube

def DownloadVideosFromCSV():
    csv_file = "meme.csv"

    if not os.path.exists('video'):
        os.makedirs('video')

    existing_files = [filename.split('.')[0] for filename in os.listdir('video') if filename.endswith('.mp4')]
    existing_indices = [int(index) for index in existing_files if index.isdigit()]
    
    if existing_indices:
        start_index = max(existing_indices) + 1
    else:
        start_index = 1

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            video_id = row['ID']
            full_link = f'https://www.youtube.com/watch?v={video_id}'
            filename = f"{start_index}.mp4"
            try:
                video = YouTube(full_link)
                video.streams.get_highest_resolution().download(output_path='video', filename=filename)
                print(f"Downloaded: {filename}")
                start_index += 1
            except:
                print(f"Failed to download: {full_link}")

def main():
    DownloadVideosFromCSV()

if __name__ == "__main__":
    main()

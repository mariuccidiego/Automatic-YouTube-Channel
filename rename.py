import os

def rename_videos(folder_path):
    video_files = [f for f in os.listdir(folder_path) if f.endswith(".mp4")]
    
    # Extract numbers from filenames and sort them
    sorted_files = sorted(video_files, key=lambda x: int(os.path.splitext(x)[0]))

    for index, filename in enumerate(sorted_files, start=1):
        new_filename = f"{index}.mp4"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

    print("Renaming completed successfully.")

if __name__ == "__main__":
    folder_path = "video"  # Replace with the actual path to your folder
    rename_videos(folder_path)

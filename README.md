# Automatic YouTube Channel

## Overview
**Automatic YouTube Channel** is a Python-based project that automates the process of downloading videos from YouTube and uploading them to a YouTube channel. This tool utilizes the `pytube` library for downloading videos and the YouTube Data API for uploading them.

## Features
- Download videos from YouTube using a CSV file containing video IDs.
- Organize downloaded videos in a structured directory.
- Upload videos automatically to a YouTube channel.
- Configure upload settings such as title, description, tags, and privacy status.

## Requirements
To run this project, ensure you have the following installed:
- Python 3.x
- `pytube`
- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `google-api-python-client`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/mariuccidiego/Automatic-YouTube-Channel.git
   cd Automatic-YouTube-Channel
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up Google API credentials:
   - Create a project in Google Cloud Console.
   - Enable YouTube Data API v3.
   - Generate `credentials.json` and place it in the project root.

## Usage
### Download Videos
- Place a CSV file (e.g., `meme.csv`) in the root directory with a column named `ID`, containing YouTube video IDs.
- Run the script to download videos:
  ```sh
  python video-downloader.py
  ```

### Upload Videos
- Ensure `credentials.json` is set up.
- Modify `configuration.py` to adjust upload settings such as title, description, and tags.
- Run the upload script:
  ```sh
  python configuration.py
  ```

## Configuration
Modify `configuration.py` to change upload settings:
- `title`: Title of the uploaded video.
- `description`: Description of the uploaded video.
- `tags`: List of tags for better discoverability.
- `privacyStatus`: Public, Private, or Unlisted.

## License
This project is open-source and available under the MIT License.

## Author
Developed by [mariuccidiego](https://github.com/mariuccidiego). Contributions and feedback are welcome!


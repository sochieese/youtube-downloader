# YouTube Downloader  <img src="https://cdn.discordapp.com/emojis/1048110912084656148.png" width="30px">

This is a YouTube downloader tool that allows you to download videos from YouTube. It provides a simple and straightforward way to save YouTube videos locally.

## 😸 Packages Used
- [yt-dlp](https://pypi.org/project/yt-dlp/): A Python library for downloading YouTube videos.
- [ffmpeg](https://ffmpeg.org/): A multimedia framework used for merging audio and video.

## Installation
To use this tool, you need to have Python and FFmpeg installed on your machine. Then, follow these steps:
1. Clone this repository to your local machine.
2. Install the required Python packages using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Ensure FFmpeg is installed and added to your system's PATH. You can download FFmpeg from [here](https://ffmpeg.org/download.html).

## Configuration
Before using the tool, you need to provide a configuration file (`config.json`) with the video ID of the YouTube video you want to download. Here's an example of the `config.json` file:

```json
{
    "Youtube_id": "PPnZs0Gnf5I",
    "quality": "2160p",
    "video_name": "see-through"
}
```
- `Youtube_id`: The video ID from the YouTube URL (e.g., `JsOOis4bBFg` from `https://www.youtube.com/watch?v=JsOOis4bBFg`).
- `quality`: The desired video resolution (e.g., `1080p`).
- `video_name`: The name of the output video file.

## Usage
Once you have set up the configuration file, run the following command to start the download:
```
python main.py
```

The tool will:
1. Download the audio and video streams separately.
2. Save the files in a folder named `PARTS` in the same directory as the script.
3. Merge the audio and video into a single file using FFmpeg.

## Playing the Downloaded Video
We recommend using [VLC Media Player](https://www.videolan.org/vlc/) to play the downloaded videos. VLC supports a wide range of audio and video codecs, ensuring compatibility with the downloaded files.

## Visitors

![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=sochieese.youtube-downloader)


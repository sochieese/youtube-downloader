# YouTube Downloader  <img src="https://cdn.discordapp.com/emojis/1048110912084656148.png" width="30px">

This is a YouTube downloader tool that allows you to download videos from YouTube. It provides a simple and straightforward way to save YouTube videos locally.

## 😸 Packages Used
- [pytube](https://pypi.org/project/pytube/): A Python library for downloading YouTube videos.
- [ffmpeg-python](https://pypi.org/project/ffmpeg-python/): An HTML5 library used for video processing.

## Installation
To use this tool, you need to have Python installed on your machine. Then, follow these steps:
1. Clone this repository to your local machine.
2. Install the required packages using the following command: 
```
pip install -r requirements.txt
```
## Configuration
Before using the tool, you need to provide a configuration file (`config.json`) with the video ID of the YouTube video you want to download. Here's an example of the `config.json` file:

```json
{
    "Youtube_id": "JsOOis4bBFg",
    "quality": "1080p", 
    "video_name": "S-Class" 
}
```
Please note that the video ID can be found in the YouTube URL (e.g., https://www.youtube.com/watch?v=JsOOis4bBFg). Also, keep in mind that some quality types may not work for certain videos due to limitations.

## Usage
Once you have set up the configuration file, run the following command to start the download:
```
python main.py
```
## Visitors

![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=sochieese.youtube-downloader)


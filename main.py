import os
import yt_dlp
import json
import subprocess
from typing import TypedDict, List

class Config(TypedDict):
    youtube_id: str
    video_name: str
    quality: str

class YDLOptions(TypedDict):
    format: str
    quiet: bool
    no_warnings: bool
    merge_output_format: str

class Format(TypedDict):
    format_id: str
    url: str
    height: int
    vcodec: str

class VideoInfo(TypedDict):
    url: str
    formats: List[Format]

def download_video(config: Config, audio_opts: YDLOptions, video_opts: YDLOptions) -> None:
    video_url = f'https://www.youtube.com/watch?v={config["youtube_id"]}'
    target_height = int(config["quality"].replace('p', ''))

    with yt_dlp.YoutubeDL(audio_opts) as ydl_audio, yt_dlp.YoutubeDL(video_opts) as ydl_video:
        info_audio: VideoInfo = ydl_audio.extract_info(video_url, download=False)
        info_video: VideoInfo = ydl_video.extract_info(video_url, download=False)
        
        audio_url = info_audio['url']
        video_url = next(
            (fmt['url'] for fmt in info_video['formats'] if fmt.get('vcodec') != 'none' and fmt.get('height') == target_height),
            None
        )

        if not video_url:
            print("No suitable video format found.")
            return

    parts_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parts")
    os.makedirs(parts_directory, exist_ok=True)

    audio_output_path = os.path.join(parts_directory, f"{config['video_name']}_audio.webm")
    video_output_path = os.path.join(parts_directory, f"{config['video_name']}_video.mp4")
    final_output_path = os.path.join(parts_directory, f"{config['video_name']}.mp4")

    audio_opts['outtmpl'] = audio_output_path
    video_opts['outtmpl'] = video_output_path

    with yt_dlp.YoutubeDL(audio_opts) as ydl_audio:
        ydl_audio.download([audio_url])

    with yt_dlp.YoutubeDL(video_opts) as ydl_video:
        ydl_video.download([video_url])

    subprocess.run([
        "ffmpeg", "-i", video_output_path,
        "-i", audio_output_path,
        "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", final_output_path
    ])

if __name__ == "__main__":
    with open("config.json") as file:
        config = json.load(file)

    audio_options = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "merge_output_format": "webm",
    }
    video_options = {
        "format": "bestvideo/best",
        "quiet": True,
        "no_warnings": True,
        "merge_output_format": "mp4",
    }

    download_video(config, audio_options, video_options)


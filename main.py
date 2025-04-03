import os
import yt_dlp
import json
import subprocess

with open("config.json") as f:
    config = json.load(f)

url = f'https://www.youtube.com/watch?v={config["Youtube_id"]}'

ydl_opts_audio = {
    'format': 'bestaudio/best',
    'quiet': True,
}
ydl_opts_video = {
    'quiet': True,
    'no_warnings': True,
    'format': 'bestvideo/best',
    'merge_output_format': 'mp4',
}

with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl_audio, yt_dlp.YoutubeDL(ydl_opts_video) as ydl_video:
    info_audio = ydl_audio.extract_info(url, download=False)
    info_video = ydl_video.extract_info(url, download=False)
    audio_url = info_audio['url']
    target_height = int(config['quality'].replace('p', ''))

    video_url = None
    for fmt in info_video['formats']:
        if fmt.get('vcodec') != 'none' and fmt.get('height') == target_height:
            video_url = fmt['url']
            break

    if not video_url:
        print("No suitable video format found.")
        exit(1)

script_dir = os.path.dirname(os.path.abspath(__file__))
parts_dir = os.path.join(script_dir, "parts")
os.makedirs(parts_dir, exist_ok=True)

audio_output = os.path.join(parts_dir, f"{config['video_name']}_audio.%(ext)s")
video_output = os.path.join(parts_dir, f"{config['video_name']}_video.%(ext)s")

ydl_opts_audio['outtmpl'] = audio_output
ydl_opts_video['outtmpl'] = video_output

with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl_audio:
    ydl_audio.download([audio_url])

with yt_dlp.YoutubeDL(ydl_opts_video) as ydl_video:
    ydl_video.download([video_url])

final_video_output = video_output.replace("%(ext)s", "mp4")
final_audio_output = audio_output.replace("%(ext)s", "webm")
final_output = os.path.join(script_dir, f"{config['video_name']}.mp4")

subprocess.run([
    "ffmpeg", "-i", final_video_output,
    "-i", final_audio_output,
    "-c", "copy", final_output
])



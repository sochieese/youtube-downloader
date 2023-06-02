import os
import ffmpeg
import pytube
import json
import subprocess    

with open("config.json") as f:
    config = json.load(f)

video = pytube.YouTube(f'https://www.youtube.com/watch?v={config["Youtube_id"]}', use_oauth=True, allow_oauth_cache=True)
Streams = video.streams
highresvid = Streams.filter(res = f"{config['quality']}", file_extension = 'mp4').first()  

highresvid.download(filename=f"{config['video_name']}_video.mp4")
stream = sorted([stream for stream in video.streams if stream.mime_type.startswith("audio")], key=lambda stream: int(stream.abr[:-4]), reverse=True)[0]
stream.download(filename=f"{config['video_name']}_audio.mp3")
video = f"{config['video_name']}_video.mp4"
audio = f"{config['video_name']}_audio.mp3"
subprocess.run(f"ffmpeg -i {video} -i {audio} -c copy {config['video_name']}.mp4")
#ffmpeg.concat(video, audio, v=1, a=1).output(f'{config["video_name"]}.mp4').run()
os.remove(f"{config['video_name']}_video.mp4")
os.remove(f"{config['video_name']}_audio.mp3")
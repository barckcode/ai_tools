from __future__ import unicode_literals
import yt_dlp
import replicate


# Youtube Process
class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


output_audio_file= 'audio_yt'

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': output_audio_file,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=DkFJE8ZdeG8'])


# Transcription Process
audio = open(f"./{output_audio_file}.mp3", "rb");

input = {
    "audio": audio,
    "batch_size": 64
}

output = replicate.run(
    "vaibhavs10/incredibly-fast-whisper:3ab86df6c8f54c11309d4d1f930ac292bad43ace52d10c80d87eb258b3c9f79c",
    input=input
)

print(output['text'])

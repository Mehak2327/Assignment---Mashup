import sys
import os
from pydub import AudioSegment

def download_videos(singer, n):
    print("Downloading videos...")
    search_query = f"ytsearch{n}:{singer}"
    os.system(f'yt-dlp -x --audio-format mp3 "{search_query}"')

def cut_and_merge(duration, output):
    print("Processing audio files...")
    final = AudioSegment.empty()

    for file in os.listdir():
        if file.endswith(".mp3"):
            audio = AudioSegment.from_mp3(file)
            cut = audio[:duration * 1000]
            final += cut

    final.export(output, format="mp3")

def main():
    if len(sys.argv) != 5:
        print("Usage: python 102303792.py <SingerName> <NumberOfVideos> <Duration> <OutputFile>")
        return

    singer = sys.argv[1]
    n = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4]

    if n <= 10 or duration <= 20:
        print("Number of videos must be >10 and duration >20")
        return

    download_videos(singer, n)
    cut_and_merge(duration, output)

    print("Mashup created successfully:", output)

if __name__ == "__main__":
    main()

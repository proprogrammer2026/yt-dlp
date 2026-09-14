import yt_dlp

text = """
VIDEO
1. MP4
2. MKV
3. WebM

AUDIO
4. MP3
5. M4A
6. Opus
7. FLAC
8. WAV
"""

while True:
    link = input("Enter Link: ")

  while True:
        print(text)

        FileType = input("Enter File type: ")

        if FileType.isdigit():
            FileType = int(FileType)

            if FileType in range(1, 9):
                break
            else:
                print("Invalid Digit")
        else:
            print("Enter Digit")


    if FileType in range(1, 4):

        while True:
            print("""
1 - Best video + best audio
2 - Maximum 2160p (4K)
3 - Maximum 1440p
4 - Maximum 1080p
5 - Maximum 720p
6 - Maximum 480p
7 - Maximum 360p
""")

            Quality = input("Enter Choice: ")

            if Quality.isdigit():
                Quality = int(Quality)

                if Quality in range(1, 8):
                    break
                else:
                    print("Invalid Digit")
            else:
                print("Enter Digit")

        if Quality == 1:
            option = {
                "format": "bestvideo+bestaudio/best"
            }

        elif Quality == 2:
            option = {
                "format": "bestvideo[height<=2160]+bestaudio/best"
            }

        elif Quality == 3:
            option = {
                "format": "bestvideo[height<=1440]+bestaudio/best"
            }

        elif Quality == 4:
            option = {
                "format": "bestvideo[height<=1080]+bestaudio/best"
            }

        elif Quality == 5:
            option = {
                "format": "bestvideo[height<=720]+bestaudio/best"
            }

        elif Quality == 6:
            option = {
                "format": "bestvideo[height<=480]+bestaudio/best"
            }

        elif Quality == 7:
            option = {
                "format": "bestvideo[height<=360]+bestaudio/best"
            }

        if FileType == 1:
            option["merge_output_format"] = "mp4"

        elif FileType == 2:
            option["merge_output_format"] = "mkv"

        elif FileType == 3:
            option["merge_output_format"] = "webm"

    elif FileType == 4:

        option = {
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            }]
        }

    elif FileType == 5:

        option = {
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a"
            }]
        }

    elif FileType == 6:

        option = {
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "opus"
            }]
        }

    elif FileType == 7:

        option = {
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "flac"
            }]
        }

    elif FileType == 8:

        option = {
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav"
            }]
        }


    break



try:
    with yt_dlp.YoutubeDL(option) as ydl:
        ydl.download([link])

except Exception as error:
    print("Download failed:")
    print(error)

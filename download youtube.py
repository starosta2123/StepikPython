# import pytube
# import os
#
# url = 'https://www.youtube.com/watch?v=T2Z6HZaN-tc'
# yt = pytube.YouTube(url)
# stream = yt.streams
# video_480 = stream.filter(res="1080p").desc().first()
# audio_best = stream.filter(adaptive=False, only_audio=True, abr="160kbps").desc().first()
# adress = r'D:\1014'
# video_480.download(adress)
# audio_best.download(adress)
# thisvideo = str(adress) + '\\' + str(yt.title) + ".mp4"
# # thisFile = str(adress) + '\\' + str(yt.title) + ".webm"
#
# ext = '.' + os.path.realpath(thisFile).split('.')[-1:][0]
# mp3file = thisFile.replace(ext, '.mp3')
# os.rename(thisFile, mp3file)

print(yt.title)

import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=T2Z6HZaN-tc'])
# youtube_dl.utils.DownloadError: ERROR: LXb3EKWsInQ: YouTube said: Unable to extract video data

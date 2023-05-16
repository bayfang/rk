from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLYMxvl3JhfZpRjpcDMhlG1xRcEpln0fww')
for video in p.videos:
    print(video.title)
    video.streams.get_highest_resolution().download()

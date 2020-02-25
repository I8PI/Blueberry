from pytube import Playlist
K=input('Provide the playlist link')
playlist = Playlist(K)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.download_all()
input('press enter to exit')
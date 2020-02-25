import pytube
link = input('Provide the Youtube link')
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
print('Download is complete')
input('press enter to exit')
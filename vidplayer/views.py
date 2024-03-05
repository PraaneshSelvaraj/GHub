from django.shortcuts import render
from .utils import Utils

# Create your views here.
def video_player(request):
    utils = Utils()
    videoTitle = request.GET.get("video")
    print(videoTitle)
    # print(utils.get_songs_list(utils.get_songs_path()))
    path = utils.play_song_path(videoTitle)
    print(path)
    return render(request, "vidplayer.html", {"src" : path, "videoTitle": videoTitle})
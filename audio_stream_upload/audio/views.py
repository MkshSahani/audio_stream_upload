from django.shortcuts import render, HttpResponse
from .models import AudioDataUser
from django.utils.timezone import utc
from datetime import datetime

def homePage(request):
    context = {}
    audio_file = AudioDataUser.objects.all()
    audio_file = list(audio_file) # list of audio file.
    audio_file_list = [[audio.audio_title, audio.audio_file] for audio in audio_file]
    context['audio_file_list'] = audio_file_list
    list_of_time_of_upload = [audio.time_of_upload for audio in audio_file] # list of time of upload of audio file.
    recent_upload_at = max(list_of_time_of_upload)
    max_index = list_of_time_of_upload.index(recent_upload_at)
    recentAudioTitle, recentAudioUrl = audio_file[max_index].audio_title, audio_file[max_index].audio_file
    context['recentTitle'] = recentAudioUrl
    context['recentURL'] = recentAudioUrl
    context['ttout'] = 10000
    #context['tout'] = 100
    now = datetime.utcnow().replace(tzinfo=utc)
    timediff = now - recent_upload_at
    important_dat = timediff.total_seconds()
    context['tout'] = important_dat
    return render(request, 'audio/base/base.html', context) # render home page.

def dummy(request):
    return render(request, 'audio/base/home.html')

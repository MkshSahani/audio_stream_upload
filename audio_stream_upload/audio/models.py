from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related 

class AudioDataUser(models.Model): 
    upload_by_user = models.ForeignKey(User, related_name="user_audio", on_delete=models.CASCADE)  
    audio_file_id = models.AutoField(primary_key=True) # audio_file_id_to_recoginize file uniquely 
    time_of_upload = models.DateTimeField(auto_now_add=True) # set date and time of now. 
    audio_title = models.CharField(max_length=120) 
    audio_file = models.URLField()

    def __str__(self): 
        return self.audio_title # title of auido file. 
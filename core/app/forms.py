from django import forms


class VideoIdForm(forms.Form):
    video_id = forms.CharField(label='動画ID')
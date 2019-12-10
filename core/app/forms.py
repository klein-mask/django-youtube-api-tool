from django import forms


class VideoIdForm(forms.Form):
    video_id = forms.CharField(label='動画ID')

class ChannelIdForm(forms.Form):
    channel_id = forms.CharField(label='チャンネルID')

class SortChoiceForm(forms.Form):
	CHOICE = (
		('published', '公開日付'),
		('title', 'タイトル'),
		('view_count', '視聴回数'),
		('like_count', '高評価数'),
		('dislike_count', '低評価数'),
		('like_percent', '高評価率'),
	)

	sort = forms.fields.ChoiceField(required=True,
									choices=CHOICE,
									initial=['published'],
									widget=forms.widgets.Select(attrs={
										'class': 'round',
										'placeholder': 'Sort'
									}))
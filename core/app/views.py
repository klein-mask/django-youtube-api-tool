from django.shortcuts import render
from app.db import MySQLClient
from django.views.generic import TemplateView, ListView
from app.videos import YoutubeAPIClient
from app.forms import VideoIdForm, ChannelIdForm, SortChoiceForm
from django.contrib.auth.models import User
from app.models import Video


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_id_form'] = VideoIdForm()
        context['channel_id_form'] = ChannelIdForm()
        return context

index = IndexView.as_view()


class VideoView(TemplateView):
    template_name = 'app/video.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = VideoIdForm(data=request.POST)
        if form.is_valid():
            video_id = form.cleaned_data.get('video_id')

        context['video_data'] = YoutubeAPIClient().get_video_data(video_id)
        return self.render_to_response(context)

video = VideoView.as_view()


class ChannelView(TemplateView):
    template_name = 'app/channel.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ChannelIdForm(data=request.POST)
        if form.is_valid():
            channel_id = form.cleaned_data.get('channel_id')

        context['videos'] = YoutubeAPIClient().get_video_datas_from_channel(channel_id)
        context['sort_form'] = SortChoiceForm()


        for d in context['videos']:
            u = User.objects.filter(username='klein').first()
            print('型：', type(u))
            Video(id=d.get('video_id'), title=d.get('title'), user=u).save()



        return self.render_to_response(context)
    

channel = ChannelView.as_view()


class VideoListView(ListView):
    template_name = 'app/video_list.html'
    model = Video
    context_object_name = 'videos'

    """
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ChannelIdForm(data=request.POST)
        if form.is_valid():
            channel_id = form.cleaned_data.get('channel_id')

        context['videos'] = YoutubeAPIClient(os.environ.get('YOUTUBE_API_KEY')).get_video_datas_from_channel(channel_id)
        context['sort_form'] = SortChoiceForm()

        return self.render_to_response(context)
    """
video_list = VideoListView.as_view()
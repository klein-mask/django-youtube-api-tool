from django.shortcuts import render
from app.db import MySQLClient
from django.views.generic import TemplateView
from app.videos import YoutubeAPIClient
from app.forms import VideoIdForm
import os

class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_id_form'] = VideoIdForm()
        return context

    """

    def read_all_users(self):
        sql = MySQLClient().open()
        res = sql.exec('select * from test')

        # 性別のフラグを文字にする
        for r in res:
            r['gender_str'] = '男性' if r['gender'] == 1 else '女性'
        print(res)
        return res
    """

index = IndexView.as_view()


class VideoView(TemplateView):
    template_name = 'app/video.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        """
        form = VideoIdForm(data=request.POST)
        if form.is_valid():
            video_id = form.cleaned_data.get('video_id')
            print(video_id)
        print(os.environ.get('YOUTUBE_API_KEY'))
        yac = YoutubeAPIClient(os.environ.get('YOUTUBE_API_KEY'))
        context['video_data'] = yac.get_video_data(video_id)
        """
        yac = YoutubeAPIClient(os.environ.get('YOUTUBE_API_KEY'))
        yac.get_video_datas_from_channel('UCw8ZhLPdQ0u_Y-TLKd61hGA')
        return self.render_to_response(context)

video = VideoView.as_view()
    

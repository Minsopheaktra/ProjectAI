from django.shortcuts import render
from flask import Response
from .main import gen, VideoCamera
from django.http import StreamingHttpResponse

# Create your views here.


def index(request):
    return render(request, 'PoolCamAI/index.html')


def main(request):
    return render(request, 'PoolCamAI/main.html')


def video_feed(request):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
    # return Response(gen(VideoCamera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')

# def index():
#     """Video streaming home page."""
#     return render_template('index.html')
from django.shortcuts import render
from .camera import VideoCamera
from django.http import StreamingHttpResponse

# Create your views here.


def index(request):
    return render(request, 'PoolCamAI/index.html')


def main(request):
    return render(request, 'PoolCamAI/main.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield b'--frame\r\nContent-Type: image/jpeg\r\nContent-Length: ' + \
              str(len(frame)).encode() + b'\r\n\r\n' + frame + b'\r\n'

def video_feed(request):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
    # return Response(gen(VideoCamera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')



from django.conf.urls import url
from . import views


app_name="upload"
urlpatterns = [
    # ex: /polls/
    url('^$', views.upload, name='upload'),
    url('show_pic/img/(?P<fileid>\d+)', views.show_picture, name='show'),

]
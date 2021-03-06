from django.conf.urls import url, include
import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='app_home'),
    url(r'^app$', views.index, name='app'),
    url(r'^status$', views.status, name='status'),
    url(r'^tasks/$', views.TEventList.as_view(), name='tasks'),
    url(r'^task_detail/(?P<pk>\d+)/$', views.TEventDetail.as_view(), name='task_detail'),
    url(r'^video_tasks/(?P<pk>[0-9a-f-]+)/$', views.TEventList.as_view(), name='video_tasks'),
    url(r'^video_tasks/(?P<pk>[0-9a-f-]+)/(?P<status>\w+)/$', views.TEventList.as_view(), name='video_tasks_status'),
    url(r'^process_tasks/(?P<process_pk>\d+)/$', views.TEventList.as_view(), name='process_tasks'),
    url(r'^process_tasks/(?P<process_pk>\d+)/(?P<status>\w+)/$', views.TEventList.as_view(),
        name='process_tasks_status'),
    url(r'^tasks/(?P<status>\w+)/$', views.TEventList.as_view(), name='tasks_filter'),
    url(r'^management/$', views.management, name='management'),
    url(r'^textsearch', views.textsearch, name='textsearch'),
    url(r'^retrievers/$', views.RetrieverList.as_view(), name='retriever_list'),
    url(r'^external', views.external, name='external'),
    url(r'^pull_external', views.pull_external, name='pull_external'),
    url(r'^youtube$', views.yt, name='youtube'),
    url(r'^process/$', views.ProcessList.as_view(), name='process_list'),
    url(r'^process/(?P<pk>\d+)/$', views.ProcessDetail.as_view(), name='process_detail'),
    url(r'^training_sets/$', views.TrainingSetList.as_view(), name='training_set_list'),
    url(r'^training_sets/(?P<pk>\d+)/$', views.TrainingSetDetail.as_view(), name='training_set_detail'),
    url(r'^models/$', views.TrainedModelList.as_view(), name='models'),
    url(r'^models/(?P<pk>\d+)/$', views.TrainedModelDetail.as_view(), name='models_detail'),
    url(r'^indexes/$', views.IndexEntryList.as_view(), name='indexes'),
    url(r'^stored_process/$', views.StoredProcessList.as_view(), name='stored_process_list'),
    url(r'^stored_process/(?P<pk>\d+)/$', views.StoredProcessDetail.as_view(), name='stored_process_detail'),
    url(r'^export_video', views.export_video, name='export_video'),
    url(r'^delete_video', views.delete_video, name='delete_video'),
    url(r'^rename_video', views.rename_video, name='rename_video'),
    url(r'^shortcuts', views.shortcuts, name='shortcuts'),
    url(r'^import_s3', views.import_s3, name='import_s3'),
    url(r'^submit_process', views.submit_process, name='submit_process'),
    url(r'^validate_process', views.validate_process, name='validate_process'),
    url(r'^videos/$', views.VideoList.as_view(), name="video_list"),
    url(r'^queries/$', views.VisualSearchList.as_view()),
    url(r'^Search$', views.search),
    url(r'^videos/(?P<pk>[0-9a-f-]+)/$', views.VideoDetail.as_view(), name='video_detail'),
    url(r'^frames/(?P<pk>\d+)/$', views.FrameDetail.as_view(), name='frame_detail'),
    url(r'^segments/(?P<pk>\d+)/$', views.SegmentDetail.as_view(), name='segment_detail'),
    url(r'^queries/(?P<pk>\d+)/$', views.VisualSearchDetail.as_view(), name='query_detail'),
    url(r'^retry/$', views.retry_task, name='restart_task'),
    url(r'^segments/by_index/(?P<pk>[0-9a-f-]+)/(?P<segment_index>\d+)$', views.segment_by_index,
        name='segment_by_index'),
    url(r'^requery/(?P<query_pk>\d+)/$', views.index, name='requery'),
    url(r'^query_frame/(?P<frame_pk>\d+)/$', views.index, name='query_frame'),
    url(r'^query_detection/(?P<detection_pk>\d+)/$', views.index, name='query_detection'),
    url(r'^annotate_frame/(?P<frame_pk>\d+)/$', views.annotate, name='annotate_frame'),
    url(r'^security', views.security, name='security'),
    url(r'^expire_token', views.expire_token, name='expire_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/profile/$', views.index, name='profile'),
]

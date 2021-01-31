

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:pk>/results/',
         views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]

"""
# Using patterns
from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = (
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$',
        views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$',
        views.vote, name='vote'),
)
"""

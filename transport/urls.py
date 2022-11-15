from django.urls import path
from . import views

urlpatterns = [
    path('', views.transportListView.as_view(),name="home"),
    path(r'<int:pk>/', views.transportDetailView.as_view(),name="detail"),
    path(r'branch/<int:pk>/', views.branchDetailView.as_view(),name="branch detail"),
    path('<pk>/delete/', views.transportDeleteView.as_view(), name="delete_transport"),
    path('<pk>/update/', views.transportUpdateView.as_view(), name="update_transport"),
    path('<pk>/update_branch/', views.branchesUpdateView.as_view(), name="update_branch"),
    path('<pk>/delete_branch/', views.branchesDeleteView.as_view(), name="delete_branch"),
    path('transporter_search', views.transporter_search),
    path('search', views.search),
    path('add_transport', views.add_transport, name="add_transport"),
    path('add_branch', views.add_branch, name="add_branch"),
    path('chatbot', views.chatbot, name="chatbot"),
]

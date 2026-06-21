from django.urls import path
from core.api import views

urlpatterns = [
    path('site-settings/', views.SiteSettingsListAPIView.as_view()),
    path('banners/', views.BannerListAPIView.as_view()),
    path('services/', views.ServiceListAPIView.as_view()),
    path('services/<int:id>/', views.ServiceRetrieveAPIView.as_view()),
    path('projects/', views.ProjectListAPIView.as_view()),
    path('social-media/', views.SocialMediaListAPIView.as_view()),
    path('customer-reviews/', views.CustomerReviewListAPIView.as_view()),
    path('blogs/', views.BlogListAPIView.as_view()),
    path('blogs/<int:id>/', views.BlogRetrieveAPIView.as_view()),
    path('contact-create/', views.ContactCreateAPIView.as_view()),
]


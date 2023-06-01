from django.urls import path
from .views import HomePageView, FAQView, ContactView, FAQAPIView

apis = [
    path('api_faq_all/', FAQAPIView.as_view(), name='faq_all'),
]

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('frequently_asked_questions/', FAQView.as_view(), name='faq'),
    path('contact/', ContactView.as_view(), name='contact'),
] + apis



from django.urls import path
from .views import ImageAugmentView, SpeechToTextPDFView, NoiseCancellationView

urlpatterns = [
    path('api/image-augment/', ImageAugmentView.as_view(), name='image-augment'),
    path('api/speech-to-text/', SpeechToTextPDFView.as_view(), name='speech-to-text'),
    path('api/noise-cancellation/', NoiseCancellationView.as_view(), name='noise-cancellation'),
    # other paths
]

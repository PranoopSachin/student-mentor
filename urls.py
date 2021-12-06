from rest_framework.routers import DefaultRouter
from api.views import QuestionViewSet
from api.views import AnswerViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'', QuestionViewSet, base_name='QUESTIONS')
urlpatterns = router.urls

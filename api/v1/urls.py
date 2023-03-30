from rest_framework.routers import SimpleRouter
from .organization import views

router = SimpleRouter()
router.register("entrants", views.EntrantViewSet)

urlpatterns = router.urls

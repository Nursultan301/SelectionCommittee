from rest_framework import permissions
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Прием абитуриентов",
        default_version='v1',
        description="Абитуриенты, желающие поступить в учебное заведение,\n подают заявления, в которых указывают "
                    "выбранную\n образовательную программу и прикладывают необходимые документы для \nподтверждения "
                    "своей квалификации и справок об образовании. \nПосле подачи заявления абитуриент проходит отбор, "
                    "\nкоторый может включать в себя экзамены, собеседования, \nтестирование и другие формы "
                    "оценки знаний.",
        license=openapi.License(name="ООсОо License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

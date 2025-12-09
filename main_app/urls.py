from django.urls import path
from .views import (
    Home,
    CreateUserView,
    LoginView,
    VerifyUserView,
    CategoryList,
    CategoryDetail,
    TechniqueListCreate,
    TechniqueDetail,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category-detail'),
    path('techniques/', TechniqueListCreate.as_view(), name='technique-list-create'),
    path('techniques/<int:id>/', TechniqueDetail.as_view(), name='technique-detail'),
]
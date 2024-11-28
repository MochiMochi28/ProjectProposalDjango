from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from django.contrib import admin
from django.urls import path
from bookinfos.views import bookInfoView
from AddSections.views import AddSectionsView
from BorrowedBooks.views import BorrowedBooksView
from .views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bookinfos/' , bookInfoView.as_view()),
    path('api/AddSections/' , AddSectionsView.as_view()),
    path('api/BorrowedBooks/' , BorrowedBooksView.as_view()), 
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/users/', UserView.as_view())
]


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SchoolSignup, StudentBulkCreate, StudentList, StudentUpdate


urlpatterns = [
    path('school/signup/', SchoolSignup.as_view(), name='school_signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/bulk-create/<int:grade>/', StudentBulkCreate.as_view(), name='student_bulk_create'),
    path('students/list/<int:grade>/', StudentList.as_view(), name='student_list'),
    path('students/update/<int:student_id>/', StudentUpdate.as_view(), name='student_update'),
]

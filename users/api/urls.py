from django.urls import path
from users.api.views import create_user
# The in-built django restframework method responsible for logging a user in and returning their authorization token
from rest_framework.authtoken.views import obtain_auth_token
# from users.api.views import createUserView

app_name = 'users'

urlpatterns = [
    # Create a new user
    path('create', create_user, name='api-create-user'),
    # Log in to the API
    path('login', obtain_auth_token, name='api-log-in'),
]




# urlpatterns =[
#     path('create', createUserView.as_view(), name='api-create-user'),
#     path('login', obtain_auth_token, name='api-')
# ]
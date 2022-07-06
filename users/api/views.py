from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# This method allows a view method to be accessed without providing authentication token or details
from rest_framework.permissions import AllowAny

# The serializer class that will be used to convert python database objects to JSON for transmittion as a HTTP response
from .serializers import UserCreateSerializer

# The in-built django restframework table responsible for saving the user Tokens
from rest_framework.authtoken.models import Token

# Method used to specify the http methods. In this case, we have 'POST' method
@api_view(['POST'])

# permission_classes: Python decorator used to set the permisions required to access a view method
# we are stating that access to this method does not require any authentication
@permission_classes((AllowAny, ))
# the method responsible for registering a new user
def create_user(request):
    data = {}
    # pass the data sent with the POST request to the UserCreateSerializer
    # the parameters passed should match the expected fields in the UserCreateSerializer
    serialized = UserCreateSerializer(data=request.data)
    # validate that the data passed has no errors
    if serialized.is_valid():
        # save the serialized data
        account = serialized.save()
        # generate the authentication token and send it to the user
        data['token'] = Token.objects.create(user=account).key
        data['response'] = 'Account Successfully Created'
    else:
        data['response'] = serialized.errors

    return Response(data=data)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import AllowAny
# from .serializers import UserCreateSerializer
# from rest_framework.authtoken.models import Token

# class createUserView(LAPIView):
#     def post(self, request):
#         data = {}
#         # pass the data sent with the POST request to the UserCreateSerializer
#         # the parameters passed should match the expected fields in the UserCreateSerializer
#         serialized = UserCreateSerializer(data=request.data)
#         # validate that the data passed has no errors
#         if serialized.is_valid():
#             # save the serialized data
#             account = serialized.save()
#             # generate the authentication token and send it to the user
#             data['token'] = Token.objects.create(user=account).key
#             data['response'] = 'Account Successfully Created'
#         else:
#             data['response'] = serialized.errors

#         return Response(data=data)








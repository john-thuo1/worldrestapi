#The default Django user database table that will be used to create a new user
from django.contrib.auth.models import User
#The built in Django serializers method used to convert python database objects to JSON objects
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    # Field is used for password confirmation
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    # UserCreateSerializer class interacts with User table and requires data sent via POST to have datafields email, password and password
    class Meta:
        model = User
        fields = ['email','password','password2']
        # Check how extra_kwargs are passed
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # Override save(), in order to validate the confirmed password before creating the new user
    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password2 != password:
            raise serializers.ValidationError({'password':'Passwords must match'})

        user = User(email=self.validated_data['email'],
                                   username=self.validated_data['email'])

        user.set_password(password)

        user.save()

        return user



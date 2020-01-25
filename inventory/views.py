from django.shortcuts import render
from rest_framework_jwt.views import ObtainJSONWebToken

def home(request):
    return render(request,'home.html')


class jwt_authentication(ObtainJSONWebToken):
   def post(self, request, *args, **kwargs):
        response = ObtainJSONWebToken.post(self, request)
        return response
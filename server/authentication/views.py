from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if (serializer.is_valid()):
        user = serializer.save()

        return Response({'user': UserSerializer(user).data, 'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT", "GET", "DELETE"])
def user(request, pk):
    # if NOT POST and user doesn't exist return error
    try:
        user = User.objects.get(pk=pk)
        
    except(User.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method is "PUT":
        # return Response(status=status.HTTP_200_OK)
        return Response("Hi user, welcome to django!")
    
    elif request.method is "GET":
        # return Response("get")
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)  # Return serialized user data

        
    elif request.method is "DELETE":
        # return Response(status=status.HTTP_200_OK)
        return Response("Hi user, welcome to django!")
        
    return Response("An error occurred!", status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(["GET"])
# def delete_all(request):
#     users = User.objects.delete()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
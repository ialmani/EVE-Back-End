from .serializers import CustomUserSerializer


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username, 'id': user.id,
    }
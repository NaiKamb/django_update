from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

User = get_user_model()

@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST']) 
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Пост успешно создан', status=201)

@api_view(['DELETE'])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response('Пост успешно удален', status=204)

@api_view(['PUT'])
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Пост не найден."}, status=404)
    
    if request.method == 'PUT':
        new_body = request.data.get('body')
        
        if new_body is not None:
            post.body = new_body
            post.save()
            return Response({"message": "Пост успешно обновлен"}, status=200)
        else:
            return Response({"error": "Отсутствует новое значение для обновления."}, status=400)

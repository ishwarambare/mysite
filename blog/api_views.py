from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer
from rest_framework import generics


class PostView(APIView):
    def get(self, request):
        try:
            data = Post.objects.all()
            s_data = PostSerializer(data, many=True).data
            return Response(data={'status': True, "result": s_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'status': False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    def get(self, request):
        try:
            data = Comment.objects.all()
            s_data = CommentSerializer(data, many=True).data
            return Response(data={'status': True, "result": s_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'status': False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PostDetialView(APIView):
    def post(self, request):
        try:
            data = request.data['post']
            data = Post.objects.filter(title__icontains=data)
            s_data = PostSerializer(data, many=True).data
            return Response(data={'status': True, "result": s_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'status': False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AddComment(APIView):
    def post(self, request):
        try:
            id = request.data['id']
            num = Post.objects.get(id=int(id))
            comment = request.data['comment']
            data = Comment.objects.create(post=num, body=comment)
            s_data = CommentSerializer(data, many=True).data
            return Response(data={'status': True, "result": s_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'status': False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class MailApiView(viewsets.ViewSet):
#     def mail_send(self, request):
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UplodeImage(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

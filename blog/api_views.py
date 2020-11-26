from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        try:
            data = Post.objects.all()
            s_data = PostSerializer(data, many=True).data
            return Response(data={'status': True, "result": s_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'status': False, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

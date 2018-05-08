from website.models import Video
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 导入状态码库
from rest_framework import status


class VideoSerializer(serializers.ModelSerializer):
    # 设置对title进行限制，最小长度为1
    title = serializers.CharField(min_length=1)
    class Meta:
        model = Video
        fields = '__all__'


@api_view(['GET', 'POST'])
def video(request):
    if request.method == 'GET':
        # 将Video.objects.all()改成按照ID进行逆向排序
        video_list = Video.objects.order_by('-id')
        # 如果需要序列化多个对象，则指定many=True
        serializer = VideoSerializer(video_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            # 序列化器将会直接将数据存储到VideoSerializer中关联的数据库Video
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        body = {
            'body': serializer.errors,
            'msg': '40001'
        }
        return Response(body, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def video_card(request, id):
    video_card = Video.objects.get(id=id)
    if request.method == 'PUT':
        serializer = VideoSerializer(video_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        video_card.delete()
        return Response({'msg': 'A-OK'}, status=status.HTTP_201_CREATED)

# 引入Models数据库
from website.models import Video
# 引入rest_framework中的序列化需要的库,构造序列化器，将models中的数据转换成字典结构
from rest_framework import serializers
# 引入rest_framework中的响应库与api_view,让视图只返回json数据
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 1.构建序列化，定义一个序列化器类
class VideoSerializer(serializers.ModelSerializer):
    # 定义一个类Meta，这是序列化的固定写法
    class Meta:
        # 需要序列化的类为Video
        model = Video
        # 定义为__all__以后，后续会将数据库中所有数据都转换为字典结构，包括以下几个：
        # title，content，url_image，cover和editors_choice
        fields = '__all__'
        # 如果只需要转换其中一部分的话，可以使用元祖来定义，如只需转换title和content的话可以按照如下定义
        # 注意：后面一个数据后的逗号不能少
        # fields = ('title','content',)

# 2.编写一个视图,且添加装饰器使得返回的Response里的数据真正转化为json数据
# 装饰器的作用即是装饰某个函数，可以理解为该函数的插件，下面语句指的是使用GET方法访问时可以返回json数据
@api_view(['GET'])
def video(request):
    # 获取所有数据库Video的所有对象，返回结果为QuerySet
    video_list = Video.objects.all()
    # 实例化一个序列化器，传入参数为获取的QuerySet即查询的所有数据库对象实体
    # 第二个参数many=True表示的是对所有数据进行序列化，如果取回的数据只有一个对象则不需要指定many
    serializer = VideoSerializer(video_list,many=True)
    print('*'*20)
    print('\n')
    print(repr(serializer))
    print('*'*20)
    print('\n')

    return Response(serializer.data)
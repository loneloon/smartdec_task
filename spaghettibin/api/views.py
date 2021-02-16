from django.utils.timezone import now
from .models import CodePost
from .serializers import PostSerializer
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.encoding import smart_text


@api_view(['GET'])
def get_list(request):
    scripts = CodePost.objects.all().order_by("-created_at")
    serializer = PostSerializer(scripts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_script(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def read_script(request, pk):
    scripts = CodePost.objects.all().filter(id=pk).first()
    serializer = PostSerializer(scripts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def update_script(request, pk):
    script_instance = CodePost.objects.all().filter(id=pk).first()

    data = request.data
    data.update({"updated_at": now()})

    serializer = PostSerializer(instance=script_instance, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_script(request, pk):
    script_instance = CodePost.objects.all().filter(id=pk).first()

    if script_instance:
        script_instance.delete()

    return Response(content_type='text/html')

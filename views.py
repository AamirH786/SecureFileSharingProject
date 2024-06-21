from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File, DownloadLink, CustomUser
from .serializers import FileSerializer, DownloadLinkSerializer, CustomUserSerializer

class ProfileViews(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        candidates = CustomUser.objects.all()
        serializer = CustomUserSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UploadFileView(APIView):
    def post(self, request, *args, **kwargs):
        if request.user.is_ops_user:
            serializer = FileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Only ops users can upload files"}, status=status.HTTP_403_FORBIDDEN)

class GenerateDownloadLinkView(APIView):
    def post(self, request, file_id, *args, **kwargs):
        file = get_object_or_404(File, id=file_id)
        link = DownloadLink.objects.create(file=file, link='some_encrypted_link')
        serializer = DownloadLinkSerializer(link)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListFilesView(APIView):
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):
        mappings = CourseCertificationMapping.objects.all()
        serializer = CourseCertificationMappingSerializer(mappings, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer)

    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return CourseCertificationMapping.objects.get(id=id)
        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, id):
        mapping = self.get_object(id)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, id):
        mapping = self.get_object(id)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, id):
        mapping = self.get_object(id)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        mapping = self.get_object(id)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
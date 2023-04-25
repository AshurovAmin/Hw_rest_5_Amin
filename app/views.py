from django.shortcuts import render

from rest_framework import mixins, generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Student, Mentors
from .serializers import CourseSerializer, StudentSerializer, MentorsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentListCreateAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MentorListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        firms = Mentors.objects.all()
        serializer = MentorsSerializer(firms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = MentorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorRetrieveUpdateDestroyAPIView(APIView):

    def get_mentor(self, mentor_id):
        return generics.get_object_or_404(Mentors, id=mentor_id)

    def get(self, request, mentor_id, *args, **kwargs):
        serializer = MentorsSerializer(self.get_mentor(mentor_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, mentor_id, *args, **kwargs):
        serializer = MentorsSerializer(self.get_mentor(mentor_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mentor_id, *args, **kwargs):
        self.get_mentor(mentor_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import viewsets
from college.models import Notice, Student
from college.myserializer import NoticeSerializer, StudentSerializer

# Create your views here.


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

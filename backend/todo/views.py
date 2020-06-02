# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    #queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner-self.request.user)
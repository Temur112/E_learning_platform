from rest_framework import generics, viewsets
from courses.api.serializers import SubjectSerializer, CourseSerializer
from courses.models import Subject, Course
from django.db.models import Count
from courses.api.pagintation import StandardPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from courses.api.permissions import isEnrolled
from courses.api.serializers import CourseWithContentsSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.annotate(total_courses=Count('courses'))
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandardPagination

    @action(
        detail=True,
        methods=['POST'],
        authentication_classes=[BasicAuthentication,],
        permission_classes=[IsAuthenticated,],
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.student.add(request.user)
        return Response({'success': True})


    @action(
        detail=True,
        methods=['GET'],
        serializer_class=CourseWithContentsSerializer,
        authentication_classes=[BasicAuthentication,],
        permission_classes=[IsAuthenticated, isEnrolled],
    )
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination
    queryset = Subject.objects.annotate(total_courses=Count('courses'))


# class CourseEnrollView(APIView):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.student.add(request.user)
#         return Response({'success': True})



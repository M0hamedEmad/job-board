from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import JobSerializer
from .models import Job
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

@api_view()
def joblistapi(request):
    jobs = Job.objects.all()
    js = JobSerializer(jobs, many=True).data

    return Response({"data":js})

@api_view()
def job(request, id):
    job = Job.objects.get(id=id)
    data = JobSerializer(job, many=False).data
    return Response({'data':data})


class JobApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    premission_class = [IsAdminUser]
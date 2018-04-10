
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse

from avi.models import (resource_model, algorithm_model, gaia_query_model,
                        herschel_query_model, plot_model, results_model,
                        algorithm_info_model)
from avi.serializers import (resource_serializer, algorithm_serializer,
                             gaia_query_serializer, hsa_query_serializer, 
                             plot_serializer, results_serializer,
                             algorithm_info_serializer)

class algorithms_info(viewsets.ModelViewSet):
    queryset = algorithm_info_model.objects.all()
    serializer_class = algorithm_info_serializer

class algorithms_list(viewsets.ModelViewSet):
    queryset = algorithm_model.objects.all()
    serializer_class = algorithm_serializer

class gaia_queries_list(viewsets.ModelViewSet):
    queryset = gaia_query_model.objects.all()
    serializer_class = gaia_query_serializer

class hsa_queries_list(viewsets.ModelViewSet):
    queryset = herschel_query_model.objects.all()
    serializer_class = hsa_query_serializer

class resources_list(viewsets.ModelViewSet):
    queryset = resource_model.objects.all()
    serializer_class = resource_serializer

class plot_list(viewsets.ModelViewSet):
    queryset = plot_model.objects.all()
    serializer_class = plot_serializer

class results_list(viewsets.ModelViewSet):
    queryset = results_model.objects.all()
    serializer_class = results_serializer

class samp_resource(APIView):
    def get(self, request, resource_id):
        res = resource_model.objects.filter(pk=resource_id)
        if not res:
            return None
        full_name = os.path.join(res[0].path, res[0].name)
        file_data = open(full_name,'rb')
        file_type = 'application/xml'
        name, ext = os.path.splitext(res[0].name) 
        if ext == ".fits" or ext == ".tar":
            file_type = 'application/tar+gzip'
        response = HttpResponse(file_data, content_type=file_type)
        return response
        
class resource(APIView):
    def get(self, request, resource_id):
        #return JsonResponse({"votable":3, "ASD": 123})
        #vot_name = open('/data/output/100.241700_9.895000_0.100000_gaia_source.vot','rb')
        res = resource_model.objects.filter(pk=resource_id)
        if not res:
            return None
        full_name = os.path.join(res[0].path, res[0].name)
        file_data = open(full_name,'rb')
        file_type = 'application/xml'
        name, ext = os.path.splitext(res[0].name) 
        if ext == ".fits" or ext == ".tar":
            file_type ='application/x-tar'
        response = HttpResponse(file_data, content_type=file_type)
        response['Content-Disposition'] = 'attachment; filename="%s"'%res[0].name
        return response

class get_resource(APIView):
    def get(self, request, resource_id):
        res = resource_model.objects.filter(pk=resource_id)
        if not res:
            return None
        full_name = os.path.join(res[0].path, res[0].name)
        file_data = open(full_name, 'rb')
        file_type = 'application/text'
        name, ext = os.path.splitext(res[0].name) 
        if ext == ".vot" or ext == ".xml":
            file_type = 'application/xml'
            return HttpResponse(file_data, content_type=file_type)
        response = HttpResponse(file_data)#, content_type=file_type)
        #response['Content-Disposition'] = 'filename="%s"'%res[0].name
        return response
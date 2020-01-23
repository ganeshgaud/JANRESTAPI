from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from testapp.utils import is_json
from .serializers import EmployeeSerializer
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCrudCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        print(id)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Created Successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=200)

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Updated Successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json',status=200)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=200)

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        emp.delete()
        msg={'msg':'Resource deleted Successfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json',status=200)


        
        




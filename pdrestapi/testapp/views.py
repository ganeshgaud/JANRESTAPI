from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from testapp.models import Employee
import json
from testapp.mixins import HttpResponseMixin,SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm



# Create your views here.
####################################################################################
##### All methods are accesed by different End Point##################################
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCrudView(HttpResponseMixin,View):    
    # Retrieving all records from Employee table by using simple json()
    def get(self,request,*args,**kwargs):
        empl=Employee.objects.all()
        emp_data=[]
        for emp in empl:
            tmp_data={
                'ename':emp.ename,
                'eaddr':emp.eaddr,
                'esal' :emp.esal,
                'eno'  :emp.eno
            }
            emp_data.append(tmp_data)
        json_data=json.dumps(emp_data)
        return HttpResponse(json_data,content_type="application/json")

    # Posting record to Employee table by using simple json()
    def post(self,request,*args,**kwargs):
         data=request.body
         json_data=is_json(data)
         if not json_data:
            json_data=json.dumps({'msg':'Please enter valid json data'})
            return self.render_to_response(json_data,status=404)
         empdata=json.loads(data)
         form=EmployeeForm(empdata)
         if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Data added successfully'})
            return self.render_to_response(json_data)
         if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=404)




####################################################################################
##### All methods are accesed by single End Point##################################
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListView(HttpResponseMixin,View):  
     def get_object_id(self,id):
         try:
             emp=Employee.objects.get(id=id)
         except Employee.DoesNotExist:
             emp=None 
         return emp

    
    # Retrieving single records from Employee table by using json()
     def get(self,request,*args,**kwargs):
        #####################################################
        # try:
        #     emp=Employee.objects.get(id=id)
        # except Employee.DoesNotExist:
        #     json_data=json.dumps({'msg':'The requested data is not available'})
        #     return self.render_to_response(json_data,status=404)
        # else:
        #     emp_data={
        #         'ename':emp.ename,
        #         'eaddr':emp.eaddr,
        #         'esal' :emp.esal,
        #         'eno'  :emp.eno
        #     }
        #     json_data=json.dumps(emp_data)
        #     return self.render_to_response(json_data)
        #######################################################

        data=request.body
        json_data=is_json(data)
        if not json_data:
            json_data=json.dumps({'msg':'Please enter valid json data'})
            return self.render_to_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            empl=Employee.objects.all()
            emp_data=[]
            for emp in empl:
                 tmp_data={
                    'ename':emp.ename,
                    'eaddr':emp.eaddr,
                    'esal' :emp.esal,
                    'eno'  :emp.eno
                 }
                 emp_data.append(tmp_data)
            json_data=json.dumps(emp_data)
            return self.render_to_response(json_data,status=200)
        emp=self.get_object_id(id)
        if  emp is None:
             json_data=json.dumps({'msg':'The requested id is not available'})
             return self.render_to_response(json_data,status=404)
        tmp_data={
            'ename':emp.ename,
            'eaddr':emp.eaddr,
            'esal' :emp.esal,
            'eno'  :emp.eno
        }
        json_data=json.dumps(tmp_data)
        return self.render_to_response(json_data,status=200)
     
    #Updating Resource by using simple json module
     def put(self,request,*args,**kwargs):
         data=request.body
         json_data=is_json(data)
         if not json_data:
            json_data=json.dumps({'msg':'Please enter valid json data'})
            return self.render_to_response(json_data,status=404)
         pdata=json.loads(data)
         id=pdata.get('id',None)
         if id is None:
             json_data=json.dumps({'msg':'Please provide id'})
             return self.render_to_response(json_data,status=404)
         emp=self.get_object_id(id)
         if  emp is None:
             json_data=json.dumps({'msg':'The requested id is not available'})
             return self.render_to_response(json_data,status=404)
         provided_data=json.loads(data)
         original_data={
             'ename':emp.ename,
             'eaddr':emp.eaddr,
             'esal' :emp.esal,
             'eno'  :emp.eno
            }
         original_data.update(provided_data)
         form=EmployeeForm(original_data,instance=emp)
         if form.is_valid():
             form.save(commit=True)
             json_data=json.dumps({'msg':'Data added successfully'})
             return self.render_to_response(json_data)
         if form.errors:
             json_data=json.dumps(form.errors)
             return self.render_to_response(json_data,status=404)

    # Posting record to Employee table by using simple json()
     def post(self,request,*args,**kwargs):
         data=request.body
         json_data=is_json(data)
         if not json_data:
            json_data=json.dumps({'msg':'Please enter valid json data'})
            return self.render_to_response(json_data,status=404)
         empdata=json.loads(data)
         form=EmployeeForm(empdata)
         if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Data added successfully'})
            return self.render_to_response(json_data)
         if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=404)

    #Deleting resource by using simple Json()
     def delete(self,request,*args,**kwargs):
         data=request.body
         json_data=is_json(data)
         if not json_data:
            json_data=json.dumps({'msg':'Please enter valid json data'})
            return self.render_to_response(json_data,status=404)
         pdata=json.loads(data)
         id=pdata.get('id',None)
         if id is None:
             json_data=json.dumps({'msg':'Please provide id'})
             return self.render_to_response(json_data,status=404)
         emp=self.get_object_id(id)
         if  emp is None:
             json_data=json.dumps({'msg':'The requested id is not available'})
             return self.render_to_response(json_data,status=404)
         status,deleted_item=emp.delete()
         if status==1:
             json_data=json.dumps({'msg':'Record deleted successfully'})
             return self.render_to_response(json_data,status=200)
         json_data=json.dumps({'msg':'Some problem in deleting record plz try after some time'})
         return self.render_to_response(json_data,status=500)


####################################################################################
##### All methods are accesed by single End Point by Django serialize()#############
class EmployeeSerializeCrudView(HttpResponseMixin,SerializeMixin,View):
    def get_object_id(self,id):
         try:
             emp=Employee.objects.get(id=id)
         except Employee.DoesNotExist:
             emp=None 
         return emp

    def get(self,request,*args,**kwargs):
        data=request.body
        json_data=is_json(data)
        if not json_data:
            json_data=json.dumps({'msg':'Please enter valid json data'})
            return self.render_to_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            qs=Employee.objects.all()
            emp_data=self.serialize(qs)
            json_data=json.dumps(emp_data)
            return self.render_to_response(json_data,status=200)
        emp=self.get_object_id(id)
        if  emp is None:
             json_data=json.dumps({'msg':'The requested id is not available'})
             return self.render_to_response(json_data,status=404)
        emp=Employee.objects.get(id=id)
        emp_data=self.serialize([emp,])
        json_data=json.dumps(emp_data)
        return self.render_to_response(json_data,status=200)
     


         



     


        




    
    

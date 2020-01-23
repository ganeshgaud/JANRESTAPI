from rest_framework import serializers
from .models import Employee
############## Here we are using only Serializer Class##############################
# #Custom Validators External(Validator Attribute)
# def multiples_of_100(value):
#     if value%100!=0:
#         raise serializers.ValidationError("Salry should be in multiple of 100")
#     return value

#    
# class EmployeeSerializer(serializers.Serializer):
#     ename=serializers.CharField(max_length=64)
#     eaddr=serializers.CharField(max_length=64)
#     esal=serializers.IntegerField(validators=[multiples_of_100])
#     eno=serializers.IntegerField()

#     #field level validators
#     # def validate_esal(self,value):
#     #     if value<5000:
#     #         raise serializers.ValidationError("Salary Should not be less than 5000")
#     #     return value

#     #object level validators
#     def validate(self,data):
#         ename=data.get('ename')
#         esal=data.get('esal')
#         if ename.lower()=='ganesh':
#             if esal<=10000:
#                 raise serializers.ValidationError('Ganesh Salary should more than 10000')
#         return data

#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)
#     def update(self,instance,validated_data):
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.eaddr=validated_data.get('eaddr',instance.eaddr)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.save()
#         return instance
#############################################################################

############## Here we are using only ModeSerializer Class##############################

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
    #object level validators
    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='ganesh':
            if esal<=10000:
                raise serializers.ValidationError('Ganesh Salary should more than 10000')
        return data


   
from rest_framework import serializers
from .models import Student,Path

#1. yöntem
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
      # CRUD İŞLEMLERİ İÇİN AŞAĞIDA 👇 BELİRTİLEN KOMUTLAR OLMALI
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance
#2. yöntem

    
class StudentSerializer(serializers.ModelSerializer):
    # full_name=serializers.SerializerMethodField()
    # number_name=serializers.SerializerMethodField()

    # def get_full_name(self,obj):
    #     return f'{obj.first_name}{obj.last_name}'
    # def get_number_name(self,obj):
    #     return f'{obj.number}{obj.first_name}'
    path=serializers.StringRelatedField()  # get işlemi yapar.Post işleminde error >>path_id 
    path_id=serializers.IntegerField() # create işlemi yapmak için kullanılır
    class Meta:
        model = Student
        fields = ["id","path_id","path","first_name", "last_name", "number"]
        # fields = '__all__'
        # exclude = ['number']

class PathSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True) # nesned olarak tüm veri geliyor 
    
    class Meta:
        model = Path
        fields = ["id", "path_name","students"]
        #fields=__all__ not best pratice tüm datayı göndermek mantıklı değil
from rest_framework import serializers
from .models import Student,Path

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    number = serializers.IntegerField(required=False) # null==False
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance

#* =====================MODEL SERİALİZER========================


class StudentSerializer(serializers.ModelSerializer):
    #full_name=serializers.SerializerMethodField()

    def get_full_name(self,obj):
        return f"{obj.first_name} {obj.last_name}"

    path=serializers.StringRelatedField()
    path_id=serializers.IntegerField()
    class Meta:
        model= Student
        fields = ['id',"path_id","path" ,'first_name', 'last_name', 'number']
        #fields = '__all__'
        # exclude = ['id'] / ('id',) list veya tuple olarak yazılabilir.
        # 
    def validate_number(self, value):

        if value > 200:
            raise serializers.ValidationError("Student number can not be greater than 2000!")  
        return value

    def validate_first_name(self, value):
        
        if value.lower() == 'barıs':
            raise serializers.ValidationError("Rafe can not be our student!")
        return value  




class PathSerializer(serializers.ModelSerializer):
    #students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Path
        fields = ['id',"path_name"]
        #fields = '__all__'  
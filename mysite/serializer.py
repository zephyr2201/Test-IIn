from rest_framework import serializers
from .models import Person
import datetime


class PersonSerializer(serializers.ModelSerializer):
    iin = serializers.CharField(max_length=12, min_length=12)
    age = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Person
        fields = ['iin', 'age']

    def create(self, validated_data):
        iin_person = validated_data['iin']
        years = iin_person[:2]
        month = iin_person[2:4]
        days = iin_person[4:6]
        century = iin_person[6:7]
        if int(century) == 1 or int(century) == 2:
            years = '18' + years
        elif int(century) == 3 or int(century) == 4:
            years = '19' + years
        else:
            years = '20' + years
        iin_convert = f"{years}-{month}-{days}"
        try:
            iin_convert = datetime.datetime.strptime(iin_convert, "%Y-%m-%d")
            return Person.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError("Invalid iin", code='invalid')

    def get_age(self, person):
        return person.calculated_age

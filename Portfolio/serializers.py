from rest_framework import serializers
from Portfolio.models import Createportfolio

class templateserializer(serializers.ModelSerializer):
    class Meta:
        model = Createportfolio
        fields = "__all__"
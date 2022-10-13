from rest_framework import serializers

from ads.models import Ad


def desc_restriction(desc):
    if len(desc)> 1000:
        raise serializers.ValidationError('description should be no more than 1000 letters')
    return desc

def title_restriction(title):
    if len(title)> 200:
        raise serializers.ValidationError('description should be no more than 1000 letters')
    return title

def photos_restriction(photos):
    if len(photos)>3:
        raise serializers.ValidationError('should be no more than 3 photos')
    return photos

class AdSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[title_restriction])
    description = serializers.CharField(validators=[desc_restriction])
    photos = serializers.JSONField(validators=[photos_restriction])


    class Meta:
        model = Ad
        fields = '__all__'
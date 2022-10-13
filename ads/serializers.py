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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['main_photo'] = instance.photos[0] if len(instance.photos) > 0 else None
        return representation


    class Meta:
        model = Ad
        fields = '__all__'


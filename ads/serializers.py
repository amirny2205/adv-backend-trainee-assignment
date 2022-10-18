from rest_framework import serializers

from ads.models import Ad


def title_restriction(title):
    if len(title) > 200:
        raise serializers.ValidationError('description should be no more than 1000 letters')
    return title


def desc_restriction(desc):
    if len(desc) > 1000:
        raise serializers.ValidationError('description should be no more than 1000 letters')
    return desc


def photos_restriction(photos):
    if len(photos)>3:
        raise serializers.ValidationError('should be no more than 3 photos')
    return photos

class AdSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[title_restriction])
    description = serializers.CharField(validators=[desc_restriction] , required=False)
    photos = serializers.JSONField(validators=[photos_restriction], required=False)
    main_photo = serializers.CharField(max_length=200, required=False)

    def __init__(self, *args, **kwargs):

        # Instantiate the superclass normally
        super(AdSerializer, self).__init__(*args, **kwargs)

        # fetch or set fields to default
        if self.context['request'].method in ('GET'):
            fields = self.context['request'].query_params.get('fields')
            if fields:
                fields = fields.split(',') + ['title','main_photo','price']
            else:
                fields = ['title','main_photo','price']
                # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)





    class Meta:
        model = Ad
        fields = '__all__'


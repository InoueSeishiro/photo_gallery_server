from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    def is_valid(self, data):
        if data['image'] is None:
            return serializers.ValidationError()
        return data


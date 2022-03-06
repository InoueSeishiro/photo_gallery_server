from rest_framework.decorators import api_view
from rest_framework.response import Response
from image.models import *


# Create your views here.
@api_view(['POST'])
def upload_images(request):
    keywords = []
    for word in request.data.get('keywords'):
        result = Keyword.objects.filter(keyword=word)
        if result.count() == 0:
            keyword = Keyword(keyword=word)
            keyword.save()
            keywords.append(keyword)
        else:
            keywords.append(result.first())
    for img in request.data.get('images'):
        image = Image(image=img)
        for keyword in keywords:
            KeywordRelation(image_id=image.id, keyword_id=keyword.id).save()


@api_view(['GET'])
def get_image_all(request):
    images = Image.objects.all()
    return Response(data=images)


@api_view(['GET'])
def test(request):
    return Response(data='success')

# def get_image_search(request):
# def get_keyword(request):
# def attach_keyword(request):
# def remove_keyword(request):
# def delete_keyword(request):

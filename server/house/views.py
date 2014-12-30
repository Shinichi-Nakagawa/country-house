from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from house.models import HouseRecord
from house.serializers import HouseRecordSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def record_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        records = HouseRecord.objects.all()
        serializer = HouseRecordSerializer(records, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HouseRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def record_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        record = HouseRecord.objects.get(pk=pk)
    except HouseRecord.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HouseRecordSerializer(record)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HouseRecordSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        record.delete()
        return HttpResponse(status=204)

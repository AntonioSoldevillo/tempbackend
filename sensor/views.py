from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataView(APIView):
    def get(self, request, *args, **kwargs):
        data = SensorData.objects.all().order_by('-timestamp')[:20]  # latest 20 entries
        serializer = SensorDataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        temperature = request.data.get('temperature')
        humidity = request.data.get('humidity')

        if temperature is None or humidity is None:
            return Response({"error": "Missing temperature or humidity"}, status=status.HTTP_400_BAD_REQUEST)

        SensorData.objects.create(temperature=temperature, humidity=humidity)
        return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)

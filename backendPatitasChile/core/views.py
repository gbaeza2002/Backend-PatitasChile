from rest_framework.response import Response
from rest_framework.views import APIView

class PrincipalView(APIView):
    def get(self, request):
        return Response({"message": "Bienvenido a la vista principal de la API"})

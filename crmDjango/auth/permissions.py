from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Sử dụng decorator để chỉ định permission
def protected_view(request):
    return Response({"message": "This is a protected view."}, status=status.HTTP_200_OK)

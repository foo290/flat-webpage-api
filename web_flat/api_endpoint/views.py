from .parser import Scraper
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['POST'])
def get_parsed(request):
    if request.data:
        link = request.data['url']
        scraper = Scraper()
        scraper.run_parser(link)
        response = scraper.get_results()
        if response:
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response('Something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response('empty data', status=status.HTTP_400_BAD_REQUEST)


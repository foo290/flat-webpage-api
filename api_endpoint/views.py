from .parser import Scraper
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .utils import validate_url


# Create your views here.

@api_view(['POST'])
@validate_url
def flatten_web(request, **kwargs):
    """
    Send a post request in format like this:
    {
        "url": "any url ..."
    }

    example:
    {
        "url": "https://www.github.com"
    }
    """
    valid = kwargs.get('valid')
    if valid:
        link = request.data['url']
        scraper = Scraper()
        scraper.run_parser(link)
        response = scraper.get_results()
        if response:
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response('Something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response('Something is not right with the post request.', status=status.HTTP_400_BAD_REQUEST)


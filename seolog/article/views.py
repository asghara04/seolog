from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Article
from .serializers import ArticleSerializer


class ArticlesView(APIView):
	def get(self, request):
		# filters
		filters = dict(request.GET.copy())

		# cutting q
		if "q" in filters:
			q = filters.pop("q")

		# setting types
		for i in filters:
			try:
				filters[i] = int(filters[i][-1])
			except:
				return Response({"message":"please enter valid filters!"}, status=status.HTTP_400_BAD_REQUEST)
	
		# Articles Query
		try:
			articles = Article.published.filter(**filters)
		except:
			articles = Article.published.all()
		
		serializer = ArticleSerializer(articles, many=True, context={"request":request})

		return Response(serializer.data, status=status.HTTP_OK_200)
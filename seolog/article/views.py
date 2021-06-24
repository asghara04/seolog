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
			articles = Article.objects.filter(**filters)
		except:
			articles = Article.objects.all()
		
		serializer = ArticleSerializer(articles, many=True, context={"request":request})

		return Response(serializer.data, status=status.HTTP_200_OK)


# single article data
class ArticleView(APIView):

	# get one article by the given detail, (if the given dertail was multiple article it gives the first one).
	def get_article(self, **kwargs):
		try:
			return Article.objects.get(**kwargs)
		except:
			raise Http404

	def get(self, request, **kwargs):
		# get article by get_article function
		article = self.get_article(**kwargs)

		# serialize the giben article
		serializer = ArticleSerializer(article, context={"request":request})

		return Response(serializer.data, status=status.HTTP_200_OK)
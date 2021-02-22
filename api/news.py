import json
from integrator import news_articles


class NewsAgent:
    
	data = news_articles()
	def search_by_title(self, title):
		response = []
		for article in self.data:
			article = json.loads(article)
			if title.lower() in article['title'].lower():
				response.append(article)
		print('results: ',len(response), title)
		return response

	def search_by_category(self, cat):
		cat = str(cat)
		response = []
		for article in self.data:
			article = json.loads(article)
			if cat == 'Opinion and Analysis':
				cat = 'Opinion and analysis'				
			if cat == article['cat']:
				response.append(article)
		print('results: ',len(response), cat)
		return response





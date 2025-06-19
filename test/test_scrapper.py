from app import Scrapper

class TestScrapper:
	def test_formats_url_correctly(self):
		url = "www.google.com"
		scp = Scrapper(url)
		assert "https://www.google.com" == scp.url

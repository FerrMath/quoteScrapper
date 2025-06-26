from app import Scrapper

class TestScrapper:
	def test_formats_url_correctly(self):
		url = "en.wikiquote.org/wiki/Main_Page"
		scp = Scrapper(url)
		assert "https://en.wikiquote.org/wiki/Main_Page" == scp.url
	
	def test_returns_true_if_is_dangerous_url(self):
		urls = [
			"www.google.zip",
			"www.google.bat",
			"www.google.dll",
			"www.google.rar",
			"www.google.msi",
			"www.google.ps2",
			"www.google.exe",
		]
		for test in urls:
			assert Scrapper._is_unsafe_url(test) == True
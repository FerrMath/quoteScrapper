import requests
from .exceptions import InvalidUrlError
from bs4 import BeautifulSoup

class Scrapper:
	soup: BeautifulSoup

	def __init__(self, url=None) -> None:
		if not (url is None):			
			clean = ""
			clean = self._clean_url(url)
			if clean is None:
				raise InvalidUrlError(f"Invalid URL: {url}")
			else:
				self.url = clean
				self._set_soup(clean)

	def get_todays_quote_of_the_day(self):
		# data = self.soup.select_one("#mf-qotd>div>div td:first-child")
		data = self.soup.select_one("#mf-qotd")
		quote = ""
		if data is None:
			return
		else:
			for td in data.find_all("td"):
				text = td.get_text(" ", strip=True)
				if len(text) > 20 and "~" not in text:
					quote = text.replace(" , ", ", ")
					break
		return quote
	
	def get_todays_quote_author(self):
		data = self.soup.select_one("#mf-qotd")
		if data is None:
			raise ValueError("Author not found")
		for td in data.find_all("td"):
			text = td.get_text(strip=True)
			if "~" in text:
				if text.startswith("~") and text.endswith("~"):
					return text.strip("~").strip()
		return "Unknown"
			
	def _clean_url(self, url:str) -> str|None:
		formated = url.strip()
		if self._is_unsafe_url(url):
			raise SystemExit("Dangerous URL detected. Aborting")
		if not url.startswith("http"):
			formated = url.split("//", 1)[-1]
			formated = "https://" + formated
		
		try:
			r = requests.head(formated, timeout=3)
			if r.status_code < 400:
				return formated
		except requests.exceptions.SSLError:
			fallback = url.replace("https://","http://", 1)
			try:
				r = requests.head(fallback, timeout=3)
				if r.status_code < 400:
					return fallback
			except:
				pass
		except:
			pass
		return None

	def _set_soup(self, url):
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		self.soup = soup


	def get_base_response(self):
		headers = {
			"User-Agent":"Mozilla/5.0",
			"Accept":"text/html"
		}
		try:
			r = requests.get(self.url, headers=headers, timeout=10)
			c_type = r.headers.get("Content-Type","")

			if 'text/html' not in c_type:
				raise requests.exceptions.RequestException(f"Tipo de conteudo não suportado: {c_type}")
			else:
				return r
		except requests.exceptions.RequestException as e:
			print(f"Error ao acessar URL: {self.url} - {e}")
			raise

	@staticmethod
	def _is_unsafe_url(url):
		dang_extensions = ['.exe', '.zip', '.rar', '.msi', '.bat', '.dll', "ps2"]
		if any(
			url.lower().endswith(ext) for ext in dang_extensions
		):
			return True
		return False

import requests
import os
from .exceptions import InvalidUrlError

class Scrapper:
	response = None

	def __init__(self, url) -> None:
		clean = ""
		clean = self._clean_url(url)
		if clean is None:
			raise InvalidUrlError(f"Invalid URL: {url}")
		else:
			self.url = clean
			print(self.url)

	
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

	@staticmethod
	def _is_unsafe_url(url):
		dang_extensions = ['.exe', '.zip', '.rar', '.msi', '.bat', '.dll', "ps2"]
		if any(
			url.lower().endswith(ext) for ext in dang_extensions
		):
			return True
		return False

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
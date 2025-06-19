import requests

class Scrapper:
	response = None

	def __init__(self, url) -> None:
		self.url = self.clean_url(url)
		response = self.get_base_response(self.url)
		if response.status_code != 200:
			print(f"Error: status code: {response.status_code}!\n{response.reason}")
	
	def clean_url(self, url) -> str:
		formated = ""
		if "http://" not in url and "https://" not in url:
			formated = f"https://{url}"
			print(formated)
			return formated
		else:
			return url

	def get_base_response(self, url:str):
		return requests.get(url)
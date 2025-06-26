from app import Scrapper

if __name__ == "__main__":
	URL = "https://en.wikiquote.zip"
	scp = Scrapper(URL)
	r = scp.get_base_response()
	print(r.text)
from app import Scrapper

if __name__ == "__main__":
	URL = "https://en.wikiquote.org/wiki/Main_Page"
	scp = Scrapper(URL)
	print(scp.get_todays_quote_of_the_day())
	print(scp.get_todays_quote_author())
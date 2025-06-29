from app import Scrapper
from app.model import Quote
from datetime import datetime

def create_todays_quote(scp:Scrapper) -> Quote|None:
	text = scp.get_todays_quote_of_the_day()
	author=scp.get_todays_quote_author()
	date=datetime.now()

	if text is None or author is None:
		return None

	todays_quote = Quote(text, author, date)
	return todays_quote


if __name__ == "__main__":
	scp = Scrapper()
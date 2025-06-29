from datetime import datetime

class Quote:
	def __init__(self, text:str, author:str, date: datetime) -> None:
		self.text = text
		self.author = author
		self.date = date
	
	def __str__(self) -> str:
		return f'"{self.text}"\n- {self.author} ({self.date.strftime("%m-%d-%Y")})'
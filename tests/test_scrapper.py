from app import Scrapper
from bs4 import BeautifulSoup

class TestScrapper:
	mock_html = """
<div id="mf-qotd">
  <div style="clear: both; border: 2px solid #ffe2e2;">
    <div style="background: #ffe2e2; text-align: center;"><b>Quote of the day</b></div>
    <div>
      <table>
        <tbody>
          <tr>
            <td valign="top" align="center">
              <table>
                <tbody>
                  <tr>
                    <td align="center">"Success is not final, failure is not fatal: it is the courage to continue that counts."</td>
                  </tr>
                  <tr>
                    <td style="font-size:smaller;">~ Winston Churchill ~</td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
          <tr>
            <td>
              <small>Extra information below the quote section.</small>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""
	
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
			assert Scrapper.is_unsafe_url(test) == True
	
	def test_successfully_gets_the_author_of_the_quote_of_the_day(self):
		scp = Scrapper()
		scp.todays_soup = BeautifulSoup(self.mock_html, "html.parser")
		author = scp.get_todays_quote_author()
		assert author == "Winston Churchill"

	def test_successfully_gets_the_quote_of_the_day(self):
		scp = Scrapper()
		scp.todays_soup = BeautifulSoup(self.mock_html, "html.parser")
		quote = scp.get_todays_quote_of_the_day()
		assert quote == '"Success is not final, failure is not fatal: it is the courage to continue that counts."'
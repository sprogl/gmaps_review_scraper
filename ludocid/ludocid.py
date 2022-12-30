import bs4
import splinter
import urllib.parse
import ludocid.exceptions
from log.logger import logger

def cid(search_term):
    url = f"https://www.google.com/search?hl=en&q={urllib.parse.quote(search_term)}"

    try:
        browser = splinter.Browser("firefox", headless=True, incognito=True)
    except splinter.exceptions.DriverNotFoundError:
        raise ludocid.exceptions.NoDriver

    browser.visit(url)

    # Click on "Reject all" to reject all cookies
    try:
        browser.find_by_id('W0wltc')[0].click()
    except splinter.exceptions.ElementDoesNotExist:
        logger.debug("no 'Reject all' button exists")
    
    
    soup = bs4.BeautifulSoup(browser.html, 'html.parser')

    browser.quit()

    try:
        cid = soup.find("a", {"data-rc_q": search_term})["data-rc_ludocids"]
    except TypeError:
        raise ludocid.exceptions.BadSearch

    return int(cid)
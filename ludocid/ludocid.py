import bs4
import splinter
import urllib.parse

def cid(search_term, save_search_file=False):
    url = f"https://www.google.com/search?q={urllib.parse.quote(search_term)}"

    browser = splinter.Browser("chrome", headless=True)
    browser.visit(url)
    if save_search_file:
        with open("page.html", "w") as file:
            file.write(browser.html)
            file.close()

    browser.find_by_text("Alle ablehnen").click()

    soup = bs4.BeautifulSoup(browser.html, 'html.parser')

    a_element = soup.find("a", {"data-rc_q": search_term})
    return int(a_element["data-rc_ludocids"])
import selenium


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def openPage(self):
        self.browser.get(self.url)

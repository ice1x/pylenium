from selenium import webdriver


class FirefoxDriver(webdriver.Firefox):

    def click_by_id(self, uri, id):
        self.get(uri)
        self.find_element_by_id(id).click()
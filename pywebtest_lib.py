from selenium import webdriver


class FirefoxDriver(webdriver.Firefox):
    """
    The goal of this wrapper for Firefox WebDriver / Selenium
    - provide combined functions to simplify web test automation
    """

    def click_by_id(self, uri, _id):
        """
        :Open uri: 
        :find element by _id on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_id(_id).click()
        return self.current_url()

    def click_by_id(self, uri, _id):
        """
        :Open uri: 
        :find element by _id on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_id(_id).click()
        return self.current_url()

    def click_by_class(self, uri, _class_name):
        """
        :Open uri: 
        :find element by _class_name on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_class_name(_class_name).click()
        return self.current_url()

    def click_by_css(self, uri, _css_selector):
        """
        :Open uri: 
        :find element by _css_selector on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_css_selector(_css_selector).click()
        return self.current_url()

    def click_by_tag_name(self, uri, _tag_name):
        """
        :Open uri: 
        :find element by _tag_name on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_tag_name(_tag_name).click()
        return self.current_url()

    def click_by_partial_link_text(self, uri, _partial_link_text):
        """
        :Open uri: 
        :find element by _partial_link_text on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_partial_link_text(_partial_link_text).click()
        return self.current_url()

    def click_by_name(self, uri, _name):
        """
        :Open uri: 
        :find element by _name on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_name(_name).click()
        return self.current_url()

    def click_by_link_text(self, uri, _link_text):
        """
        :Open uri: 
        :find element by _link_text on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_link_text(_link_text).click()
        return self.current_url()

    def click_by_xpath(self, uri, _xpath):
        """
        :Open uri: 
        :find element by _xpath on the uri:
         click by element
        :return current uri - will be the same in case of redirect absence: 
        """
        self.get(uri)
        self.find_element_by_xpath(_xpath).click()
        return self.current_url()

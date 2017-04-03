from selenium import webdriver
import urllib2
import zlib
from HTMLParser import HTMLParser
import logging
from logging import info
import time


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


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


class UrlFinder(HTMLParser):
    def __init__(self, my_tag):
        HTMLParser.__init__(self)
        self.links = []
        self.my_tag = my_tag

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.my_tag == tag:
            try:
                self.links.append(attrs['href'])
            except:
                pass

def urlopen(uri):
    """
    Get HTTP code
    """

    def try_urlopen(message='OK'):
        try:
            urllib2.urlopen(uri, timeout=30)
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                message = str(e.code)
            elif hasattr(e, 'reason'):
                message = e.reason
            info("%s - %s" % (message, str(uri)))
            return message
        except Exception, e:
            info('Exception: %s - %s' % (str(uri), repr(e)))
            time.sleep(1)
            try_urlopen('OK')
        return message

    message = try_urlopen()
    return message


def parser(node, tag):
    """
    Parse web page "where - node" / "search inside this tag"
    """
    _parser = UrlFinder(tag)
    try:
        response = urllib.urlopen(node).read()
    except Exception as e:
        info("urllib failed: %s" % e.__repr__())
        response = []

    if response and len(response) > 0:
        # NOTE: it was obsolete urllib.urlopen(node).headers.getheader('Content-Encoding') == 'gzip':
        if urllib2.urlopen(node).headers.getheader('Content-Encoding') == 'gzip':
            content = zlib.decompress(response, zlib.MAX_WBITS | 32)
        else:
            content = response
        _parser.feed(content)
        return _parser.links
    else:
        info('Content length: %s on %s by tag: %s' % (str(len(response)), str(node), str(tag)))
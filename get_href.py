from selenium import webdriver
from urllib2 import URLError
from HTMLParser import HTMLParser
from logging import info
import urllib
import logging
import urllib2
import zlib
import time
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
URI = sys.argv[1]
METH = sys.argv[2]
TAG = sys.argv[3]
DRV = sys.argv[4]

print("URI: %s\n METH: %s\n TAG: %s\n DRV: %s" % (URI, METH, TAG, DRV))

if DRV == "urllib":
    print "METH ignored, search through tag"

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

    def parser(node, tag):
        """
        Parse sitemap "where - node" / "search inside this tag"
        """
        _parser = UrlFinder(tag)
        try:
            response = urllib.urlopen(node).read()
        except Exception as e:
            info("urllib failed: %s" % e.__repr__())
            response = []

        if response and len(response) > 0:
            if urllib.urlopen(node).headers.getheader('Content-Encoding') == 'gzip':
                content = zlib.decompress(response, zlib.MAX_WBITS | 32)
            else:
                content = response
            _parser.feed(content)
            return _parser.links
        else:
            info('Content length: %s on %s by tag: %s' % (str(len(response)), str(node), str(tag)))


    def urlopen(url):
        """
        Get HTTP code
        func. from sitemap
        """

        def try_urlopen(message):
            try:
                urllib2.urlopen(url, timeout=30)
            except URLError, e:
                if hasattr(e, 'code'):
                    message = str(e.code)
                elif hasattr(e, 'reason'):
                    message = e.reason
                info("%s - %s" % (message, str(url)))
                return message
            except Exception, e:
                info('Exception: %s - %s' % (str(url), repr(e)))
                time.sleep(1)
                try_urlopen('OK')
            return message

        message = try_urlopen('OK')
        return message

    hrefs = parser(URI, TAG)
    for href in hrefs:
        print href
    print len(hrefs)


elif DRV == "firefox":
    ff = webdriver.Firefox()

    FIND = {
        "id": ff.find_elements_by_id,
        "tag": ff.find_elements_by_tag_name,
        "class": ff.find_elements_by_class_name,
        "css": ff.find_elements_by_css_selector,
        "xfref": ff.find_elements_by_xpath,
        "partlink": ff.find_elements_by_partial_link_text,
        "name": ff.find_elements_by_name
    }

    ff.get(URI)
    elements = FIND[METH](TAG)
    for i in elements:
        print i.get_attribute("href")
    print len(elements)
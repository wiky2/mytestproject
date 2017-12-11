import codecs
import sys
from lxml import etree

def readFile(file, decoding):
    html = ''
    try:
        html = open(file).read().decode(decoding)
    except:
        pass
    return html

def extract(file, decoding, xpath):
    html = readFile(file, decoding)
    tree = etree.HTML(html)
    return tree.xpath(xpath)

if __name__ == '__main__':
    sections = extract('peak.txt', 'utf-8', "//h3//a[@class='toc-backref']")
    for title in sections:
        print title.text
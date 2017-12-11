#-*- encoding:utf-8 -*-
#!/depot/Python-2.5/bin/pytho
from lxml import *
import lxml.html as H

#tables=[]
doc = H.document_fromstring(s)#返回rootnode
tables=doc.xpath("//")  #Package lxml :: Module etree :: Class _Element 
print tables



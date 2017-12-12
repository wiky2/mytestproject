import libxml2, sys

doc = libxml2.parseFile("libxml2-api.xml")
if doc.name != "libxml2-api.xml":
    print "doc.name failed"
    sys.exit(1)
else:
    print doc.name
root = doc.children
if root.name != "api":
    print "root.name failed"
    sys.exit(1)
else:
    print root.name
child = root.children
if child.name != "files":
    print "child.name failed"
    sys.exit(1)
else:
    print child.name
doc.freeDoc()

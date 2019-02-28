import re
def replace(filename):
    with open (filename, 'r+' ) as f:
        content = f.read()
    content_new = re.sub('not(.*)poor', 'good', content)
    with open (filename, 'w' ) as f1:
        f1.write(content_new)
        
replace("abc.txt")





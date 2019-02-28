import re
def correction(line):
    string = re.sub(r'(?<=[.,])(?=[^\s])', r' ', line)
    string = string.replace('and','&')
    return string
print(correction(' Hello,I am raj.I am good in presentations and dancing.Thank You.'))

import re
def clean(f):
    text=""
    with open(f, 'r') as file:
        text = file.read().replace('\n', '')
    print(text)
    print('\n')
    x = re.sub("http://\S+|https://\S+",'',text)
    x = re.sub("\s+", '_', x)
    x = re.sub("\W", '', x)
    x = re.sub("_", ' ', x)
    x=x.lower()
    print(x)

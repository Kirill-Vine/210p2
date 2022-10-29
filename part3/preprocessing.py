"""
use createNewFile(f)
f = file name
1. Program opens a text file
2. Reads and removes all characters that are not words or whitespace, extra whitespace between words, and all website links
3. Converts all the words to lowercase
4. Removes stopwords from the file stopwords.txt
5. Reduces all words to their root form by removing suffixes -ly, -ing, and -ment
6. Creates and writes into a new file with the prefix preproc_ followed by the original file name
"""
import re
def clean(f): #clean
    text=""
    with open(f, 'r') as file:
        text = file.read().replace('\n', ' ')
    x = re.sub("http://\S+|https://\S+",'',text)
    x = re.sub("[^a-zA-Z0-9_\s]", '', x)
    x = re.sub("\s+", '@', x)
    x = re.sub("@+", ' ', x)
    x=x.lower()
    file.close()
    return x
def rsw(f): #remove stopwords
    sw = open("stopwords.txt", "r")
    lst=[]
    for i in sw:
        lst.append(i.strip('\n'))
    x=re.split('\s',f)
    ct=0
    y=list()
    for i in x:
        if i not in lst:
            y.append(i)
    sw.close()
    return y
def sal(f): #Stemming and Lemmatization
    x=list()
    for i in f:
        x.append(re.sub('ing$','',i)) if re.search('ing$',i) else x.append(re.sub('ly$','',i)) if re.search('ly$',i) else x.append(re.sub('ment$','',i)) if re.search('ment$',i) else x.append(i)
    return ' '.join(x)
def createNewFile(f): #f=input file name
    name = 'preproc_'+f
    nf=open(name,'w')
    nf.write(sal(rsw(clean(f))))
    nf.close()

# read in files for cleaning    
def readManifest(manifest):
    # read from in tfidf_docs.txt
    # this file is a manifest of the documents used in the following code
    for line in open(manifest, 'r'):
        file = line.strip('\n')
        createNewFile(file)
              
# Main method
def main():
    readManifest("tfidf_docs.txt")

main()

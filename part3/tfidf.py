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
import math

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
        
        

def wordFreq(manifest):
    # open each preproc_file.txt in manifest
    documents = {}
    for line in open(manifest, 'r'):
        file = line.strip('\n')
        file = f'preproc_{file}'
        # doc is the current working preprocessed text document
        doc = open(file, 'r').read()
        # count word frequencies
        words = doc.split(' ')
        frequencies = {}
        for word in words:
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1
                
        documents[file] = frequencies
    return documents


    
    

def termFreq(manifest):
    documents = wordFreq(manifest)
    docTF = {}
    for doc, terms in documents.items():
        preProcDoc = open(doc, 'r').read()
        totalTerms = len(preProcDoc.split(' '))
        tfDct = {}
        for term, count in terms.items():
            tf = count / totalTerms
            tfDct[term] = tf
        docTF[doc] = tfDct
    return docTF
    
def calcidf(manifest):
    docTF = termFreq(manifest)
    totalDocs = len(docTF)
    docIDF = {}
    for doc, terms in docTF.items():
        iDF = {}
        for term, tf in terms.items():
            docCount = 0
            for document, t in docTF.items():
                if term in t:
                    docCount += 1
            iDF[term] = math.log((totalDocs) / (docCount)) + 1
        docIDF[doc] = iDF
    return docIDF
    
def tfidf(manifest):
    docIDF = calcidf(manifest)
    docTF = termFreq(manifest)
    docTfidScores = {}
    
    for doc, terms in docIDF.items():
        tfidScore = {}
        for term, idf in terms.items():
            tfidScore[term] = round(idf * docTF[doc][term], 2)
        docTfidScores[doc] = tfidScore
    return docTfidScores
    
def createNewtTFIDF(f, contents): #f=input file name
    name = 'tfidf_'+f
    nf=open(name,'w')
    nf.write(contents)
    nf.close()

    
def printTop5(manifest):
    docTfidScores = tfidf(manifest)
    for doc, scores in docTfidScores.items():
        top5 = []
        scoresSort = dict(sorted(scores.items(), key=lambda item: (-item[1], item[0])))
        i = 0
        for term, score in scoresSort.items():
            top5.append((term, score))
            i += 1
            if i == 5:
                break
        createNewtTFIDF(re.sub('preproc_', '', doc), str(top5))
# Main method
def main():
    # Preprocessing step
    # inputs manifest ("tfidf_docx.txt) then preprocesses each file name in manifest
    readManifest("tfidf_docs.txt")
    # computes tfidf on preprocessed files generated it previous step
    ''' 
    inputs "tfidf_docs.txt" and adds "preproc_" to the beginning of 
    each file name in order to call each preprocessed file in manifest
    wrties to file name with "tfidf_" appended to the beginning of the file name
    '''
    printTop5("tfidf_docs.txt")
    
main()

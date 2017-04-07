###autor: Rennan de Lucena Gaio###

#a biblioteca do nltk e urllib2 devem ser instaladas antes de usar esse programa

import nltk
import sys


#devo complementar o codigo para conseguir ver os possiveis padroes de um defacement
#em vez de usar black list, utilizar a estrutura do html

def getHTML (url):
	import urllib2
	pageTxt = urllib2.urlopen(url).read()
	return pageTxt


#uma versao alternativa para outra compatibilidade 
#para instalar o beautifulsoup: sudo pip install beautifulsoup4
def getHTMLBeautify (url):
	from bs4 import BeautifulSoup
	import requests

	response = requests.get(url)

	soup = BeautifulSoup(response.content, "html.parser")

	return soup

def extractCleanHTML (tagList):
	cleanList = []
	count = len(tagList)
	index = 0

	while (count-index)>0:
		while tagList[index]==".":
			index+=1

		while (index<count)and(tagList[index]=="<"):
			index+=1
			while (tagList[index]!=">"):
				index+=1
			index+=1
		
		if (index<count):
			cleanList.append(tagList[index])
			index+=1
	return cleanList


def createTagList (allowedPhrases):
	#obtem os tokens, separados por frase
	tokensPerPhrase = []
	for phrase in allowedPhrases:
		tokensPerPhrase.append(nltk.word_tokenize(phrase))

	#gera uma lista com todos os tokens do texto
	tokens = []
	for phrase in tokensPerPhrase:
		for token in phrase:
			tokens.append(token)

	#obtem a classificacao gramatica das palavras
	#listaTagsRuim = nltk.pos_tag(tokens)

	#gera uma lista de classificacoes mais facil de mexer
	#listaTagsBoa = []
	#for par in listaTagsRuim:
	#	listaTagsBoa.append([str(par[0]),str(par[1])])
	#return listaTagsBoa
	return tokens


def correctFile (raw):	
	raw=raw.replace(b'\xc2\xa0', b' ')
	raw=raw.replace(b'\xe2\x80\x93', b', ')
	raw=raw.replace(b'\xc3\xaf', b'i')
	raw=raw.replace(b'\xc4\x87', b'c')
	raw=raw.replace(b'\xe2\x80\x8b', b' ')
	raw=raw.replace(b'\xc3\xa7', b'c')
	raw=raw.replace(b'\xc3\xa1', b'a')
	raw=raw.replace(b'\xe2\x80\x94', b' - ')
	raw=raw.replace(b'\xe2\x80\x95', b', ')
	raw=raw.replace(b'\xe2\x80\x99', b"'")
	raw=raw.replace(b'\xc3\xbe', b'b')
	raw=raw.replace(b'\xc3\xba', b'u')
	raw=raw.replace(b'\xc3\xad', b'i')
	raw=raw.replace(b'\xc3\xb3', b'o')
	raw=raw.replace(b'\xc3\xb6', b'o')
	raw=raw.replace(b'\xc3\x9e', b'p')
	raw=raw.replace(b'\xc3\xbd', b'y')
	raw=raw.replace(b'\xc3\xb8', b'o')
	raw=raw.replace(b'\xe2\x80\x9c', b'"')
	raw=raw.replace(b'\xe2\x80\x9d', b'"')
	raw=raw.replace(b'\xc3\xa6', b'ae')



reload(sys)
sys.setdefaultencoding('cp860')

blacklist=['hacked', 'hack', 'hackers', 'lulzsec', 'anonymous', 'teamp0ison', 'teampoison', 'thejester', 'th3j35t3r', 'a-team']

#abre o arquivo
#arquivo = open('teste.txt')
if len(sys.argv) < 2:
	print "Usage: python " + sys.argv[0] + " <site's URL>"
else:
	raw = getHTML(sys.argv[1])

	#print raw

	#tira caracteres especiais que podem existir no html
	correctFile(raw)

	#obtem o segmentador de sentencas
	sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

	#separa as frases do texto
	badPhrases = sent_tokenizer.tokenize(raw)

	#cria a lista de tokens do texto
	tokens = createTagList(badPhrases)

	tokens = extractCleanHTML(tokens)

	count = 0

	#tenho q transformar essa parte do codigo no analisador
	for word in tokens:
		if word.lower() in blacklist:
			print 'hacked! '+word
			count += 1
	if count == 0:
		print '"safe"'
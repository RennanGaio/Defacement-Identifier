###autor: Rennan de Lucena Gaio###

#a biblioteca do nltk e urllib2 devem ser instaladas antes de usar esse programa

import nltk
import sys


#devo complementar o codigo para conseguir ver os possiveis padroes de um defacement
#em vez de usar black list, utilizar a estrutura do html

def extraiHTML (url):
	import urllib2

	paginaTxt = urllib2.urlopen(url).read()

	return paginaTxt

def limpaHTML (listaDeTags):
	listaLimpa=[]
	cont=len(listaDeTags)
	index = 0

	while (cont-index)>0:
		while listaDeTags[index]==".":
			index+=1

		while (index<cont)and(listaDeTags[index]=="<"):
			index+=1
			while (listaDeTags[index]!=">"):
				index+=1
			index+=1
		
		if (index<cont):
			listaLimpa.append(listaDeTags[index])
			index+=1
	return listaLimpa


def criaListaTags (listaFrasesBoa):
	#obtem os tokens, separados por frase
	tokensPorFrase = []
	for frase in listaFrasesBoa:
		tokensPorFrase.append(nltk.word_tokenize(frase))

	#gera uma lista com todos os tokens do texto
	tokensGeral = []
	for frase in tokensPorFrase:
		for token in frase:
			tokensGeral.append(token)

	#obtem a classificacao gramatica das palavras
	#listaTagsRuim = nltk.pos_tag(tokensGeral)

	#gera uma lista de classificacoes mais facil de mexer
	#listaTagsBoa = []
	#for par in listaTagsRuim:
	#	listaTagsBoa.append([str(par[0]),str(par[1])])
	#return listaTagsBoa
	return tokensGeral


def trataArquivo (raw):	
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
	print 'como usar: python <nome do programa> <ULR do site>'
else:
	raw = extraiHTML(sys.argv[1])

	print raw

	#tira caracteres especiais que podem existir no html
	trataArquivo(raw)

	#obtem o segmentador de sentencas
	sent_tokenizer=nltk.data.load("tokenizers/punkt/english.pickle")

	#separa as frases do texto
	listaFrasesRuim = sent_tokenizer.tokenize(raw)

	#cria a lista de tokens do texto
	tokensGeral=criaListaTags(listaFrasesRuim)

	tokensGeral= limpaHTML(tokensGeral)

	for word in tokensGeral:
		if word.lower() in blacklist:
			print 'hacked! '+word
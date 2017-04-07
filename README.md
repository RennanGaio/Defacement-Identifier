# Defacement-Identifier

Authors: Rennan de Lucena Gaio & João Luis da Silva Guio Soares

## pre-install

### install packages 
  ```
  sudo pip install nltk
  sudo pip install urllib2
  ```
  or: 
  ```
  sudo bash requirements.sh  
  ```

  The NLTK punkt english package is needed as the tokenizer.
  ```python
  python
  import nltk
  nltk.download()
  ```
  Use the GUI to download the punkt model.
## usage
  execute: python path/to/app.py URL

## return
 'hacked + word identified' - if site may be hacked
 
 "safe" - if site may be ok
  
  

# Surveillance in the COVID-19 Pandemic: An Analysis of Digital Contact-tracing in East Asian Countries

## About This Project
We collected hundreds of thousands of news articles from liberal and conservative news media across five countries: the United States, South Korea, Taiwan, Hong Kong, and Singapore. Working with three different languages (English, Korean, and Chinese), we aimed to analyze the contact-tracing efforts of East Asian countries in comparison to those of the United States. We wanted to understand how each country viewed contact tracing as an effective means of predicting and controlling the disease in the context of some of its harmful consequences, such as infringement of privacy and potential misuse of information.

This project is part of the Big Data Studies Lab, a research group at Seoul National University.

## Organization
There are five folders, one for each country. In each country is a Jupyter notebook with the same name as the country. This is the main notebook with all of the code.

The `data` folder includes the raw scraped text from the news articles, as well as the cleaned and processed text.

The `models` folder includes the vectors included in the models for topic modeling.

The `proc` folder includes the document term matrix, the node lists, and the edge lists. 

The optional `scripts` folder includes additional scripts I may have used in the scraping process.

## Methodology
All notebooks are arranged in a similar fashion:
1. Data Collection (scraping)
2. Data Cleaning and Tokenizing
3. Topic Modeling
4. Network Semantic Analysis of Topics

## Tools

### Scraping
* BeautifulSoup4
* FakeUserAgent
* Python requests

### Data Cleaning and Processing
* [KoNLPy](https://konlpy.org/en/latest/) (Korean morpheme tokenizer and Part-of-speech tagger)
* [Soylemma](https://pypi.org/project/soylemma/) (Korean lemmatizer)
* [Korean stop words](https://github.com/stopwords-iso/stopwords-ko)
* [Jieba](https://github.com/fxsjy/jieba) (Chinese)
* [nltk](https://www.nltk.org/) (English stop words, lemmatizer, stemmer)

### Topic Modeling
* [sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html) (NMF, TFIDF)

### Misc.
* networkx
* matplotlib


## News Sources and Search Terms
The following are the news sources and search terms used for each country.
Date range used: January 01, 2020 to the end of June.

### South Korea

* Search terms: `코로나`, `COVID-19`
* Newspapers: [조선일보](http://www.chosun.com/), [중앙일보](https://joongang.joins.com/), [동아일보](https://www.donga.com/), [한겨레](http://www.hani.co.kr/), [경향신문](http://www.khan.co.kr/)
* These were scraped the top results from the [Naver News](https://news.naver.com/) portal.


### United States of America

* Search terms: `COVID-19`, `coronavirus`
* Newspapers: [CNN](https://edition.cnn.com/), [Fox](https://www.foxnews.com/), [New York Times](https://www.nytimes.com/), [Washington Post](https://www.washingtonpost.com/), [Breitbart](https://www.breitbart.com/), [Daily Caller](https://dailycaller.com/)


### Hong Kong
* Chinese search terms: `COVID-19`, `新冠肺炎`
* Chinese Newspapers: [Oriental Daily News (東方日報)](https://orientaldaily.on.cc/), [Ming Pao (明報)](https://www.mingpao.com/), [Sing Tao Daily (星島日報)](https://std.stheadline.com/)
* English search terms: `COVID-19`, `coronavirus`
* English Newspapers: [South China Morning Post’s (SCMP)](https://www.scmp.com/news/hong-kong), [Hong Kong Free Press](https://hongkongfp.com/)


### Taiwan
* Search terms: `COVID-19`, `新冠肺炎`
* Newspapers: [United Daily News](https://udn.com/news/index), [China Times](https://www.chinatimes.com/?chdtv), [Liberty Times](https://www.ltn.com.tw/), [Apple Daily](https://tw.appledaily.com/)



### Singapore
* Search terms: `COVID-19`, `coronavirus`
* [The Straits Times](https://www.straitstimes.com/), [The New Paper](https://www.tnp.sg/)



## Useful Articles

* [Topic Modeling with LDA and NMF on the ABC News Headlines dataset](https://medium.com/ml2vec/topic-modeling-is-an-unsupervised-learning-approach-to-clustering-documents-to-discover-topics-fdfbf30e27df)
* [Topic Modeling and Latent Dirichlet Allocation (LDA) in Python](https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24)
* [Mining English and Korean text with Python](https://www.lucypark.kr/courses/2015-ba/text-mining.html)
* [데이터 사이언스](https://ehfgk78.github.io/2018/01/23/DataScience08-KoNLPy/) - on using KoNLPy
* [말뭉치를 이용한 한국어 용언 분석기](https://lovit.github.io/nlp/2019/01/22/trained_kor_lemmatizer/) - Lemmatizing Korean by using Part-Of-Speech tagging




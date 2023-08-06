from newspaper import Article, ArticleException
import TextSummarisation as ts

def extract_text(url1):
    news_article=Article(url1,language='en')
    news_article.download()
    news_article.parse()
    ltext=news_article.text

    return ltext

url='https://timesofindia.indiatimes.com/india/sitting-at-right-place-amit-shah-as-he-shares-stage-with-maharashtra-deputy-cm-ajit-pawar/articleshow/102478068.cms'
text2=extract_text(url)
output=ts.summarize(text2)


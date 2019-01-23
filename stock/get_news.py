from datetime import datetime, timedelta
import requests


def get_news(input_key_word):

    news=list()

    python_date_from = datetime.today()+timedelta(days=-21)

    url_key_word = input_key_word
    url_date_from = str(python_date_from.year)+"-" + \
        str(python_date_from.month)+"-"+str(python_date_from.day)
    apiKey = "7919d88a858c4e3596ba7d7d24eb99fa"

    url = 'https://newsapi.org/v2/everything?q='+url_key_word +"&sortBy=relevancy&apiKey="+apiKey
    json_data = requests.get(url).json()

    for article in json_data["articles"][:9]:
        
        title=[article["title"],article['url']]
        source=article["source"]['name']
        description=article["description"]
        date=article["publishedAt"][5:10]
        
        news.append({
            "title":title,
            "source":source,
            "description":description,
            "date":date,
            })
    return news

if __name__ == '__main__':
    """
    An article(element) in articles:
    {
    'source': {'id': 'techcrunch', 'name': 'TechCrunch'}, 
    'author': 'Natasha Lomas', 
    'title': 'Apple Pay is coming to Target, Taco Bell, Speedway and two other U.S. chains', 
    'description': 'A little more retail momentum for Apple Pay: Apple has announced another clutch of U.S. retailers will soon support its eponymous mobile payment tech — most notably discount retailer Target. Apple Pay is rolling out to Target stores now, according to Apple, w…', 
    'url': 'http://techcrunch.com/2019/01/22/apple-pay-is-coming-to-target-taco-bell-speedway-and-two-other-u-s-chains/', 
    'urlToImage': 'https://techcrunch.com/wp-content/uploads/2019/01/Apple-Pay-coming-to-partners-Customer-checking-out-with-Apple-Pay-at-Target-01222019.jpg?w=608', 
    'publishedAt': '2019-01-22T14:38:39Z', 
    'content': 'A little more retail momentum for Apple Pay: Apple has announced another clutch of U.S. retailers will soon support its eponymous mobile payment tech — most notably discount retailer Target.\r\nApple Pay is rolling out to Target stores now, according to Apple, … [+1502 chars]'
    }
    """

    print(get_news("PROSHARES ULTRAPRO SHORT QQQ"))

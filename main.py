import requests
import bs4
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.143 Safari/537.36'
}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    art = article.text.split(sep=' ')
    for keyword in KEYWORDS:
        data__ = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs["title"]
        title = article.find("h2").find("span").text
        href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        link = base_url + href
        if keyword in art:
            print(f' {keyword}<дата> {data__} - <заголовок> - {title} - <ссылка> - {link}')
        else:
            response = requests.get(link, headers=HEADERS)
            text_ = response.text
            soup = bs4.BeautifulSoup(text_, features='html.parser')
            article_ = soup.find(id="post-content-body")
            art_ = article_.text.split(sep=' ')
            if keyword in art_:
                print(f'<дата> {data__} - <заголовок> - {title} - <ссылка> - {link}')

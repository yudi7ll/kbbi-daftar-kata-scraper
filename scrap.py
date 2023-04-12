import requests
from bs4 import BeautifulSoup


def fetchHtml(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def main():
    page = "1"
    last_page = "106"
    base_url = "https://www.kbbi.co.id/daftar-kata?page="

    open('daftar_kata.txt', 'w').write('')
    f = open('daftar_kata.txt', 'a')

    for i in range(int(page), int(last_page)+1):
        wordlists = []
        ul_list = fetchHtml(base_url + page).findAll('div', class_="row")

        for ul in ul_list:
            li_list = ul.findAll('li')
            for li in li_list:
                wordlists.append(li.text)

        for word in wordlists:
            f.write(word + "\n")

        print("appending page {} wordlist".format(page))
        page = str(int(page) + 1)

    print('done')
    f.close()


main()

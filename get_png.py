from bs4 import BeautifulSoup
import requests
import os


def download_file(path, url):
    filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    with open(os.path.join(path, filename), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)


def get_pic(url):
    # url = 'https://store.line.me/stickershop/product/6153/zh-Hant'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    is_animation = True

    pic_urls = []
    for tag in soup.find_all("span"):
        if u'style' not in tag.attrs:
            continue
        style = tag['style']
        l_p = style.rfind('(') + 1
        r_p = style.rfind(')')
        sticker = style[l_p:r_p]
        if is_animation:
            pic_urls.append(sticker.replace("/stickers", "/animation"))
    title = soup.title.text.split()[0]

    if not os.path.exists(title):
        os.mkdir(title)

    download_dir = os.path.join(os.getcwd(), title)
    for url in pic_urls:
        download_file(download_dir, url)

if __name__ == '__main__':
    # main()
    pass
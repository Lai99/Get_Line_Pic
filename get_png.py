from bs4 import BeautifulSoup
import requests
import os
import time


def download_file(path, url):
    filename = url.split("/")[-1]
    r = requests.get(url, stream=True)
    with open(os.path.join(path, filename), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)


def get_pic(url, check):
    """
        get_pic(url) -> Get url and parse the html content then to find the tag <span> which also have
                                attribute 'style'. From the tag text to get the picture url and download the pics
                                in folder with the name 'title'
        """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    is_animation = check

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
        else:
            pic_urls.append(sticker)

    if len(pic_urls) == 0:
        print "Find no picture to download"
        return 1

    title = soup.title.text.split()[0]

    if not os.path.exists(title):
        os.mkdir(title)

    download_dir = os.path.join(os.getcwd(), title)
    for url in pic_urls:
        download_file(download_dir, url)
        time.sleep(0.1)

if __name__ == '__main__':
    # main()
    pass
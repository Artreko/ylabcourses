from urllib.parse import urlparse


def domain_name(url):
    return urlparse(url).hostname.split('.')[-2]


def main():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


if __name__ == '__main__':
    main()
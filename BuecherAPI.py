import requests
from bs4 import BeautifulSoup

class BuecherGrabber:
    def __init__(self, isbn):
        self.isbn = isbn
        self.book_details = {}
        self.artikel_url = None
        
    def __getattr__(self, key):
        if key in self.book_details:
            return self.book_details[key]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")

    def get_description_text(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        product_description = soup.find('div', class_='col-md-9 col-sm-8 col-xs-12', attrs={'data-behavior': 'productDescLong'})
        if product_description:
            description_text = ''
            for elem in product_description.contents:
                if elem.name == 'br':
                    break
                elif isinstance(elem, str):
                    description_text += elem.strip()
            self.book_details.update({'beschreibung': description_text})
        else:
            self.book_details.update({'beschreibung': 'N/A'})

    def get_product_details(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        product_details = soup.find('div', class_='hidden-xxs hidden-xs col-sm-4 col-md-3 product-details')
        if product_details:
            details_list = product_details.find('ul', class_='plain product-details-list')
            if details_list:
                for detail in details_list.find_all('li', class_='product-details-value'):
                    try:
                        key, value = map(str.strip, detail.get_text().split(':', 1))
                        self.book_details[key.lower()] = value
                    except:
                        continue

    def get_table_of_content(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        col_xs_12_div = soup.find_all('div', class_='col-xs-12')
        self.book_details.update({'inhaltsverzeichnis': col_xs_12_div[-1].text.strip()})

    def grab_info(self):
        self.checker()
        self.get_description_text()
        self.get_product_details()
        self.get_table_of_content()

    def print_info(self):
        for key, value in self.book_details.items():
            print(f"{key.capitalize()}: {value}\n=================================================")
        if self.artikel_url:
            print(f"Artikel URL: {self.artikel_url}\n=================================================")

    def checker(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.buecher.de','DNT': '1','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Sec-GPC': '1','TE': 'trailers'}
        data = {'form[rubrik]': '24', 'form[q]': self.isbn}
        response = requests.post('https://www.buecher.de/ni/search_search/quick_search/receiver_object/shop_search_quicksearch/',headers=headers, data=data)
        if response.status_code == 200:
            self.html = response.text
            self.artikel_url = response.url
            return True
        else:
            return False


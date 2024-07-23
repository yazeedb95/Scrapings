
import requests
from bs4 import BeautifulSoup
import csv

from tqdm import tqdm
import time

def get_allURLS():
# for loop to get all pages
    links = []
    for pages in tqdm(range(1, 841)):   
        if pages == 1:
            URL = 'https://jo.opensooq.com/en/find?PostSearch[categoryId]=7713&PostSearch[subCategoryId]=7715'
        else:
            URL = f'https://jo.opensooq.com/en/find?page={pages}&PostSearch[categoryId]=7713&PostSearch[subCategoryId]=7715'

        page = requests.get(URL)
        
        src = page.content
        soup = BeautifulSoup(src, 'html.parser')

        countaners = soup.find_all('div', {'class': 'pt-16'})[0]
        len_countaners = len(countaners)
        
        
        for link in soup.find_all("a", {"class": 'flex flexNoWrap p-16 blackColor radius-8 grayHoverBg ripple boxShadow2 relative'}):
            links.append(link.get("href"))
            
        

    for i in links:
        with open('openSooq_links.txt', 'a', encoding='utf-8-sig') as f:
            f.write(f"https://jo.opensooq.com{str(i)}\n")
        
    print('file created')
    print(len(links))

def main(): 
    
    get_allURLS()
    
if __name__ == '__main__':
    main()
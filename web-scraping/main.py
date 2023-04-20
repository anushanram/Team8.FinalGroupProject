from bs4 import BeautifulSoup
from Web_Scraping import Web_Scraping
from datetime import datetime
import requests, math, logging, os

# get total number of pages 
def get_number_of_pages(url):
    logging.info("get total number of pages function")
    response = requests.get(url).text
    # parsing - lxml
    soup = BeautifulSoup(response,'lxml')
    num_results = int(soup.find("span", class_ = "total-filter-count").text.split()[0].replace(',',''))
    page_size = 100
    return math.ceil(num_results/page_size)

# retrieve data from the URL
def get_data(url):
    logging.info("get data from url function")
    response = requests.get(url).text
    # parsing - lxml
    soup = BeautifulSoup(response,'lxml')
    return soup

def main():
    # Logging format
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path,'log/app_Log')
    logging.basicConfig(filename=file_name,level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s %(lineno)d %(message)s')

    # read environment variables
    db_host = os.environ['DB_HOST']
    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']
    db = os.environ['DB']
    table = os.environ['DB_TABLE']

    url = "https://www.cars.com/shopping/results/?list_price_max=&makes[]=&maximum_distance=20&models[]=&page={}&page_size=100&stock_type=all&zip=14174"
    soups = []

    # get total number of pages
    num_pages = get_number_of_pages(url.format(1))

    for page_index in range(1,num_pages+1):
        soup = get_data(url.format(page_index))
        logging.info("received {} page!".format(page_index))
        soups.append(soup)

    # loop through each soup
    logging.info("loop through each soup")
    for soup in soups:
        # initalize web-scraping-class
        scraping_obj = Web_Scraping(soup,db_host,db_user,db_password,db,table)
        scraping_obj.get_car_details()

if __name__ == "__main__":
    # get today date
    date = datetime.today().strftime('%Y-%m-%d')
    print("{} web-scraping started ....".format(date))
    logging.info("{} web-scraping started....".format(date))

    main()

    print("{} web-scraping completed".format(date))
    logging.info("{} web-scraping completed".format(date))






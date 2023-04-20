from MySQL_DB import MySQL_DB
from bs4 import BeautifulSoup
from datetime import datetime
import logging

class Web_Scraping:
    def __init__(self,soup,db_host,db_user,db_password,db,table):
        logging.info("web scraping class")
        self.soup = soup
        self.cards = self.soup.find_all("div", class_ = "vehicle-card")
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db = db
        self.table = table
    
    def get_car_details(self):
        logging.info("get car details function")
        # instantiate mysql connection
        db_obj = MySQL_DB(self.db_host,self.db_user,self.db_password,self.db)

        # loop through each card
        logging.info("loop through each card in the soup")
        for card in self.cards:
            details = card.find("div", class_ = "vehicle-details")
            
            # get car name
            try:
                logging.info("get car year, make and model")
                name = details.a.h2.text
                year = name.split()[0]
                make = name.split()[1]
                model = " ".join(name.split()[2:])
            except Exception as e:
                logging.info("filed to acquire year,make and model" + str(e))
                year, make, model = None, None, None
            
            # get mileage
            try:
                mileage = details.find("div", class_ = "mileage").text.split()[0].replace(',','')
            except Exception as e:
                logging.info("filed to acquire mileage" + str(e))
                mileage = None

            # get car condition
            try:
                condition = details.find("p", class_ = "stock-type").text
            except Exception as e:
                logging.info("filed to acquire car candition" + str(e))
                condition = None

            # get car price
            try:
                price = details.find("span", class_ = "primary-price").text[1:].replace(',','')
            except Exception as e:
                logging.info("filed to acquire car price" + str(e))
                price = None

            # get dealer
            try:
                dealer = details.find("div", class_ = "dealer-name").text[1:-1]
            except Exception as e:
                logging.info("filed to acquire car dealer: " + str(e))
                dealer = None

            # dealer ratings
            try:
                dealer_rating = details.find("span", class_ = "sds-rating__count").text
            except Exception as e:
                logging.info("filed to acquire dealer ratings: " + str(e))
                dealer_rating = None

            # dealer rating count 
            try:
                dealer_rating_count = details.find("span", class_ = "sds-rating__link sds-button-link").text[1:-1].split()[0]
            except Exception as e:
                logging.info("filed to acquire dealer rating count: " + str(e))
                dealer_rating_count = None

            # enter the record
            logging.info("record- {} {} {} {} {} {} {} {} {}".format(year,make,model,mileage,condition,dealer,dealer_rating,dealer_rating_count,price))
            try:
                # get today date
                date = datetime.today().strftime('%Y-%m-%d')
                db_obj.add_record(self.table,date,year,make,model,mileage,condition,dealer,dealer_rating,dealer_rating_count,int(price))
            except Exception as e:
                logging.info("filed to add record: " + str(e))


# html_text = requests.get('https://www.cars.com/shopping/results/?list_price_max=&makes[]=&maximum_distance=20&models[]=&page=1&page_size=100&stock_type=all&zip=14174').text
# # # instantiate Beautifulsoup object
# # # parser - lxml
# soup = BeautifulSoup(html_text,'lxml')
# obj = Web_Scraping(soup)
# obj.get_car_details()

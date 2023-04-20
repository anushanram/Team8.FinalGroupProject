import mysql.connector, logging

class MySQL_DB:
    def __init__(self, host, user, password, database):
        logging.info("mysql db connection")
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(host = host,
             user = user,
             password = password,
             database = database,
             auth_plugin='mysql_native_password')
        
    def close_connection(self):
        logging.info("db connection closing function")
        self.connection.close()

    def get_databases(self):
        logging.info("get databases function")
        cursor = self.connection.cursor()
        query = """SHOW DATABASES;"""
        cursor.execute(query)
        databases = cursor.fetchall()

        return databases
    
    def add_record(self,table_name,date,year,make,model,mileage,car_condition,dealer,dealer_rating,dealer_rating_count,price):
        logging.info("add record function")
        cursor = self.connection.cursor()
        # Execute the query
        query = """INSERT INTO `{}` (date,year,make,model,mileage,car_condition,dealer,dealer_rating,dealer_rating_count,price) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""".format(table_name)
        val = (date,year,make,model,mileage,car_condition,dealer,dealer_rating,dealer_rating_count,price)
        
        cursor.execute(query, val)
        self.connection.commit()
        logging.info("new record entered successfully")
        

# db_obj = MySQL_DB('34.130.29.75','root','crs.123','bdat1004')
# print(db_obj.get_databases())
# db_obj.add_record('cars','2023-04-07','2017','Kia','Picanto',35000,'used','KIA Lanka',4.8,1000,20000)


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

    def get_selected_date_car_models(self,table_name,date):
        logging.info("get selected date car models function")
        cursor = self.connection.cursor()

        # Execute the query
        query = """SELECT make, COUNT(*) as count FROM `{}` WHERE date='{}' GROUP BY make;""".format(table_name,date)

        cursor.execute(query)
        records = cursor.fetchall()
        return records
    
    def get_all_dates_car_models(self,table_name):
        logging.info("get all dates car models function")
        cursor = self.connection.cursor()
        # Execute the query
        query = """SELECT make, COUNT(*) as count FROM `{}` GROUP BY make;""".format(table_name)

        cursor.execute(query)
        records = cursor.fetchall()
        return records
    
    def get_selected_date_car_conditions(self,table_name,date):
        logging.info("get selected date car conditions function")
        cursor = self.connection.cursor()

        # Execute the query
        query = """SELECT car_condition, COUNT(*) as count FROM `{}` WHERE date='{}' GROUP BY car_condition;""".format(table_name,date)

        cursor.execute(query)
        records = cursor.fetchall()
        return records
        
    def get_all_dates_car_conditions(self,table_name):
        logging.info("get all dates car conditions function")
        cursor = self.connection.cursor()
        # Execute the query
        query = """SELECT car_condition, COUNT(*) as count FROM `{}` GROUP BY car_condition;""".format(table_name)

        cursor.execute(query)
        records = cursor.fetchall()
        return records
        

# print(db_obj.get_databases())
# db_obj.add_record('cars','2023-04-07','2017','Kia','Picanto',35000,'used','KIA Lanka',4.8,1000,20000)
# print(db_obj.get_last_day_car_models())
# db_obj.get_last_day_car_models()
# print(db_obj.get_all_dates_car_models('cars'))
# print(db_obj.get_selected_date_car_models('cars','2023-04-17'))
# print(db_obj.get_all_dates_car_conditions('cars'))
# print(db_obj.get_selected_date_car_conditions('cars','2023-04-17'))

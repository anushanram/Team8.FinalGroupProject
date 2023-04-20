import mysql.connector, logging, datetime

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
    
    def get_all_items(self,table):
        logging.info("get all items function")
        cursor = self.connection.cursor()

        # Execute the query
        cursor.execute('SELECT * FROM {}.{};'.format(self.database,table))
        records = cursor.fetchall()

        # Convert list of tuples into list of lists
        list_of_lists = [list(elem) for elem in records]

        # all records
        records = []

        # Creating dictionary
        for row in list_of_lists:
            data = {}
            data['id'] = row[0]
            data['date'] = row[1].strftime('%Y-%m-%d')
            data['year'] = row[2]
            data['make'] = row[3]
            data['model'] = row[4]
            data['mileage'] = row[5]
            data['car_condition'] = row[6]
            data['dealer'] = row[7]
            data['dealer_rating'] = row[8]
            data['dealer_rating_count'] = row[9]
            data['price($)'] = row[10]
            records.append(data)

        return records
    
    def get_items_by_make(self,table,make):
        logging.info("get items by make function")
        cursor = self.connection.cursor()

        # Execute the query
        cursor.execute("""SELECT * FROM {}.{} WHERE make='{}';""".format(self.database,table,make))
        records = cursor.fetchall()

        # Convert list of tuples into list of lists
        list_of_lists = [list(elem) for elem in records]

        # all records
        records = []

        # Creating dictionary
        for row in list_of_lists:
            data = {}
            data['id'] = row[0]
            data['date'] = row[1].strftime('%Y-%m-%d')
            data['year'] = row[2]
            data['make'] = row[3]
            data['model'] = row[4]
            data['mileage'] = row[5]
            data['car_condition'] = row[6]
            data['dealer'] = row[7]
            data['dealer_rating'] = row[8]
            data['dealer_rating_count'] = row[9]
            data['price($)'] = row[10]
            records.append(data)

        return records
    
    def get_items_by_id(self,table,id):
        logging.info("get items by id function")
        cursor = self.connection.cursor()

        # Execute the query
        cursor.execute("""SELECT * FROM {}.{} WHERE id='{}';""".format(self.database,table,id))
        records = cursor.fetchall()

        # Convert list of tuples into list of lists
        list_of_lists = [list(elem) for elem in records]

        # all records
        records = []

        # Creating dictionary
        for row in list_of_lists:
            data = {}
            data['id'] = row[0]
            data['date'] = row[1].strftime('%Y-%m-%d')
            data['year'] = row[2]
            data['make'] = row[3]
            data['model'] = row[4]
            data['mileage'] = row[5]
            data['car_condition'] = row[6]
            data['dealer'] = row[7]
            data['dealer_rating'] = row[8]
            data['dealer_rating_count'] = row[9]
            data['price($)'] = row[10]
            records.append(data)

        return records[0]
    
    def get_record_count(self,table):
        logging.info("get record count function")
        cursor = self.connection.cursor()
        query = """SELECT COUNT(*) FROM {}.{};""".format(self.database,table)
        cursor.execute(query)
        count = cursor.fetchall()
        return count[0][0]
    
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
# print(db_obj.get_all_items('cars'))
# print(db_obj.get_items_by_make('cars','Toyota'))
# print(db_obj.get_items_by_id('cars',22))
# print(db_obj.get_record_count('cars'))

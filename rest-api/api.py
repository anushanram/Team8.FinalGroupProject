from waitress import serve
from flask import Flask, render_template
from flask_restx import Api, Resource, fields
from get_post_cors import get_post_cors
from MySQL_DB import MySQL_DB
import os,logging

app = Flask(__name__)
api = Api(app, version='1.0V', title='cars.com API')

# Logging format
logging.basicConfig(filename='log/app_Log',level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s %(lineno)d %(message)s')

# Namespaces
carsns = api.namespace('api/v1/car', description='cars')

# read environment variables
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db = os.environ['DB']
table = os.environ['DB_TABLE']

@carsns.route('')
class Get_All_Cars(Resource):
    def get(self):
        try:
            # Instantiate DB instance
            db_obj = MySQL_DB(db_host,db_user,db_password,db)
            records = db_obj.get_all_items(table)
            db_obj.close_connection()
           
            return records, 200    # No need to jsonify here
        except Exception:
            return get_post_cors({'result':'internal server error'},500)

@carsns.route('/get-by-make/<string:make>')
class Get_Cars_By_Make(Resource):
    def get(self,make):
        try:
            # Instantiate DB instance
            db_obj = MySQL_DB(db_host,db_user,db_password,db)
            records = db_obj.get_items_by_make(table,make)
            db_obj.close_connection()
           
            return records, 200    # No need to jsonify here
        except Exception:
            return get_post_cors({'result':'internal server error'},500)
        
@carsns.route('/get-by-id/<int:id>')
class Get_Cars_By_Id(Resource):
    def get(self,id):
        try:
            # Instantiate DB instance
            db_obj = MySQL_DB(db_host,db_user,db_password,db)
            records = db_obj.get_items_by_id(table,id)
            db_obj.close_connection()
           
            return records, 200    # No need to jsonify here
        except Exception:
            return get_post_cors({'result':'internal server error'},500)
        
@carsns.route('/get-record-count')
class Get_Record_Count(Resource):
    def get(self):
        try:
            # Instantiate DB instance
            db_obj = MySQL_DB(db_host,db_user,db_password,db)
            num_records = db_obj.get_record_count(table)
            db_obj.close_connection()
           
            return {"count": num_records}, 200    # No need to jsonify here
        except Exception:
            return get_post_cors({'result':'internal server error'},500)

# main driver function
if __name__ == '__main__':
 
    serve(app,host="0.0.0.0",port="5000")


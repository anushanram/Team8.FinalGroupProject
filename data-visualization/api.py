from waitress import serve
from flask import Flask, render_template
from MySQL_DB import MySQL_DB
import json,logging,os

# logging format
logging.basicConfig(filename='log/app_Log',level=logging.INFO, format='%(asctime)s [%(levelname)s] %(filename)s %(lineno)d %(message)s')

app = Flask(__name__)

# read environment variables
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB = os.environ['DB']
TABLE = os.environ['DB_TABLE']

@app.route('/')
def visualize_all_dates():
    logging.info("visualize all dates endpoint")

    # instantiate MySQL class
    db_obj = MySQL_DB(DB_HOST,DB_USER,DB_PASSWORD,DB)
    # for car make
    df1 = db_obj.get_all_dates_car_models(TABLE)
    # for car condition
    df2 = db_obj.get_all_dates_car_conditions(TABLE)

    tempdata = json.dumps({'type':"All time",'make':df1,'condition':df2})

    return render_template('index.html', tempdata=tempdata)

@app.route('/<string:date>')
def visualize_selected_date(date):
    logging.info("visulize selected date endpoint")

    # instantiate MySQL class
    db_obj = MySQL_DB(DB_HOST,DB_USER,DB_PASSWORD,DB)

    # for car make
    df1 = db_obj.get_selected_date_car_models(TABLE,date)
    # for car condition
    df2 = db_obj.get_selected_date_car_conditions(TABLE,date)

    tempdata = json.dumps({'type':"{}".format(date),'make':df1,'condition':df2})

    return render_template('index.html', tempdata=tempdata)


if __name__ == '__main__':
    serve(app,host="0.0.0.0",port="5001")
    # app.run()


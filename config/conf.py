import os

GY_API_URL = 'http://api.yansl.com:8084'

GY_DB_URL = {                               
    'host': 'qa.guoyasoft.com',             
    'port': 3306,                           
    'db': 'guoya_virtual_mall_1811',        
    'user': 'root',                         
    'passwd': 'Guoya006',                   
    'charset': 'utf8'                       
}											
FILE_PATH = os.path.join(os.path.dirname(__file__), "../data")
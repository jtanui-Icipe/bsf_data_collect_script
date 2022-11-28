# importing the requests library
import requests
import time
from datetime import date
import requests
import schedule
import time

import csv




# defining the api-endpoint of KOBO
API_ENDPOINT = "https://bsf_larvae_data"

icipe = "https://api.init.st/data/v1/events/latest?accessKey=ist_JILmv8kZlwpR0TUk_7b0ZVlv9QAMsQr2&bucketKey=55862636050916269000000000"
sanergy = "https://api.init.st/data/v1/events/latest?accessKey=ist_JILmv8kZlwpR0TUk_7b0ZVlv9QAMsQr2&bucketKey=55862636050914983000000000"
zihang = "https://api.init.st/data/v1/events/latest?accessKey=ist_JILmv8kZlwpR0TUk_7b0ZVlv9QAMsQr2&bucketKey=55862636050916269000000000"

APIs = [icipe,sanergy,zihang]
farmer = ""




def fetch_data():

 for API in range(3):
   
    #get data from Synefa API    
    js = requests.get(APIs[API]).json()
    #print(js)
   
    if(API == 0):
        farmer = "icipe"
    elif(API == 1):
        farmer = "sanergy"
    elif(API == 2):
        farmer = "zihang"

    # your API key here
    #API_KEY = "XXXXXXXXXXXXXXXXX"
   
    my_date = date.today().strftime("%Y/%m/%d")
    my_time = time.strftime("%H:%M:%S", time.localtime())
   
    try:
        # data to be sent to api
        data = {
            'farmer': farmer,
            'Record_ID_system_date': my_date,
            'Record_ID_system_time': my_time,    
            'AIR_HUMIDITY': list(js['AIR_HUMIDITY'].values())[0],
            'AIR_TEMPERATURE': list(js['AIR_TEMPERATURE'].values())[0],
            'CARBON_DIOXIDE': list(js['CARBON_DIOXIDE'].values())[0],
            'EVENT': list(js['EVENT'].values())[0],
            'LIGHT_INTENSITY': list(js['LIGHT_INTENSITY'].values())[0],
            'SHIELD_BATTERY_LEVEL': list(js['SHIELD_BATTERY_LEVEL'].values())[0],
            'SHIELD_FW_VERSION': list(js['SHIELD_FW_VERSION'].values())[0],
            'SHIELD_ID': list(js['SHIELD_ID'].values())[0],
            'SOIL_MOISTURE': list(js['SOIL_MOISTURE'].values())[0],
            'SOIL_NITROGEN': list(js['SOIL_NITROGEN'].values())[0],
            'SOIL_PHOSPHOROUS': list(js['SOIL_PHOSPHOROUS'].values())[0],
            'SOIL_POTASSIUM': list(js['SOIL_POTASSIUM'].values())[0],
            'SOIL_TEMPERATURE': list(js['SOIL_TEMPERATURE'].values())[0],
            'SPEAR_BATTERY_LEVEL': list(js['SPEAR_BATTERY_LEVEL'].values())[0],
            'SPEAR_DATA': list(js['SPEAR_DATA'].values())[0],
            'SPEAR_FW_VERSION': list(js['SPEAR_FW_VERSION'].values())[0],
            'SPEAR_ID': list(js['SPEAR_ID'].values())[0],
            'STORE_TIMESTAMP_DATE': list(js['STORE_TIMESTAMP'].values())[0].split(',')[0],
            'Store_timestamp_time': list(js['STORE_TIMESTAMP'].values())[0].split(',')[1],    
            'VALVE_POSITION': list(js['VALVE_POSITION'].values())[0],
            'WATER_DISPENSED': list(js['WATER_DISPENSED'].values())[0]
            }

        #print("Data to be posted \n")
        #print(data)
   
        # list of column names
        field_names = ['farmer','Record_ID_system_date','Record_ID_system_time','AIR_HUMIDITY','AIR_TEMPERATURE','CARBON_DIOXIDE','EVENT','LIGHT_INTENSITY','SHIELD_BATTERY_LEVEL','SHIELD_FW_VERSION','SHIELD_ID','SOIL_MOISTURE','SOIL_NITROGEN','SOIL_PHOSPHOROUS','SOIL_POTASSIUM','SOIL_TEMPERATURE','SPEAR_BATTERY_LEVEL','SPEAR_DATA','SPEAR_FW_VERSION','SPEAR_ID','STORE_TIMESTAMP_DATE','Store_timestamp_time','VALVE_POSITION','WATER_DISPENSED']      
       
        with open('./data/data_iots.csv','a') as fd:
            a = list(data.values())              
            a_str = ''
                 
            for b in range(len(a)):
                a_str = a_str + a[b] + ','
                #print(a_str)
               
            fd.write(a_str + '\n')
            print("Data POST executed successfully")
           
        #requests.post(url = API_ENDPOINT, data = data)
        #print("POST executed successfully")
       
    except Exception as  e:
       
        # list of column names
        #field_names = ['farmer','system_date','system_time','device_date','device_time','error_message']
       
        data = {
            'farmer': farmer,
            'system_date': my_date,
            'system_time': my_time,  
            'device_date': list(js['STORE_TIMESTAMP'].values())[0].split(',')[0],
            'device_time': list(js['STORE_TIMESTAMP'].values())[0].split(',')[1],
            'error_message': str(e)
            }
       
        with open('./data/data_iots_error_log.csv','a') as fd:
            a = list(data.values())
            #print(a)    
            fd.write(str(a[0]) + ',' + str(a[1]) + ',' + str(a[2]) + ',' + str(a[3]) + ',' + str(a[4]) + ',' + str(a[5]) + '\n')
            print("Error POST NOT successful")

#CronJob

#fetch_data()

schedule.every().hour.at(":25").do(fetch_data)
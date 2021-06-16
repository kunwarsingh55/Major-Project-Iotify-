import requests #Handels all out GET/POST requests
import json     #Handles Json data
import serial   #For serial communication with arduino
import time
import asyncio
import threading

'''
Tasks:
 Check Connection (Handshake with Server)
 Routine GET request to server to check for changes.
 Routine POST request to server to update ParkingData

'''


url = 'http://127.0.0.1:8000/dataExchange/'
port = input('Enter Port :')


#Parse Json Data
def parseJson(content):
    stuff = str(content.content,'utf-8')
    contentAsJson = json.loads(stuff)
    return contentAsJson

#Gets data from arduino and send to Server
def connectionCheck():
    handShakeURL = url + 'handshake/'
    run = True
    handShake = False
    while run == True:
        if handShake is False:
            try:
                handShakeSession = requests.session()
                response = parseJson(handShakeSession.get(handShakeURL))
                if response is not None and response['message'] == 'OK':
                    print('\n\nHandshake Successful\n\n')
                    handShake = True
                    run = False
            except:
                print('Cannot Connect...')
                
        time.sleep(5)
    return handShake
        
#Get latest sensor data from arduino                
def getArduinoData():

    '''
    arduinoConnection = False
    port = port
    port_path = '/dev/tty/' + port 

    while arduinoConnection == False:
        try:
            arduino = serial.Serial(port,9600)
            arduinoConnection = True
        except:
            print('Error in getting data from the arduino')

        time.sleep(3)
    '''
    #Format for arduino to send -> E@F@F
    serialData = 'E@F@F'                             #str(arduino.readline(), 'utf-8')
    serialDataList = serialData.split('@')
    arduinoData = {
                    'Spot_1' : str(serialDataList[0]),
                    'Spot_2' : str(serialDataList[1]),
                    'Spot_3' : str(serialDataList[2]) 
                    }

    return arduinoData

#Send Parking Data
def sendParkingData():
    requestSent = False
    postURL = url + 'piData/'
    while requestSent == False:
        try:
            print('\n\nChecking Connection...\n\n')
            if connectionCheck():
                print('\n\n Connection OK \n\n Now Trting to Send Data...\n\n')
                postRequestSession = requests.session()
                print(getArduinoData())
                postResponse = parseJson(postRequestSession.post(postURL, getArduinoData()))
                print('\n\n','Data Sent, Server Response : ',postResponse,'\n\n')
                requestSent = True
            else:
                raise Exception ('No Good')
        except:
            print('Error Sending data')
        time.sleep(4)



sendParkingData()

'''


def read_post_data(url, port):

    run = True
    handshake = False
    uno = False
    port_path = '/dev/tty' + port
    

    #arduino = serial.Serial('/dev/ttyUSB1', 9600)
    
    pi_session = requests.session()


    while run is True:
        if handshake is False:
            try:
                print("Trying Handshake...")

                #Try to Connect to API

                handshake = True

            except:
                print('Cannot make handshake')
                

        if handshake is True and uno is False:
            try:
                print("\n\nHandshake Successful...")
                print("Now trying to connect to arduino...")
                arduino = serial.Serial(port_path, 9600)
                uno = True
            except:
                print('Cannot get data from arduino')


        if handshake is True and uno is True:

            line = str(arduino.readline(), 'utf-8')
            line_content1 = line.split()
            line_content2 = line_content1[0].split('@')
            
            moisture = line_content2[1]
            temperature = line_content2[3]
            humidity = line_content2[5]

            print('Data From Arduino : ',moisture,temperature,humidity)

            

            payload = {'data':'SensorData','moisture':moisture,'temperature':temperature,'humidity':humidity,'time_stamp':timee, 'csrfmiddlewaretoken':csrftoken}

            try:
                post_response = pi_session.post(url, data=payload)
                post_response_str = str(post_response.content, 'utf-8')
                post_response_json = json.loads(post_response_str)
                print(post_response_json)
            except:
                print('Cannot POST data')
                handshake = False
                uno = False

        time.sleep(5)




if __name__ == "__main__":

    t1 = threading.Thread(target=read_post_data, args=('http://192.168.8.121:8080/dashboard/pidata', 'USB0' ))
    #read_post_data(url= 'http://192.168.43.135:8080/dashboard/pidata', port='USB0')
    t1.start()
    asyncio.get_event_loop().run_until_complete(control())
    #t1.join()


'''
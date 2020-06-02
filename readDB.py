import requests
class ReadDB:
    def __init__(self,numAnalog,numDigital,url,offset):
        self.numAnalog = numAnalog
        self.numDigital = numDigital
        self.url = url
        self.offset = offset
        self.regData = [0]*numAnalog
        self.coilData = [0]*numDigital
	
    def updateData(self):
        try:
            responseDB = requests.get(self.url+'lastvalues/')
            # convert json -> list
            data = responseDB.json()
            # xu ly du lieu tung kenh
            for index in data:
                # xac dinh loai sensor: D, A
                sensorType = index['dhunittype']

                # xac dinh kenh sensor
                dataLen = len(index['_id'])
                sensorChannel = int(index['_id'][33:dataLen])

                # kiem tra loai sensor
                if sensorType == 'D':
                    # neu digital=> ghi du lieu vao list coil
                   # print('Digital Type')
                    if len(index['v'])>0:
                        self.coilData[sensorChannel] = int(index['v'])
                    else:
                        self.coilData[sensorChannel] = 0
                else:
                    # neu analog=> convert value
                 #   print('Analog Type')
                    # tim out_min, out_min, in_min, in_max, offset, D qua api 

                    # tinh D
                    D = float(index['v'])
                    # tim dhunitid
                    sensorUnitId = index['dhunitid']

                    # request toi db
                    try:
                        resDhUnit = requests.get(self.url+'dhunit/'+sensorUnitId)
                        dataUnit = resDhUnit.json()

                        #  tinh out_min, out_min, in_min, in_max, offset
                        input_max = int(dataUnit['variable']['output_max'])
                        input_min = int(dataUnit['variable']['output_min'])
                        # config = int(dataUnit['variable']['off_set'])
                        output_max = 65535
                        output_min = 0
			
                        #  convert du lieu
                        value = round((output_min-output_max)/(input_min-input_max)*(D-input_min)+output_min+ self.offset)
                        self.regData[sensorChannel] = value
                    except requests.exceptions.ConnectionError as err:
                        print('error request dhunit', err)
                        self.regData[sensorChannel] = 0

        except requests.exceptions.ConnectionError as errc:
            print("error request lastvalues:", errc)
            self.regData = [0]*self.numAnalog
            self.coilData = [0]*self.numDigital

        print('regedit value: ',self.regData)
        print('coil value: ', self.coilData)
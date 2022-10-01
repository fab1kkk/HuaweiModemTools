from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection

def getDeviceSignal():

    with Connection('http://admin:pwd@192.168.8.1/') as connection:
        client = Client(connection)

        #print(client.device.signal())
        #print(client.device.information())

        return client.device.signal()
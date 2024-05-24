import requests
import time
import random
from datetime import datetime




class TemperatureSensor:
  def __init__(self, sensorID, period):
    self.sensorID = sensorID
    self.period = period

    self.startUploading()

  def startUploading(self):
  
    while True:
      metric_value = random.randint(10, 30)
      iso_format = datetime.now().isoformat()

      response = requests.post("http://localhost:3001/api/updatesensormetric", json={
        "parentSensorID": self.sensorID,
        "metricValue": metric_value,
        "metricTime": iso_format
      }).json()
      print(response, metric_value, iso_format)
      
      time.sleep(self.period)
      
  


mytempsensor = TemperatureSensor(
  sensorID="6650fe04923e39e761b438b9",
  period=2
)




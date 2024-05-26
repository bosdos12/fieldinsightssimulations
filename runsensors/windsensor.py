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
      metric_value = random.randint(5, 50)
      iso_format = datetime.now().isoformat()
      response = requests.post("http://localhost:3001/api/updatesensormetric", json={
        "parentSensorID": self.sensorID,
        "metricValue": metric_value,
        "metricTime": iso_format
      }).json()
      print(response, metric_value, iso_format)
      time.sleep(self.period)
mytempsensor = TemperatureSensor(
  sensorID="windsensorrr",
  period=2
)




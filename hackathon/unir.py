import http.client
import csv
import json
import datetime

def cityToCode(city):
    with open('airport-codes.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if city in row[0]:
                return(row[1])

def Airline(origin, destination, departDate, returnDate):
  conn = http.client.HTTPSConnection("skyscanner-skyscanner-flight-search-v1.p.rapidapi.com")

  headers = {
      'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
      'x-rapidapi-key': "abe99dabacmsh557148920e4cf9ap1144cbjsnc8e110192d67"
      }
  departDate = datetime.datetime.strptime(departDate, "%m/%d/%Y").strftime("%Y-%m-%d")
  returnDate = datetime.datetime.strptime(returnDate, "%m/%d/%Y").strftime("%Y-%m-%d")
  orig = origin
  orig = cityToCode(orig)
  dest = destination
  dest = cityToCode(dest)
  depart = departDate
  comeBack = returnDate

  """ 
    orig = "SFO"
    dest = "JFK"
    depart = "2020-04-01"
    comeBack = "2020-05-01"
  """

  conn.request("GET", "/apiservices/browsequotes/v1.0/US/USD/en-US/" + orig + "-sky/" + dest + "-sky/" + depart + "?inboundpartialdate=" + comeBack, headers=headers)

  res = conn.getresponse()
  data = res.read()
  data = data.decode("utf-8")

  print(data)

  data_dict = json.loads(data)

  price = data_dict["Quotes"][0]["MinPrice"]
  id = data_dict["Quotes"][0]["OutboundLeg"]["CarrierIds"][0]
  for carrier in data_dict["Carriers"]:
    if carrier["CarrierId"] == id:
      name = carrier["Name"]
  #print(data_dict["Quotes"][0]["MinPrice"])
  #print(data_dict)

  return(name, price)


print(Airline("San Francisco", "New York", "04/01/2020", "05/01/2020"))

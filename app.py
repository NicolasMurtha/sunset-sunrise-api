from flask import Flask, request, jsonify
from flask_restful import Api
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/plan-activity', methods=['POST'])
def search_data ():

 data = request.get_json()
 lat = data.get('latitude')
 lng = data.get('longitude')
 date = data.get('date')
 tzid = "America/Sao_Paulo"

 data = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}&tzid={tzid}")
 response_json = data.json()

 sunrise_time = response_json['results']['sunrise']
 sunset_time = response_json['results']['sunset']
 day_length = response_json['results']['day_length']

 activities = [
 f"caminhada ao nascer do sol às {sunrise_time}",
 "piquenique durante o dia",
 f"fotografia ao pôr do sol às {sunset_time}",
 "observação das estrelas após o por do sol"
 ]

 return jsonify({
  'sunrise' : sunrise_time,
  'sunset' : sunset_time,
  'activities' : activities,
  'day_length' : day_length
 })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)


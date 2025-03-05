from weather import Weather,Unit
w=Weather()
location = w.lookup_by_location('dublin')
forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)

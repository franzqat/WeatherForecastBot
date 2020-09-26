from pyowm.owm import OWM
from pyowm.utils.config import get_config_from
config_dict = get_config_from('configfile.json')
owm = OWM('TOKEN', config_dict)     
   

def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return str(arr[(val % 16)])

def getWeatherAtCoords(lat,lon):
    mgr = owm.weather_manager()  
    # = mgr.weather_at_place('Pomezia,IT')  # the observation object is a box containing a weather object
    
    observation = mgr.weather_at_coords(lat,lon) # the observation object is a box containing a weather object
    weather = observation.weather

    #print (weather.status)           # short version of status (eg. 'Rain')
    #print (weather.detailed_status) # detailed version of status (eg. 'light rain')


    curr_time = weather.reference_time('iso')
    curr_status = weather.status
    curr_detailed = weather.detailed_status

    # ---------TEMPERATURE---------

    temp_dict_celsius = weather.temperature('celsius')  # guess?

    temp = int(temp_dict_celsius['temp'])
    temp_min = int(temp_dict_celsius['temp_min'])
    temp_max = int(temp_dict_celsius['temp_max'])

    # ---------WIND---------

    wind_dict_in_knots = observation.weather.wind(unit='knots')

    wind_direction = degToCompass(wind_dict_in_knots['deg'])
    wind_speed = wind_dict_in_knots['speed']

    results = """
            Time : {}
            Status : {}
            Detailed : {}
            Temperature : {}
            Min Temperature : {}
            Max Temperature : {}
            """.format(curr_time,
                       curr_status, curr_detailed, temp, temp_min, temp_max)


    return results
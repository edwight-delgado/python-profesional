from datetime import datetime
import pytz

def time_zone(zone):
	bogota_timezone = pytz.timezone(zone)
	bogota_date = datetime.now(bogota_timezone)
	return(zone, bogota_date.strftime('%d/%m/%Y , %H:%M:%S'))

my_zone = ('America/Bogota','America/Mexico_City','America/Caracas','Europe/Lisbon','Europe/Berlin')

res = [time_zone(zone) for zone in my_zone]
print(res)
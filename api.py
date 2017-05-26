import requests

def start():

	parameters = {
		'origin': str(raw_input('Punto de partida: ')),
		'destination': str(raw_input('Destino: ')),
		'mode': str(raw_input('Como viajas? driving/walking/bicycling/transit: '))
	}

	if parameters['mode'] == 'transit':
		parameters['arrival_time'] = str(raw_input('hora de llegada:'))
		parameters['departure_time'] = str(raw_input('hora de salida:'))

	r = requests.get('https://maps.googleapis.com/maps/api/directions/json', parameters).json()
	print '--no hay resultados--' if r['status'] == 'ZERO_RESULTS' else showInfo(r)

def showInfo(data):
	print '--------------------------------'
	print 'Punto de partida: ' + data['routes'][0]['legs'][0]['start_address']
	print 'Destino: ' + data['routes'][0]['legs'][0]['end_address']
	print 'Distancia: ' + data['routes'][0]['legs'][0]['distance']['text']
	print 'El viaje dura ' + data['routes'][0]['legs'][0]['duration']['text']
	print '--------------------------------'
	if str(raw_input('Quieres las indicaciones? S/N ')) == 's': showIndications(data['routes'][0]['legs'][0]['steps'])

def showIndications(steps):
	print '--------------------------------\n(presione enter para continuar)'
	for step in steps:
		print step['html_instructions']
		print step['distance']['text'] + ', ' + step['duration']['text']
		raw_input()
	print '--------------------------------\nHa llegado a su destino. Gracias por usar Google Maps!'
start()
def requestData():
	datos = {
		'nombre': str(input('Cual es tu nombre?')),
		'ap_pa': str(input('Cual es tu apellido paterno?')),
		'ap_ma': str(input('Cual es tu apellido materno?')),
		'edad': str(input('Cual es tu edad? ')),
		'sexo': str(input('Cual es tu sexo? M/F')),

		'familia': {
			'padres': {
				'padre': {
					'nombre': str(input('Cual es el nombre de tu padre?')),
					'edad': int(input('Que edad tiene?'))
				},
				'madre': {
					'nombre': str(input('Cual es el nombre de tu madre?')),
					'edad': int(input('Que edad tiene?'))
				}
			},
			'hermanos': {}
		}
	}

	no_hermanos = int(input('cuantos hermanos tienes?'))
	if no_hermanos != 0:
		hermanos = {}
		for h in range(0, no_hermanos):
			nombre = str(input('Como se llama tu herman@'))
			hermanos[nombre] = {
				'ap_pa': datos['ap_pa'],
				'ap_ma': datos['ap_ma'],
				'edad': int(input('Que edad tiene?'))
			}
		datos['familia']['hermanos'] = hermanos

	return datos

print(requestData())
def winner(candidates):
	scores = []
	if len(candidates) != 3:  # Si no hay 3 jugadores
		return False
	for c in candidates:
		if 'name' not in c or 'scores' not in c:  # si tiene nombre
			return False
		if len(c['scores']) != 1 and len(c['scores']) != 2:  # si tiene tiros diferente de 1 o 2
			return False
		for score in c['scores']:
			if score%5 != 0:
				return False
			if score > 100:
				return False
		if sum(c['scores']) > 100:
			return False
		if sum(c['scores']) <= 100:
			scores.append(sum(c['scores']))
		else:
			scores.append(0)

	winner  = candidates[scores.index(max(scores))]
	return winner['name']
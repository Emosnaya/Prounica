from classPokemon import Pokemon

charmander = Pokemon('Charmander', 4, 'Fuego', '0.6m', '8.5kg', 'H/M', 'Lagartija', 10, 4, 5)
squirtle = Pokemon('Squirtle', 7, 'Agua', '0.5m', '9kg', 'H/M', 'Tortuguita', 10, 4, 5 )

peleadores = {
    1 : charmander.nombre,
    2 : squirtle.nombre
}

for clave, valor in peleadores.items():
    print(f'{clave}.{valor}')

player1 = int(input('Ingrese un pokemon a pelear: '))
player2 = int(input('Ingrese el segundo pokemon: '))

print(f'Pelea entre {peleadores[player1]} y {peleadores[player2]}')



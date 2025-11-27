f1_teams = ['Mercedes', 'Ferrari', 'RedBull', 'McLaren', 'Racing Bulls', 'Alpine', 'Aston Martin', 'Williams', 'Kick Sauber', 'HAAS']
f1_drivers = ['Max Verstappen', 'Lewis Hamilton', 'Charles Leclerc', 'Lando Norris', 'Oscar Piastri', 'Yuki Tsunoda', 'George Russel', 'Kimi Antonelli', 'Oliver Bearman', 'Esteban Ocon', 'Isack Hadjar', 'Liam Lawson','Gabriel Bortoleto', 'Nico Hülkenberg', 'Fernando Alonso', 'Lance Stroll', 'Franco Colapinto', 'Pierre Gasly', 'Carlos Sainz', 'Alex Albon']

print(f1_teams[1])
print(f1_teams[-2])

print(f'{f1_teams[-3]} tymu se tento rok dari!')
print(f1_teams[1:4])

print(len(f1_drivers))

f1_teams_2026 = f1_teams.copy()
f1_teams_2026.append('Cadillac')
f1_drivers_2026 = f1_drivers.copy()
f1_drivers_2026.append('Checo Perez')
f1_drivers_2026.append('Valtteri Bottas')

print(len(f1_teams_2026))
print(len(f1_drivers_2026))

for index, team in enumerate(f1_teams_2026):
    print(f'Tym {index + 1}: {team}')


if 'Aston Martin' in f1_teams_2026:
    print('Their cars are green!')


print(f1_teams_2026.index('Racing Bulls'))

f1_teams_2026.pop(f1_teams_2026.index('HAAS'))
print(f1_teams_2026)

f1_drivers_2026.sort()
print(f1_drivers_2026)

redbull_family = (f1_drivers[0], f1_drivers[f1_drivers.index('Yuki Tsunoda')], f1_drivers[f1_drivers.index('Isack Hadjar')], f1_drivers[f1_drivers.index('Liam Lawson')])
print(redbull_family)
print(type(redbull_family))

print(redbull_family[0])
print(redbull_family[1:3])
print(len(redbull_family))
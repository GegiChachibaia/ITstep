#ამოცანა 1
def make_order(customer:str,size:str,*toppings,**extras):
    total_cost = 0
    if size.lower() == 'small':
        total_cost += 10
    elif size.lower() == 'medium':
        total_cost += 15
    elif size.lower() == 'large':
        total_cost += 20
    else:
        print('Please choose either small,meidum or large')
        return
    for topping in toppings:
        total_cost+=2

    if extras.get('delivery'):
        total_cost += 5
    print('--------------------------')
    print(f'Customer name: {customer}')
    print(f'Size: {size}')

    if toppings:
        print('Toppings:')
        for topping in toppings:
            print(f'  - {topping}')

    if extras:
        print('Extras:')
        for key, value in extras.items():
            print(f'  - {key}: {value}')

    print(f'Total cost: {total_cost}')
    print('--------------------------')
    return total_cost
make_order('Nino', 'large', 'cheese', 'olives', delivery=True,drink = 'Cola')
toppings = ['cheese', 'mushrooms', 'ham']
extras = {'delivery': False, 'note': 'No onions'}
make_order('Luka', 'medium', *toppings, **extras)

#ამოცანა 2
players = [
    {"nick": "ShadowWolf", "level": 42, "wins": 120, "losses": 30},
    {"nick": "PixelQueen", "level": 42, "wins": 95, "losses": 10},
    {"nick": "NoobMaster", "level": 7, "wins": 3, "losses": 40},
    {"nick": "DragonFly", "level": 58, "wins": 200, "losses": 100},
    {"nick": "CatLord", "level": 58, "wins": 150, "losses": 25},
]

level_sort = sorted(players, key = lambda level:(level['level'] , level['wins']),reverse=True)
winrate_sort = sorted(players, key = lambda winrate:(winrate['wins'] / (winrate['wins'] + winrate['losses'])),reverse=True)
nick_sort = sorted(players, key = lambda nickname : (len(nickname['nick']) , nickname['nick']))
print(nick_sort)
print(winrate_sort)
print(level_sort)


#ამოცანა 3
songs = [
    {"title": "Sunrise", "artist": "Luna", "duration": 215, "plays": 5400},
    {"title": "Midnight Drive", "artist": "Neon Pulse", "duration": 187, "plays": 12800},
    {"title": "Ocean Eyes", "artist": "Luna", "duration": 243, "plays": 9100},
    {"title": "Thunder", "artist": "Neon Pulse", "duration": 201, "plays": 7600},
    {"title": "Quiet Rain", "artist": "Mira", "duration": 156, "plays": 3200},
]

def show_playlist(name,*songs):
    counter = 1
    print(name)
    for song in songs:
        print(f'{counter}. {song['title']} - {song['artist']} ({song['duration']} წმ)')
        counter += 1
show_playlist('My playlist',*songs)
short_first = sorted(songs, key = lambda dur:dur['duration'])
show_playlist('Short first',*short_first)
top3 = sorted(songs ,key = lambda top: top['plays'] ,reverse=True)[:3]
show_playlist('Top 3 played',*top3)

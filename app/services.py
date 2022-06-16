class Pokemon:
    def __init__(self, name, hp, defense, att, speed, sprite, shiny_sprite, height, weight):
        self.types = []
        self.abilities = []
        self.moves = []
        self.name = name
        self.hp = hp
        self.defense = defense
        self.att = att
        self.speed = speed
        self.sprite = sprite
        self.shiny_sprite = shiny_sprite
        self.height = height
        self.weight = weight

    def disp_poke(self):
        print(f"\n{self.name.title()}- Weight- {self.weight} Height-{self.height} HP-{self.hp} Defense-{self.defense} Attack-{self.att}\n Types= {self.types}\n Abilities= {self.abilities}\n Moves= {self.moves}")
        print(f"\nSprite-{self.sprite},\n Shiny-{self.shiny_sprite}\n\n")

class Pokedex:
    def __init__(self):
        self.pokemon = {}
        
    def add_poke(self, pname):
        result = r.get("https://pokeapi.co/api/v2/pokemon/" + pname.lower())
        data = result.json()
        hp = data['stats'][0]['base_stat']
        defense = data['stats'][2]['base_stat']
        att = data['stats'][1]['base_stat']
        speed = data['stats'][5]['base_stat']
        sprite = data['sprites']['front_default']
        shiny_sprite = data['sprites']['front_shiny']
        height = data['height']
        weight = data['weight']
        
        new_poke = Pokemon(pname, hp, defense, att, speed, sprite, shiny_sprite, height, weight)
        for a in data['abilities']:
            new_poke.abilities.append(a['ability']['name'])
        for b in data['types']:
            new_poke.types.append(b['type']['name'])
        for c in data['moves']:
            new_poke.moves.append(c['move']['name'])
        for x in range(3,len(new_poke.moves)):
            new_poke.moves.pop()
        self.pokemon[pname] = new_poke
        
    def show_dex(self):
        for n in self.pokemon:
            self.pokemon[n].disp_poke()

class Move:
    def __init__(self, name):
        self.name = name
        result = r.get('https://pokeapi.co/api/v2/move/' + self.name)
        data = result.json()
        self.id = data['id']
        self.power = data['power']
        self.pp = data['pp']
        
    def disp(self):
        print(f"Name-{self.name}\tID-{self.id}\tPower-{self.power}\tPP-{self.pp}")
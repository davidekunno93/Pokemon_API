import requests

class Pokemon():
    def __init__(self, name):
        self.name = name.title()
        # url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # response = requests.get(url)
        # if response.ok:
        #     data = response.json()
    
    def test_data(self):
        url = (f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}/")
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return data
        else:
            print("The name specified is not in the Pokemon database")

# capture sprite URL
# sprite = data["sprites"]["front_shiny"]
    def sprite(self):
        self.test_data()
        data = self.test_data()
        sprite = data["sprites"]["front_shiny"]
        return sprite

# capture pokemon's name
# pokemon_name = data["name"].title()
    def pokemon_name(self):
        self.test_data()
        data = self.test_data()
        pokemon_name = data["name"].title()
        return f"*This Pokemon's name is: {pokemon_name}*"

# capture pokemon's XP
# pokemon_xp = data["base_experience"]
    def exp(self):
        self.test_data()
        data = self.test_data()
        pokemon_xp = data["base_experience"]
        return f"This Pokemon's XP is: {pokemon_xp}"

    def abilities(self):
        self.test_data()
        data = self.test_data()
        abilities = {}
        ability_list = data["abilities"]
        # abilities key is a list of indices > indices dict first key ability > ability dict {name: "", url: ""}
        for k in range(2):
            ability_name = data["abilities"][int(k)]["ability"]["name"].title()
            # response2 = url link to ability's details
            response2 = requests.get(data["abilities"][int(k)]["ability"]["url"])
            if response2.ok:
                data2 = response2.json()
                effect = data2["effect_entries"][1]["effect"]
                abilities[ability_name] = effect
        return abilities
    
    def moves(self):
        self.test_data()
        data = self.test_data()
        moves = {}
        move_list = data["moves"]
        for k in range(4):
            move_name = move_list[int(k)]["move"]["name"].title()
            response2 = requests.get(move_list[int(k)]["move"]["url"])
            if response2.ok:
                data2 = response2.json()
                move_power = data2["power"]
                moves[move_name] = move_power
        return moves

    def pokedex(self):
        all_dict = {}
        print(self.pokemon_name())
        all_dict["name"] = self.name
        all_dict["sprite"] = self.sprite()
        all_dict["abilities"] = self.abilities()
        all_dict["moves"] = self.moves()
        i = 1
        for k, v in all_dict.items():
            print(k.title(), ": ", v, sep="", end="\n\n")
        # print(all_dict, "\n")
        
MyChar = Pokemon("Charizard")
MyChar.pokedex()

# pikachu = Pokemon("Pikachu")
# pikachu.pokedex()

# pidgeotto = Pokemon("Pidgeotto")
# pidgeotto.pokedex()

# arcanine = Pokemon("Arcanine")
# arcanine.pokedex()

# zapdos = Pokemon("Zapdos")
# zapdos.pokedex()
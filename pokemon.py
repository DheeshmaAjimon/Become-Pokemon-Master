class Pokemon:
  
    def __init__(self, name, level, poke_type, max_health, current_health = 25, knocked_out = False):
        self.name = name 
        self.level = level 
        self.type = poke_type
        self.max_health = max_health
        self.health = current_health
        self.is_knocked_out = knocked_out
#if pokemon is called without attribute this returns the info about the pokemon.
    def __repr__(self):
        return ("{name} is a level {level}, {type} type pokemon. It is currently at {health} health and has a max health of {maxhealth}.".format(name = self.name, level = self.level, type= self.type, health= self.health, maxhealth= self.max_health))


#method that lowers the health of the pokemon object. If the lost is greater than the pokemon's health then the pokemon gets knocked out.
    def lose_health(self, lost):
        new_health = self.health - lost
        if new_health >0:
            self.health = new_health 
            print("{name} has lost {lost} health! {name} now has {health} health.".format(name= self.name, lost = lost, health = self.health))
        elif new_health <= 0:
            self.health = 0
            self.is_knocked_out = True
            print(self.name + " has been knocked out!")
#method restores pokemon object to max health and sets knocked out to False.
    def revive(self):
        if self.is_knocked_out == True:
            self.is_knocked_out = False
            self.health = self.max_health
            print(self.name + " has been revived!")
#restores pokemon to full health    
    def restore_max_health(self):
        self.health = self.max_health
        print(self.name + " has been restored to full health.")
#method adds to the health of the object pokemon. Cannot add more health than the max health for the pokemon.
    def gain_health(self, gain_amount):
        new_health = self.health + gain_amount
        if new_health < self.max_health:
            self.health = new_health
            print("{name} has gained {gain} health! {name} now has {health} health.".format(name = self.name, gain = gain_amount, health = self.health))
        elif new_health <= self.max_health:
            self.health = self.max_health
            print(self.name + " has been restored to full health!")
#Method that knocks out the opponent's pokemon.
    def knock_out(self, other_pokemon):
        other_pokemon.health = 0 
        other_pokemon.is_knocked_out = True
        print(other_pokemon.name + " has been knocked out!")


#Method that deals damage to the opponent's pokemon. Damage is based on the type of the pokemon and the level.
    def attack(self, other_pokemon):
        if self.is_knocked_out != True:
            damage = 0 
            if self.type == "fire":
                if other_pokemon.type == "fire":
                    damage = 0.5 * self.level
                if other_pokemon.type == "water":
                    damage = 0.5 * self.level
                if other_pokemon.type == "grass":
                    damage = 2 * self.level
            if self.type == "water":
                if other_pokemon.type == "fire":
                    damage = 2 * self.level
                if other_pokemon.type == "water":
                    damage = 0.5 * self.level
                if other_pokemon.type == "grass":
                    damage = 0.5 * self.level
            if self.type == "grass":
                if other_pokemon.type == "fire":
                    damage = 0.5 * self.level
                if other_pokemon.type == "water":
                    damage = 2 * self.level
                if other_pokemon.type == "grass":
                    damage = 0.5 * self.level
            other_pokemon.lose_health(damage)
            print( "{selfname} has dealt {othername} {damage} damage!".format(selfname= self.name, othername= other_pokemon.name, damage = damage))
        else:
            print (self.name + " is knocked out and cannot attack.")


#Trainer class allows for trainers to be created.
class Trainer:
    def __init__(self, name, pokemon, potions, current_pokemon):
        self.name = name
        self.pokemons = pokemon
        self.potions = potions
        self.current_pokemon = current_pokemon
    def __repr__(self):
        return "The trainer {name} has {pokemon} pokemon, {potions} potions, and {current} is the current pokemon.\n".format(name = self.name, pokemon = self.pokemons, potions = self.potions, current = self.current_pokemon)


#method restores max health 
    def potion(self):
        self.potions = self.potions - 1
        if self.current_pokemon.is_knocked_out == False:
            self.current_pokemon.restore_max_health()
            print(self.name + " has restored " + self.current_pokemon + " to full health.")
        elif self.current_pokemon.is_knocked_out == True:
            self.current_pokemon.revive()
            print("{name} has revived {poke}".format(name= self.name, poke= self.current_pokemon))


#method used by trainer takes their active pokemon and attacks the opponent pokemon.
    def attack_other_trainer(self, other_trainer):
        their_pokemon = other_trainer.current_pokemon
        self.current_pokemon.attack(their_pokemon)
        print(self.name + " has attacked " + other_trainer.name +"!")


#method knocks out the opponent's active pokemon.
    def knock_out_pokemon(self, other_trainer):
        their_pokemon = other_trainer.current_pokemon
        self.current_pokemon.knock_out(their_pokemon)
        print(self.name + " has attacked " + other_trainer.name +"!")


#method allows for trainer to switch their current pokemon to another pokemon in their belt as long as it is not knocked out.    
    def switch_current_pokemon(self, new_current_pokemon):
        for poke in self.pokemons:
            if poke == new_current_pokemon:
                if new_current_pokemon.is_knocked_out != True:
                    self.current_pokemon = new_current_pokemon
                    print(self.name + " has changed current pokemon to " + self.current_pokemon.name)


pok1 = Pokemon("pok1", 2, "fire", 20)
pok2 = Pokemon("pok2", 3, "water", 30)
pok3 = Pokemon("pok3", 4, "grass", 40)
pok4 = Pokemon("pok4", 4, "fire", 40)
pok5 = Pokemon("pok5", 2, "water", 20)
pok6 = Pokemon("pok6", 3, "grass", 30)

trainer1 = Trainer("trainer1", [pok1, pok3, pok6], 4, pok3)
trainer2 = Trainer("trainer2", [pok2, pok4, pok5], 4, pok4)

#Playing Pokemon!

trainer1.attack_other_trainer(trainer2)
trainer2.attack_other_trainer(trainer1)
trainer1.attack_other_trainer(trainer2)
trainer2.attack_other_trainer(trainer1)
trainer2.switch_current_pokemon(0)
trainer2.switch_current_pokemon(1)



trainer1.knock_out_pokemon(trainer2)
trainer2.potion()

print(trainer1)
print(trainer2)

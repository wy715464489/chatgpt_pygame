
class Character:
    """Represents a character in the game, either the player or an enemy."""
    
    def __init__(self, name, health, attack, deck=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.deck = deck if deck else []

    def is_alive(self):
        """Check if the character is still alive."""
        return self.health > 0

    def take_damage(self, damage):
        """Character takes damage, reducing health."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self, enemy):
        """Attack an enemy character."""
        enemy.take_damage(self.attack)

    def add_card_to_deck(self, card):
        """Add a card to the character's deck."""
        self.deck.append(card)


class Card:
    """Represents a card in the game with a specific effect."""

    def __init__(self, name, effect, power):
        self.name = name
        self.effect = effect
        self.power = power

    def apply_effect(self, caster, target):
        """Apply the card's effect."""
        if self.effect == 'heal':
            caster.health += self.power
        elif self.effect == 'damage':
            target.take_damage(self.power)

    def __str__(self):
        return f"{self.name} ({self.effect}, Power: {self.power})"


# Example setup
player = Character('Hero', 100, 10)
goblin = Character('Goblin', 30, 5)

# Create some cards
heal_card = Card('Healing Light', 'heal', 10)
fireball_card = Card('Fireball', 'damage', 15)

# Add cards to player's deck
player.add_card_to_deck(heal_card)
player.add_card_to_deck(fireball_card)

# Example of using a card from the deck
print(f'Player Health Before: {player.health}')
player.deck[0].apply_effect(player, goblin)  # Player uses the first card in the deck (Healing Light)
print(f'Player Health After: {player.health}')

# Example of combat
print(f'Goblin Health Before: {goblin.health}')
player.deck[1].apply_effect(player, goblin)  # Player uses the second card in the deck (Fireball)
print(f'Goblin Health After: {goblin.health}')

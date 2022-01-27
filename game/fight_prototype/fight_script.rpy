init python:
    class AttackType(Enum):
        LIGHT = 0
        HEAVY = 1


    class Guard(SmartEnum):
        LOW_GUARD = 0
        SEMI_GUARD = 1
        FULL_GUARD = 2


    class AttributeType(Enum):
        HEALTH = 0
        STAMINA = 1
        LIGHT_ATTACK_DAMAGE = 2
        HEAVY_ATTACK_DAMAGE = 3


    class SpecialAbilityType(Enum):
        PASSIVE = 0
        ACTIVE = 1


    class Attack:
        def __init__(self, move_type, name, damage, stamina_cost, counter_guard, images):
            self.move_type = move_type
            self.name = name
            self.damage = damage
            self.stamina_cost = stamina_cost
            self.counter_guard = counter_guard
            self.images = images
            

    class Defence:
        def __init__(self, move_type, stamina_cost):
            self.move_type = move_type
            self.stamina_cost = stamina_cost

    
    class Attribute:
        def __init__(self, type, name, value, description, passive_ability, active_ability):
            self.type = type
            self.name = name
            self.value = value
            self.description = description
            self.passive_ability = passive_ability
            self.active_ability = active_ability


    class SpecialAbility:
        def __init__(self, type, name, description):
            self.type = type
            self.name = name
            self.description = description


    class BasePlayer:
        def __init__(self, guard=None, stamina=10, health=100, attack_multiplier=1):
            self.guard = guard
            self.max_stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier
            
            self._stamina = stamina
            self._health = health

            self.attacks = {
                AttackType.LIGHT: None,
                AttackType.HEAVY: None
            }
            self.attributes = []
            self.special_abilities = []

        @property
        def stamina(self):
            return self._stamina

        @stamina.setter
        def stamina(self, value):
            self._stamina = value
            self._stamina = min(self._stamina, self.max_stamina)
            
        @property
        def health(self):
            return self._health

        @health.setter
        def health(self, value):
            self._health = value
            self._health = max(self._health, 0)

        def set_specials(self):
            for attr in self.attributes:
                if attr == 10:
                    self.special_abilities.append(attr.active_ability)
                if attr >= 5:
                    self.special_abilities.append(attr.passive_ability)

        def change_health(self, value):
            current_health = self._health
            self._health += value

            renpy.show_screen("health_bar", current_health, self._health)


    class Opponent(BasePlayer):
        def __init__(self, guard=None, stamina=10, health=100, attack_multiplier=1):
            BasePlayer.__init__(self, guard, stamina, health, attack_multiplier)

            self.guard_images = {
                Guard.FULL_GUARD: "images/v2/tomstancekick.webp",
                Guard.SEMI_GUARD: "images/v2/tomstancehook.webp",
                Guard.LOW_GUARD: "images/v2/tomstancejab.webp"
            }

        @property
        def guard_image(self):
            return self.guard_images[self.guard]

    
    class Player(BasePlayer):
        def __init__(self, guard=None, stamina=10, health=100, attack_multiplier=1):
            BasePlayer.__init__(self, guard, stamina, health, attack_multiplier)
            
            self.fury = 0
            self.moves = {
                "q": None, # light attack
                "w": None, # heavy attack
                "e": None, # semi guard
                "r": None # full guard
            }

        def set_fury(self, value, opponent):
            self.fury = value
            
            if self.fury <= 2:
                opponent.guard = Guard.FULL_GUARD
                self.fury = 0


label player_attack_turn(player_move, player, opponent):
    $ renpy.set_return_stack([])

    if isinstance(player_move.move_type, Guard):
        $ player.guard = player_move.move_type

        call opponent_attack_turn(player, opponent)

    scene expression player_move.images["start_image"]
    pause 0.5

    if player.stamina < player_move.stamina_cost:
        call opponent_attack_turn(player, opponent)

    $ player.stamina -= player_move.stamina_cost

    # Set player passive guard
    if player_move.move_type == AttackType.LIGHT:
        $ player.guard = Guard.SEMI_GUARD
    elif player_move.move_type == AttackType.HEAVY:
        $ player.guard = Guard.LOW_GUARD
        $ opponent.guard = Guard.LOW_GUARD

    # Player attack hit        
    if opponent.guard < player_move.counter_guard:
        # Player attack counter
        if opponent.guard == Guard.SEMI_GUARD:
            $ counter_attack = renpy.random.choice(opponent.attacks)

            if opponent.stamina >= counter_attack.stamina_cost:
                call screen fight_defense(counter_attack)

        # Player attack hit
        scene expression player_move.images["hit_image"]
        with vpunch

        $ opponent.change_health(-player_move.damage)

        show screen fight_popup("{} Hit".format(player_move.move_type.name))
        pause 1.0


    # Player attack blocked
    else:
        scene expression player_move.images["block_image"]
        with vpunch

        if player_move.move_type == AttackType.HEAVY:
            $ opponent.change_health(-2) # Reduced damage
            show screen fight_popup("Guard Shattered")
        else:
            $ opponent.stamina += 3
            $ player.set_fury(player.fury + 1, opponent)
            show screen fight_popup("Blocked")
        pause 1.0

    call screen fight_attack


label player_defence_turn(player_move, player, opponent_attack, opponent):
    $ renpy.set_return_stack([])

    $ opponent.stamina -= opponent_attack.stamina_cost

    # Set opponent passive guard
    if opponent_attack.move_type == AttackType.LIGHT:
        $ opponent.guard = Guard.SEMI_GUARD
    elif opponent_attack.move_type == AttackType.HEAVY:
        $ opponent.guard = Guard.LOW_GUARD

    if player_move is not None:
        ## Player Attack Moves
        if player_move.move_type == AttackType.LIGHT:
            $ player.guard = Guard.SEMI_GUARD

            # Player Counter Attack
            if opponent_attack.move_type == AttackType.HEAVY:
                call player_attack_turn(player_move, player, opponent)
        
        elif player_move.move_type == AttackType.HEAVY:
            $ player.guard = Guard.LOW_GUARD

        ## Defence Moves
        if isinstance(player_move.move_type, Guard):
            $ player.guard = player_move.move_type

    # Opponent's attack hits
    if player.guard < opponent_attack.counter_guard:
        scene expression opponent_attack.images["hit_image"]
        with vpunch

        $ player.health -= opponent_attack.damage * opponent.attack_multiplier

        show screen fight_popup("{} HIT".format(opponent_attack.move_type.name))
        pause 1

    # Opponent's attack blocked
    else:
        scene expression move.images["block_image"]
        with vpunch

        if opponent_attack.move_type == AttackType.HEAVY:
            $ player.health -= 2
            $ player.guard = Guard.LOW_GUARD
            show screen fight_popup("GUARD SHATTERED")
        else:
            $ player.stamina += 3
            show screen fight_popup("BLOCKED")
        pause 1

    call screen fight_attack


label opponent_attack_turn(player, opponent):
    $ renpy.set_return_stack([])

    if player.guard == Guard.FULL_GUARD: # Heavily favour heavy attack 
        $ p = (0.1, 0.9)
    elif opponent.attacks[AttackType.LIGHT].stamina_cost < opponent.stamina < opponent.attacks[AttackType.HEAVY].stamina_cost: # Heavily favour light attack
        $ p = (0.9, 0.1)
    else:
        $ p = (0.5, 0.5)

    $ move_type = weighted_choice((AttackType.LIGHT, AttackType.HEAVY), p=p)
    $ move = opponent.attacks[move_type]

    if move.stamina_cost < opponent.stamina:
        call screen fight_defense(move)
    else:
        $ opponent.guard = Guard.SEMI_GUARD
        $ opponent.stamina += 4
        $ player.stamina += 4
        
        call screen fight_attack


label fight_test:

    python:
        player_light_attack = Attack(AttackType.LIGHT, "Jab", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        })
        player_heavy_attack = Attack(AttackType.HEAVY, "Jab", 10, 4, Guard.FULL_GUARD, {
            "start_image": "images/v2/hook2start.webp",
            "hit_image": "images/v2/hook2pic.webp",
            "block_image": "images/v2/hook1pic.webp"
        })
        player_semi_guard = Defence(Guard.SEMI_GUARD, 2)
        player_full_guard = Defence(Guard.FULL_GUARD, 3)

        opponent_light_attack = Attack(AttackType.LIGHT, "Jab", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/tomjab.webp",
            "hit_image": "images/v2/tomjabhit.webp",
            "block_image": "images/v2/tomjabblock.webp"
        })
        opponent_heavy_attack = Attack(AttackType.HEAVY, "Jab", 10, 4, Guard.FULL_GUARD, {
            "start_image": "images/v2/tomkick.webp",
            "hit_image": "images/v2/tomkickhit.webp",
            "block_image": "images/v2/tomkickblock.webp"
        })

        opponent.attacks[AttackType.LIGHT] = opponent_light_attack
        opponent.attacks[AttackType.HEAVY] = opponent_heavy_attack

        player.moves["q"] = player_light_attack
        player.moves["w"] = player_heavy_attack
        player.moves["e"] = player_semi_guard
        player.moves["r"] = player_full_guard

        player.attributes.append(Attribute(AttributeType.HEALTH, "Health", 1, "", None, None))
        player.attributes.append(Attribute(AttributeType.STAMINA, "Stamina", 1, "", None, None))
        player.attributes.append(Attribute(AttributeType.LIGHT_ATTACK_DAMAGE, "Light Attack Damage", 1, "", None, None))
        player.attributes.append(Attribute(AttributeType.HEAVY_ATTACK_DAMAGE, "Heavy Attack Damage", 1, "", None, None))

        mc.fighter = player
    
    call screen fight_menu([
        Attack(AttackType.LIGHT, "Jab", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        }),
        Attack(AttackType.LIGHT, "Body Hook", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        }),
        Attack(AttackType.LIGHT, "Knee", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        }),
        Attack(AttackType.HEAVY, "Hook", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        }),
        Attack(AttackType.HEAVY, "Uppercut", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        }),
        Attack(AttackType.HEAVY, "Kick", 5, 2, Guard.SEMI_GUARD, {
            "start_image": "images/v2/jab2start.webp",
            "hit_image": "images/v2/jab2pic.webp",
            "block_image": "images/v2/jab1pic.webp"
        })
    ])

    label fight_start:

    show screen test_health
    show screen health_bar(100, 100)

    menu:

        "Easy":
            $ fight_reaction_time = 1.5

        "Medium":
            $ fight_reaction_time = 1

        "Hard":
            $ fight_reaction_time = 0.75

        "Impossible":
            $ fight_reaction_time = 0.5

    call screen fight_attack

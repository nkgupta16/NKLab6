class VideoGameCharacter:
    def __init__(self, health_points, stamina_points, damage):
        self.health_points = health_points
        self.stamina_points = stamina_points
        self.damage = damage

    def hits_before_stamina_depletion(self, stamina_loss_per_hit):
        if stamina_loss_per_hit <= 0:
            return float('inf')
        return self.stamina_points // stamina_loss_per_hit

    def hits_to_die(self, incoming_damage):
        if incoming_damage <= 0:
            return float('inf')
        return self.health_points // incoming_damage


class WeakEnemy(VideoGameCharacter):
    pass


class Boss(VideoGameCharacter):
    pass


# Example usage:
weak_enemy = WeakEnemy(30, 10, 5)  # 30 HP, 10 Stamina, 5 Damage
boss = Boss(300, 100, 50)  # 300 HP, 100 Stamina, 50 Damage

# Assuming each hit to the weak enemy costs 3 stamina points and deals 10 damage.
weak_enemy_hits_before_stamina_depletion = weak_enemy.hits_before_stamina_depletion(3)
weak_enemy_hits_to_die = weak_enemy.hits_to_die(10)

# Assuming each hit to the boss costs 10 stamina points and deals 30 damage.
boss_hits_before_stamina_depletion = boss.hits_before_stamina_depletion(10)
boss_hits_to_die = boss.hits_to_die(30)

print(f"The weak enemy can take {weak_enemy_hits_before_stamina_depletion} hits before running out of stamina.")
print(f"It will take {weak_enemy_hits_to_die} hits before the weak enemy dies.")

print(f"The boss can take {boss_hits_before_stamina_depletion} hits before running out of stamina.")
print(f"It will take {boss_hits_to_die} hits before the boss dies.")

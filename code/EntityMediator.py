from code.Const import WIN_HEIGHT
from code.Effects import Explosion, play_crash_sound
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top >= WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2, entity_list: list[Entity]):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True:
            is_colliding = (
                ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom
            )
            if is_colliding:
                if ent2 not in ent1.colliding_with:
                    ent1.colliding_with.add(ent2)
                    ent2.colliding_with.add(ent1)
                    crash_pos = (
                        (ent1.rect.centerx + ent2.rect.centerx) // 2,
                        (ent1.rect.centery + ent2.rect.centery) // 2,
                    )
                    entity_list.append(Explosion(crash_pos))
                    play_crash_sound()
                    if isinstance(ent1, Player):
                        ent1.health -= 1
                    else:
                        ent1.health -= ent2.damage
                    if isinstance(ent2, Player):
                        ent2.health -= 1
                    else:
                        ent2.health -= ent1.damage
                    ent1.last_dmg = ent2.name
                    ent2.last_dmg = ent1.name
                    ent1.on_hit(ent2.damage, ent2)
                    ent2.on_hit(ent1.damage, ent1)
            else:
                ent1.colliding_with.discard(ent2)
                ent2.colliding_with.discard(ent1)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2, entity_list)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                for other in entity_list:
                    other.colliding_with.discard(ent)
                entity_list.remove(ent)

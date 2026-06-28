from code.Bird import Bird
from code.Dragon import Dragon
from code.Entity import Entity

class EntityMediator():
    @staticmethod
    def verify_collision(ent1: Dragon, ent2: Bird):
        valid_interaction = False
        if isinstance(ent1, Dragon) and isinstance(ent2, Bird):
            if ent1.rect.colliderect(ent2.rect):
                valid_interaction = True
        return valid_interaction

    @staticmethod
    def process_collision(ent1: Dragon, ent2: Bird):
        if EntityMediator.verify_collision(ent1, ent2):
            ent2.health = 0
            ent1.score += 5

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                if isinstance(entity, Bird):
                    entity_list.remove(entity)
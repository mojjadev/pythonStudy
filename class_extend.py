#하나의 클래스를 만듬
#일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print(" 체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 은 파괴되었습니다.".format(self.name))
    
#파이어뱃 : 공격 유닛
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격을 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)
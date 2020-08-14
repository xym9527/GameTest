from workTwo.person import Person
import random


class TongLao(Person):

    def __init__(self, name, lv=1):

        self.personTemplate()
        super().__init__(name, lv)
        self.currentClassname = TongLao
        self.initInfo()

        self.abilityList += [self.fight_zms, self.fight_ssf]

    def personTemplate(self):
        """
        天姥人物模板基础属性
        """

        TongLao.HP = Person.HP + 500
        TongLao.MP = Person.MP + 200
        TongLao.CE = Person.CE + 50

    def showPersonInfo(self):
        """
        展示人物信息
        :return:
        """
        print(f"""{self.name} 人物基本信息:
        战斗力(CE):{self.CE}
        血量(HP):{self.HP}
        魔力值(MP):{self.MP}
        级别/级数(LV):{self.LV}
    
        技能列表：基础攻击、天山折梅手、生死符
        \n""")

    def fight_zms(self):
        """
        技能：天山折梅手，群体技能
        :return:
        """
        # 魔力值不足则施展普通攻击，否则施展天山折梅手
        fightScope = 1

        if self.tmpMP - 400 < 0:
            print("不好,魔力值不足,", end=" ")
            fightScope, tmpHurt = self.basicAttack()
        else:
            self.tmpMP -= 400  # 该技能的消耗魔力值
            tmpHurt = self.CE * random.uniform(2, 3)  # 该技能的伤害值：基础战斗力的2倍

            print(f"{self.name} 施展了群攻门派技能:天山折梅手,", end=' ')

        # 返回1代表群攻，同时该技能的伤害值
        return fightScope, tmpHurt

    def fight_ssf(self):
        """
        技能：生死符，单体技能
        :return:
        """
        # 魔力值不足则施展普通攻击，否则施展生死符
        fightScope = 0

        if self.tmpMP - 200 < 0:
            print("魔力值不足,", end=" ")
            fightScope, tmpHurt = self.basicAttack()
        else:
            self.tmpMP -= 200  # 该技能的消耗魔力值
            tmpHurt = self.CE * random.uniform(2, 4)  # 该技能的伤害值：基础战斗力的3倍

            print(f"{self.name} 施展了单体门派技能:生死符,", end=' ')

        # 返回0代表单体攻击，同时返回该技能的伤害值
        return fightScope, tmpHurt


if __name__ == '__main__':
    wyz = TongLao('无崖子', 3)
    lqs = TongLao('李秋水', 1)

    jn = wyz.put_ability()

    wyz.showPersonInfo()
    lqs.showPersonInfo()

    wyz.see_people(lqs.name)
    a, b = jn()
    lqs.takeHurts(b)

    jn = wyz.put_ability()
    wyz.see_people(lqs.name)
    a, b = jn()
    lqs.takeHurts(b)

import random


class Person:
    """
    定义普通人物的基本信息类
    """
    # 普通人物血量基础模板
    HP = 1000
    # 普通人物魔力基础模板
    MP = 500
    # 普通人物战斗力基础模板
    CE = 100

    def __init__(self, name, LV=1):
        """
        战斗力：CE（Combat Effectiveness)
        血量：HP(Health Point）
        魔力值：MP(Magic Point)
        级别/级数：LV(Level)
        :param name:
        :param LV:
        """
        self.name = name
        self.LV = int(LV)
        self.currentClassname = Person
        self.abilityList = [self.basicAttack]
        self.initInfo()

    def put_ability(self):
        """
        战斗中随机施展技能
        :return: 返回施展技能的函数对象
        """

        ability = random.choice(self.abilityList)
        return ability

    def basicAttack(self):
        """
        技能：基础攻击
        :return:
        """
        fightScope = 0
        tmpHurt = self.tmpCE
        print(f"{self.name} 施展了普通技能:基础攻击,", end=' ')

        # 返回0代表单体攻击，tmpCE代表该技能的伤害值
        return fightScope, tmpHurt

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
    
    技能列表：基础攻击
    \n""")

    def initInfo(self):
        self.CE = self.countCE()
        self.tmpCE = self.CE  # 战斗中魔力

        self.HP = self.countHP()  # 总血量
        self.tmpHP = self.HP  # 战斗中血量

        self.MP = self.countMP()  # 总魔力
        self.tmpMP = self.MP  # 战斗中魔力

    def countCE(self):
        """
        不同的级数返回不同的战斗力
        :return:
        """
        return self.currentClassname.CE * int(self.LV)

    def countHP(self):
        """
        不同的级数返回不同的血量
        :return:
        """
        return self.currentClassname.HP * int(self.LV)

    def countMP(self):
        """
        不同的级数返回不同的魔力
        :return:
        """
        return self.currentClassname.MP * int(self.LV)

    def takeHurts(self, hurt):
        """
        被攻击伤害,减去相应血量
        :param hurt:
        :return: False  代表死亡； True 代表活着
        """
        self.tmpHP -= int(hurt)
        print(f"{self.name} 受到了{int(hurt)}点击伤害")
        if self.tmpHP <= 0:
            print(f"dieInfo:{self.name}血量为0，死亡！")
            return False
        return True

    def see_people(self, name):
        """
        攻击前对话
        :param name:
        :return:
        """
        if name == '无崖子':
            print(f"{self.name}:师弟!", end=" ")
        elif name == '李秋水':
            print(f"{self.name}:呸，贱人!", end=" ")
        elif name == '丁春秋':
            print(f"{self.name}:叛徒！我杀了你!", end=" ")
        else:
            print(f"{self.name}:{name},接招吧!", end=" ")


if __name__ == '__main__':
    xiaobai = Person("小白", 1)
    xiaobai.showPersonInfo()

from workTwo.tonglao import TongLao


class XuZhu(TongLao):
    def __init__(self, name, lv=1):

        self.personTemplate()
        super().__init__(name, lv)
        self.currentClassname = XuZhu
        self.initInfo()

        self.abilityList += [self.read]

    def personTemplate(self):
        """
        虚竹人物模板基础属性
        """
        XuZhu.HP = TongLao.HP + 1000
        XuZhu.MP = TongLao.MP + 350
        XuZhu.CE = TongLao.CE + 70

    def read(self):
        """
        虚竹念经，回血
        :return:
        """
        if self.tmpHP == self.HP:
            print("罪过罪过!阿弥陀佛")
        elif self.tmpHP + 500 >= self.HP:
            self.tmpHP = self.HP
            print("罪过罪过!满血了又！")
        else:
            self.tmpHP += 500
            print("罪过罪过!补气血500点")

        # 返回2 代表不是进攻技能，0 代表0伤害
        return 2, 0

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

        技能列表：基础攻击、天山折梅手、生死符、念经
        \n""")

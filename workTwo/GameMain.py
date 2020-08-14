from workTwo.person import Person
from workTwo.tonglao import TongLao
from workTwo.xuzu import XuZhu
import random


class Game:

    def __init__(self, attacks, defenders):
        """

        :param attacks: 存储进攻方人员的列表
        :param defenders: 存储防守方人员的列表
        """
        if not attacks or not defenders:
            print("请提供参战双方人员!")

        self.attacks = attacks
        self.defenders = defenders
        self.count = 1  # 统计当前回合
        self.attacks_survive = self.attacks  # 进攻方还未死亡人员
        self.defender_survive = self.defenders  # 防守方还未死亡人员
        self.attacks_Attacked = None  # 进攻方当前被攻击人
        self.defender_Attacked = None  # 防守方当前被攻击人

    def GameFightMain(self):

        # 战斗前显示攻击双方人员名单
        self.showPartakePerson()
        # 定义首轮回合攻击双方被攻击人员
        self.attacks_Attacked = self.getAttacked(self.attacks_survive)
        self.defender_Attacked = self.getAttacked(self.defender_survive)

        while True:

            print(f"-------第{self.count}回合--------------------------------------")
            # 功方发起进攻，返回当前防守方被攻击人
            self.defender_Attacked = self.attackBehaviour(self.attacks,
                                                          self.defender_Attacked, self.defender_survive)
            # 防守方当前被攻击人为None，代表防守方失败
            if self.defender_Attacked is None:
                break

            # 防守方发起进攻，返回当前进攻方被攻击人
            self.attacks_Attacked = self.attackBehaviour(self.defenders,
                                                         self.attacks_Attacked, self.attacks_survive, False)
            # 进攻方当前被攻击人为None，代表进攻方失败
            if self.attacks_Attacked is None:
                break

            # 未结束进行下一回
            self.count += 1
            print(f"*-***********************************************************-*")

        print(f"*-*-------------------------------------------------------*-*")
        print(f"*-------------------------GAME OVER-------------------------*")
        print(f"*-*-------------------------------------------------------*-*")

    def getAttacked(self, survives):
        """
        获取彼方当前被攻击人员
        :param survives: 活着人员列表
        :return:
        """
        try:
            return random.choice(survives)
        except  IndexError as e:
            return None

    def showPartakePerson(self):
        """

        :return:
        """
        print("*****************显示参战人员************************")

        print("攻击方:")
        for attack in self.attacks:
            print(f" {attack.name}", end="")
        print("")
        print("防守方:")
        for defender in self.defenders:
            print(f" {defender.name}", end="")
        print("")
        print("****************************************************")

    def attackBehaviour(self, attacks, defender_Attacked, defender_survive, isAttack=True):
        """

        :param attacks:  当前攻击方的人员
        :param defender_Attacked: 防守方的被攻击人员
        :param defender_survive:  防守方的未死亡人员
        :param isAttack: True当前发起攻击的 是"进攻者"; False 当前发起攻击的 是"防守者"
        :return: 返回当前被攻击人
        """
        # 遍历攻方对守方的技能施展
        for attack in attacks:
            # 获取当前攻击者准备施展的技能
            jn = attack.put_ability()

            # 在攻击信息前显示攻守属性
            if isAttack:
                print("(攻)", end="")
            else:
                print("(守)", end="")

            # 攻击前对被攻击方的语言攻击
            attack.see_people(defender_Attacked.name)

            # 获取施展技能返回的范围和伤害值H
            fightScope, fightHurt = jn()
            # fightHurt=int(fightHurt)

            # fightScope为 1 代表群体攻击
            if fightScope == 1:
                # 遍历防守方幸存人员进行伤害
                for defender_Attacked in defender_survive:
                    isSurvive = defender_Attacked.takeHurts(fightHurt)
                    # 检查当前被攻击人是否死亡
                    if not isSurvive:
                        defender_survive.remove(defender_Attacked)
                        defender_Attacked = self.getAttacked(defender_survive)
                        # 获取当前被攻击人为None，代表没有活人了，isAttack 代表进攻方还是防守方
                        if defender_Attacked is None and isAttack:
                            print("防守方均已死亡，进攻方获胜！")
                            return None
                        elif defender_Attacked is None and not isAttack:
                            print("进攻方均已死亡，防守方获胜！")
                            return None

            # fightScope为 0 代表单体攻击
            elif fightScope == 0:
                isSurvive = defender_Attacked.takeHurts(fightHurt)
                if not isSurvive:
                    defender_survive.remove(defender_Attacked)
                    defender_Attacked = self.getAttacked(defender_survive)
                    if defender_Attacked is None and isAttack:
                        print("防守方均已死亡，进攻方获胜！")
                        return None

                    elif defender_Attacked is None and not isAttack:
                        print("进攻方均已死亡，防守方获胜！")
                        return None

        return defender_Attacked


if __name__ == '__main__':
    attacks = []
    defenders = []
    attack1 = Person("吴清波", 1)
    attack2 = TongLao("李秋水", 1)
    attack3 = XuZhu("虚竹", 1)
    attacks.append(attack1)
    attacks.append(attack2)
    attacks.append(attack3)

    defender1 = Person("李祥源", 5)
    defender2 = Person("袁慧慧", 4)

    defenders.append(defender1)
    defenders.append(defender2)

    theRound = Game(attacks, defenders)
    theRound.GameFightMain()

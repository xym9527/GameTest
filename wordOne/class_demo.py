# -*- coding:utf-8 -*-

"""
用类和面向对象的思想，“描述”生活中任意接触到的东西。

"""


class Car:

    def __init__(self, carModel, carBrand, carColor):
        """

        :param carModel: 车型
        :param carBrand: 车品牌
        :param carColor: 车颜色
        """
        self.carModel = carModel
        self.carBrand = carBrand
        self.carColor = carColor
        self.doorStatus = False
        self.runStatus = False

    def openDoor(self):
        if self.doorStatus:
            print("门是开着的")
        else:
            self.doorStatus = True
            print("门打开了")

    def closeDoor(self):
        if not self.doorStatus:
            print("门是关着的")
        else:
            self.doorStatus = False
            print("门已经关好了")

    def driverForward(self):
        if self.runStatus:
            print("车正在前进中")
        else:
            print("请先启动车")

    def driverBackward(self):
        if self.runStatus:
            print("请注意,正在倒车")
        else:
            print("请先启动车")

    def startUp(self):
        if self.doorStatus:
            print("门是开着的,请关闭车门后再启动")
        elif self.runStatus:
            print("车是启动着的")
        else:
            self.runStatus = True
            print("车启动成功")

    def stalls(self):
        if not self.runStatus:
            print("车没有启动")
        else:
            self.runStatus = False
            print("车熄火成功")

    def showCarInfo(self):
        print(f"这辆车型是{self.carModel},品牌是{self.carBrand},颜色是{self.carColor}")


if __name__ == '__main__':
    baoma = Car('Suv', '宝马', '白色')
    baoma.showCarInfo()
    baoma.closeDoor()
    baoma.openDoor()
    baoma.closeDoor()
    baoma.startUp()
    baoma.stalls()
    baoma.driverBackward()

# 执行测试的类
from game import  Game
import unittest

class GameTestCase(unittest.TestCase):
    """
    gui测试
    """
    def setUp(self):
        self.gameTest = Game(1300,800)

    def testWIindowSize(self):
        """
        测试宽高的宽高
        :return:
        """
        print("屏幕的宽：{}高:{}".format(self.gameTest.width,self.gameTest.height))
        self.assertEqual(self.gameTest.width,1300)
        self.assertEqual(self.gameTest.height,800)


    def testCellListNum(self):
        """
        测试cellList数量是否正常
        :return:
        """
        for i in range(3,100):
            self.gameTest.set_cell_num(i)
            print("测试用例的num：{}  期望得到的num：{}".format(len(self.gameTest.cell_list.get_cell_list()),i+2))
            self.assertEqual(len(self.gameTest.cell_list.get_cell_list()),i+2)






if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(GameTestCase("testWIindowSize"))
    suite.addTest(GameTestCase("testCellListNum"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
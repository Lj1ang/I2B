from src.convert2bitmap import Convert2Btimap

class test():
    def __init__(self):
        self.test1=Convert2Btimap(r"../img/1.png")

    def Test1(self):
        self.test1.ModifyImg()
        self.test1.Convert2Hex()
        self.test1.WriteTxt()

if __name__=='__main__':
    test=test()
    test.Test1()

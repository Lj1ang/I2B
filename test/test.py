from src.ConvertImage2Bitmap import ConvertImage2Btimap
import sys

class Test:
    def __init__(self):
        self.img_path= r"../img/1.png"

    # test basic functions
    def test1(self):
        test1= ConvertImage2Btimap(self.img_path)
        try:
            test1.ModifyImg()
            test1.Convert2Hex()
            test1.WriteTxt()
        except :
            print("test1 failed")
            sys.exit(1)
        else:
            print("test1 passed")

    # test resize
    def test2(self):
        img_size=(128, 64)
        test2= ConvertImage2Btimap(self.img_path, img_size)
        test2.ModifyImg()
        test2.Convert2Hex()
        test2.WriteTxt()
        try:
            test2.ModifyImg()
            test2.Convert2Hex()
            test2.WriteTxt()
        except:
            print("test2 failed")
            sys.exit(1)
        else:
            print("test2 passed")

        # TODO : IN ssd1306 olde screen

if __name__ == '__main__':
    test = Test()
    test.test1()
    test.test2()

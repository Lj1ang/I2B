import cv2 as cv


class ConvertImage2Btimap :

    def __init__(self, img_path: str, dst_size: tuple = None):
        self.img_path = img_path
        self.img_src = cv.imread(img_path, cv.CV_8UC1)
        self.prefix = img_path.split(r"/")[-1].split(r".")[0]
        self.dst_size=dst_size
        self.img_dst = None
        self.hex_array = []

    def ModifyImg(self) -> None:
        if self.dst_size != None:
            resize_dst=cv.resize(self.img_src, self.dst_size)
        retval, self.img_dst = cv.threshold(self.img_src, None, 1, cv.THRESH_OTSU)


    def Convert2Hex(self) -> None:
        (weight, height) = self.img_dst.shape
        cnt = 0
        val = 0
        for i in range(height):
            for j in range(weight):
                cnt += 1
                val += self.img_dst[j][i] << 1
                if cnt % 8 == 0:
                    # format :  '0x5': str --> '0x05':str
                    self.hex_array.append('0x{:02X}'.format(val))
                    val = 0

    def WriteTxt(self) -> None:
        txt = open(r"../txt/" + self.prefix + r".txt", "w")
        # TODO: format
        txt.write("[")
        for each in self.hex_array:
            txt.write(each + ", ")
        txt.write("]")
        txt.close()

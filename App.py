from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

class WritePic: 

    def __init__(self , text ,writer):

        # for linux
        # reshaped_text = arabic_reshaper.reshape(text)
        self.text = text # get_display(reshaped_text)

        reshaped_text = arabic_reshaper.reshape(writer)
        self.writer = ': ' + get_display(reshaped_text)

        self.img = Image.open ('files/pic.png')
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype('files/Vazir.ttf',35,encoding='unic')



    def find_x (self , text:str):
        return (self.img.size[0] - self.draw.textsize(text,font=self.font)[0])/2

    def find_line (self):
        strs = self.text.split(' ')

        w = self.img.size[0]
        res = ''
        i=0
        while ( i < len(strs) and self.draw.textsize(res,font=self.font)[0]+300 < w):
            if (res == ''):
                res = strs[i]
            else:
                res = res + " " + strs[i]
            i += 1

        self.text = self.text.replace(res,'')

        return res

    def find_y (self):
        temp = self.text
        s = ' '
        res =0
        while (self.text != '' and self.text != ' ' and s != '' ):
            s = self.find_line()
            res += self.draw.textsize(s,font=self.font)[1]

        self.text = temp
        return (self.img.size[1] - res)/2



    def write (self):

        t_y = self.find_y()

        s = ' '
        while (self.text != '' and self.text != ' ' and s != '' ):
            s = self.find_line()
            t_x = self.find_x(s)

            # shadow
            self.draw.text( ( t_x-5 , t_y ),s,(0,0,0),font=self.font)
            self.draw.text( ( t_x+5 , t_y ),s,(0,0,0),font=self.font)
            self.draw.text( (t_x , t_y-5 ),s,(0,0,0),font=self.font)
            self.draw.text( (t_x , t_y+5 ),s,(0,0,0),font=self.font)

            # text
            self.draw.text( (t_x, t_y),s,(255,255,255),font=self.font)

            t_y += 50

        # shadow
        w_x = self.find_x(self.writer)
        w_font = ImageFont.truetype('files/Vazir.ttf',25,encoding='unic')
        self.draw.text( (w_x-3 , 50 ),self.writer,(255,255,255),font=w_font)
        self.draw.text( (w_x+3 , 50 ),self.writer,(255,255,255),font=w_font)
        self.draw.text( (w_x , 50-3 ),self.writer,(255,255,255),font=w_font)
        self.draw.text( (w_x , 50+3 ),self.writer,(255,255,255),w_font)

        self.draw.text( (w_x,50 ),self.writer ,(255,2,2),font=w_font)

        self.img.save('files/res.webp')
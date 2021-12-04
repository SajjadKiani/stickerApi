from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

class WritePic: 
    img = Image.open ('files/pic.png')
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(35,encoding='unic')

    def __init__(self , text ,writer):
        reshaped_text = arabic_reshaper.reshape(text)
        self.text = get_display(reshaped_text)

        reshaped_text = arabic_reshaper.reshape(writer)
        self.writer = ': ' + get_display(reshaped_text)


    def find_x (self , text:str):
        return self.draw.textsize(text)[0]

    def find_line (self):
        strs = self.text.split(' ')

        w = self.img.size[0]
        res = ''
        i=0
        while ( i < len(strs) and self.draw.textsize(res)[0]+300 < w):
            if (res == ''):
                res = strs[i]
            else:
                res = res + " " + strs[i]
            i += 1

        self.text = self.text.replace(res,'')

        return res


    def write (self):

        p_x,p_y = self.img.size
        t_y = 0

        s = ' '
        while (self.text != '' and self.text != ' ' and s != '' ):
            s = self.find_line()
            t_x = self.find_x(s)

            # shadow
            self.draw.text( (((p_x - t_x)/2 )-3 , ((p_y - t_y )/2 ) ),s,(255,255,255))
            self.draw.text( (((p_x - t_x)/2 )+3 , ((p_y - t_y )/2 ) ),s,(255,255,255))
            self.draw.text( (((p_x - t_x)/2 ) , ((p_y - t_y )/2 )-3 ),s,(255,255,255))
            self.draw.text( (((p_x - t_x)/2 ) , ((p_y - t_y )/2 )+3 ),s,(255,255,255))

            # text
            self.draw.text( ((p_x - t_x)/2 , (p_y - t_y )/2 ),s,(0,0,0))

            t_y = t_y + self.draw.textsize(s)[1] + 50


        # shadow
        w_x = self.find_x(self.writer)+100
        # w_font = ImageFont.truetype(25,encoding='unic')
        self.draw.text( (w_x-3 , 50 ),self.writer,(255,255,255))
        self.draw.text( (w_x+3 , 50 ),self.writer,(255,255,255))
        self.draw.text( (w_x , 50-3 ),self.writer,(255,255,255))
        self.draw.text( (w_x , 50+3 ),self.writer,(255,255,255))

        self.draw.text( (w_x,50 ),self.writer ,(255,2,2))

        self.img.save('files/res.webp')

# if __name__=='__main__':
#     WritePic('salam','baba').write()
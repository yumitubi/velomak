# -*- coding: utf-8 -*-

import random
import Image, ImageDraw, ImageFont
from velomak.settings import DIR_CAPCHA, DIR_BLOG

class capcha(object):
    """Generate capcha for web-sites"""

    def __init__(self, num_symbols=5):
        self.lenth = num_symbols

    def rn(self, number):
        """Return random number"""
        return random.choice(range(number))

    def gen_string(self):
        """generate string for capcha"""
        chars = ('a', 'b', 'd', 'e', 'f', 'g', 'h', 'j', 'm', 'n', 'q', 'r', 't', 'u', 'y',
                  'A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'M', 'N', 'Q', 'R', 'T', 'U', 'Y',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9'
                 );
        string = ''
        for i in range(self.lenth):
            string = string + random.choice(chars)
        return string

    def gen_color(self):
        """return random color"""
        colors = ('green', 'red', 'blue', 'black')
        return random.choice(colors)

    def gen_capcha(self):
        """Generate capcha"""
        x = 7
        y = (5, 7, 9, 11, 13, 15, 17, 19)
        img = Image.new("RGB", (150, 30), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rectangle((0, 0, 150, 30), fill="white")
        string_img = self.gen_string()
        string_capcha = self.gen_string()
        font = ImageFont.truetype(DIR_BLOG + "/UbuntuMono-BI.ttf", 16)
        for char in string_capcha:
            draw.text((x, random.choice(y)), char, fill=self.gen_color(), font=font)
            draw.line([self.rn(150), self.rn(30), self.rn(150), self.rn(30)], fill=self.gen_color())
            draw.line([self.rn(150), self.rn(30), self.rn(150), self.rn(30)], fill=self.gen_color())
            x += 30
        name_capcha = DIR_CAPCHA + '/' + string_img + '.png'
        img.save(name_capcha)
        return string_img + '.png', string_capcha


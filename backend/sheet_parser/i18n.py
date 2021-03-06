#!/usr/bin/env python
# -*- coding: utf-8 -*-


class I18N(object):
    __musical_text = {
        "english": {
            "key": {
                '-1': 'F major. B-flat',
                '-2': 'B-flat major. Key signature: B-flat; E-flat',
                '-3': 'E-flat major. Key signature: A-flat; B-flat; E-flat',
                '-4': 'A-flat major. Key signature: A-flat; B-flat; D-flat; E-flat',
                '-5': 'D-flat major. Key signature: A-flat; B-flat; D-flat; E-flat; G-flat',
                '-6': 'G-flat major. Key signature: A-flat; B-flat; C-flat; D-flat; E-flat; G-flat',
                '-7': 'C-flat major. Key signature: A-flat; B-flat; C-flat; D-flat; E-flat; F-flat; G-flat',
                '0': 'C major. Key signature: None',
                '1': 'G major. Key signature: F-sharp',
                '2': 'D major. Key signature: C-sharp; F-sharp',
                '3': 'A major. Key signature: C-sharp; F-sharp; G-sharp',
                '4': 'E major. Key signature: C-sharp; D-sharp; F-sharp; G-sharp',
                '5': 'B major. Key signature: A-sharp; C-sharp; D-sharp; F-sharp; G-sharp',
                '6': 'F-sharp major. Key signature: A-sharp; C-sharp; D-sharp; E-sharp; F-sharp; G-sharp',
                '7': 'C-sharp major. Key signature: A-sharp; B-sharp; C-sharp; D-sharp; E-sharp; F-sharp; G-sharp'
            },
            "dynamics": {
                'p': 'soft',
                'pp': 'very soft',
                'ppp': 'very very soft',
                'f': 'loud',
                'ff': 'very loud',
                'fff': 'very very loud',
                'fz': 'accented note',
                'mf': 'half strong',
                'mp': 'half soft'
            },
            "other": {
                "octave_shift": "the following set of notes need to be shifted up by one octave",
                " 拍": "",
            },

        },
        "chinese": {
            "key": dict(zip(['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'],
                            ['5个降号', '4个降号', '3个降号', '两个降号'
                                , '1个降号', '没有升降号', '1个升号',
                             '两个升号', '3个升号', '4个升号', '5个升号'])),

            "dynamics": {
                'p': '弱',
                'pp': '很弱',
                'ppp': '最弱',
                'f': '强',
                'ff': '很强',
                'fff': '最强',
                'fz': '突强',
                'mf': '中强',
                'mp': '中弱'
            },

            "meta": {
                'tempo': "拍子",
                'composer': '作曲',
                'title': '标题',
                'key': "调号",
                'beat': '节拍'
            },

            "wedge":{
                'crescendo': ' 渐强 ',
                'diminuendo' : ' 渐弱 '
            },

            "accidental": {
                "sharp": "升",
                "natural": "还原",
                "flat": "降"
            },


            "title":{
                "For Elise": "致爱丽丝",
                "qianlizhiwai" : "千里之外"
            },

            "composer":{
                "Beethoven": "贝多芬",
                "zhoujielun": "周杰伦"
            },

            "step": dict(zip(['C','D','E','F','G','A','B'], \
                             ['多', '来', '咪', '发', '缩', '拉', '西'])),
            "octave": {'1': '大字二组 ','2': '大字一组 ','3': '大字组 ',\
                       '4': '小字组 ','5': '小字一组 ','6': '小字二组 ',
                       '7': '小字三组 ','8': '小字四组 ','9': '小字五组 '},
            "duration": dict(zip(['64th', '32th', '16th', 'eighth', \
                                  'quarter', 'half', 'whole'],
                             ['六十四分音符','三十二分音符','十六分音符',\
                              '八分音符','四分音符','二分音符','全音符'])),
            "other": {
                "octave_shift": "以下的一组音符需要升高八度",
                "second musical line": "第二行乐句",
                "not defined": "未定义",
                "first musical line": "第一行 ",
                " rest": " 休止符",
                "dotted ": "附点 ",
                "grace note ": "装饰音 ",
                "start slur ": " 开始连音 ",
                "arpeggiated ": "琶音 ",
                "start tuplet ": " 开始三连音",
                " stop slur " : " 结束连音 ",
                " stop tuplet ": " 结束三连音",
                "tied note ": "连结音符 ",
                " note": "",
                " perminute": " 每分钟",
                "staccato ": "断音 ",
            }
        }
    }
    __language = None

    def set_language(self, lang):
        lang = lang.lower()
        print(lang)
        if lang != "english" and lang != "chinese":
            print('only support English and Chinese')
        self.__language = lang

    def get_language(self):
        return self.__language

    def get_text(self, keyword, t="other"):
        # if the keyword is not found, return itself
        if self.__language is None:
            print("language not set")
            return False
        if t not in self.__musical_text[self.__language]:
            return keyword
        return self.__musical_text[self.__language][t].get(keyword, keyword)

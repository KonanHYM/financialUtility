# -*- coding: utf-8 -*-
# 微信公众号后台自动处理工具
# 将研报转换成HTML格式，转换为JSON格式，解析JSON生成适用于微信公众平台的HTML代码
import docx

from style import STYLE

#待处理文件路径
FILE_PATH = "../file/招商策略-细看估值，图说中观-行业比较系列V2.0.docx"

#待处理JSON文件格式
DATA = {
    "title" : "",
    "author" : "",
    "abstract" : "",
    "content" : [
        [

        ],#一个列表表示一段，一个tumple 表示一种类型的句子，tumple中第一个元素表示数据类型
           #tumple 中的数据类型, One-class, Two-class, List-num, Bold, UnderLine, Bold-Underline, Normal,
    ]
}

#微信公众号模版生成器
class WechatAutoGenerator:
    def __init__(self, local_path, style):
        self.local_path = local_path
        self.style = style
        self.article_data = self.doc_parser()

    #处理研报信息，生成JSON
    def doc_parser(self):
        document = docx.Document(docx=self.local_path)
        #print document.core_properties.author
        #print document.core_properties.title
        for item in document.paragraphs:
            if item.text:
                for run_ob in item.runs:
                    print run_ob.text
        return None
                # print item.text.bold
                # print item.style.font.bold
                # print '-------'

    #run_object 处理方法
    def run_ob_parser(self, run_ob):
        pass

    #套用模版，解析JSON 自动生成微信页面
    def wechat_auto_generator(self):
        html_body = ""
        my_style = STYLE['normal_style']
        final_html = my_style["Body"][0] + html_body + my_style["Body"][1]
        f = open("final.html",'w')
        f.write(final_html)
        f.close()

if __name__ == '__main__':
    wechat_generator = WechatAutoGenerator(local_path=FILE_PATH, style=STYLE)

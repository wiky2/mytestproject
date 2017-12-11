#python去除html标签 获取纯文本2010-03-23 17:25#coding=utf-8
import htmllib
import formatter
class MyParser(htmllib.HTMLParser):

    def __init__(self, verbose = 0):
        fmt = formatter.AbstractFormatter(formatter.DumbWriter())
        htmllib.HTMLParser.__init__(self, fmt, verbose)
    def start_style(self, attrs):
        self.save_bgn()
    def end_style(self):
        self.save_end()
    def start_script(self, attrs):
        if "src" in attrs[0]:
            pass
        else:
            self.save_bgn()
    def end_script(self):
        if self.savedata:
            self.save_end()

    def strip_tags(html):
        html = html.replace('&nbsp;', ' ')  #替换空格
        par = MyParser()
        result = []
        par.handle_data=result.append
        par.feed(html)
        par.close()
        return "".join(result)


if __name__== "__main__":
html = """<aaa name="放大法肯定是">的发生地方</aaa><input type="text" name="地方叫老师的" /><b>范德萨<br><u>飞洒的收到<br></u></b><div style="text-align: left;"><b><u>方式地方收到收到</u></b><br>方式地方卡斯迪朗飞洒的李开复<br></div>
"""
strip_tags(html) 


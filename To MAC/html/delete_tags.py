#coding=utf-8
from html.parser import HTMLParser
def strip_tags(html):

    html=html.strip()#  去除空格
    html=html.strip("\n")#去除回车
    result=[]
    parse=HTMLParser()
    parse.handle_data=result.append#将方法赋值给handle_data
    parse.feed(html)
    parse.close()
    print(result)#处理完毕后再返回给result
    return "".join(result)

if __name__== "__main__":
    html = """<aaa name="放大法肯定是">的发生地方</aaa><input type="text" name="地方叫老师的" /><b>范德萨<br><u>飞洒的收到<br></u></b><div style="text-align: left;"><b><u>方式地方收到收到</u></b><br>方式地方卡斯迪朗飞洒的李开复<br></div>
"""
    print(strip_tags(html))


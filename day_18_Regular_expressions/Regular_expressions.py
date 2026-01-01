import re
from collections import Counter

msg = "警告：您的账号 4522-3322-1111-0000 于 2023-01-01 消费了 $999.00 元。"
credit_card = re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}', msg)
print(credit_card)
consumption_date = re.findall(r'\d{4}-\d{2}-\d{2}', msg)
print(consumption_date)


# mission_2
# 编写一个函数 is_valid_variable(name)。 判断一个字符串是不是合法的 Python 变量名。
def is_valid_variable(name: str):
    pattern = r'^[a-zA-Z_]\w*$'
    '''限制开头 (^)：告诉正则“必须从字符串第一个字符开始查”。
    第一位规则([a - zA - Z_])：第一位只能是字母或下划线。
    后续规则(\w *)
    \w代表“字母、数字、下划线”的集合（Word character）。
    *代表“后面这些东西可以出现0次或无限次”。
    限制结尾($)：告诉正则“必须匹配到字符串结束”。（如果不加这个，var! 这种非法变量名也会被匹配成功，因为它包含了合法的
    var）。'''
    return bool(re.search(pattern, name))


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False (连字符非法)
print(is_valid_variable("1first_name"))  # False (数字开头非法)
print(is_valid_variable("variable1"))  # True

# mission_3
# 请用 re.sub() 去掉所有的 % 符号，还原出正常的句子。
text = "%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing."
normal_text = re.sub(r'%', r'', text)
print(normal_text)

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
pattern = r'<[^>]+>'

matches = re.findall(pattern, text)
print(matches)
no_html_text = re.sub(pattern, '', text)
print(no_html_text)
# 清理以下文本。在清理过程后，计算最常见的三个单词是什么。
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
pattern = r'[^\w\s]'
paragraph = re.sub(pattern, '', paragraph).lower()  # 去除所有的非字符与空格+小写
statistics = Counter(paragraph.split())
print(statistics.most_common(3))
# 下面的文本包含了几个电子邮件地址。编写一个可以查找或提取电子邮件地址的模式。
email_address= '''
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
'''
pattern = r'[\w.-]+@[\w]+\.[\w]{2,}'
emails = re.findall(pattern, email_address)
print("提取到的有效邮箱:", emails)
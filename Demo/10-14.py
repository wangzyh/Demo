Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> browser.get("https://www.taobao.com")
>>> input_frist = browser.find_elenium_by_id('q')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    input_frist = browser.find_elenium_by_id('q')
AttributeError: 'WebDriver' object has no attribute 'find_elenium_by_id'
>>> input_frist = browser.find_element_by_id('q')
>>> print(input_frist)
<selenium.webdriver.remote.webelement.WebElement (session="e62033f49c12853b5344827c5421cc71", element="0.06938211038778741-1")>
>>> browser.close()
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> browser.get("https://www.taobao.com")
>>> from selenium.webdriver.common.by import By
>>> input_first = browser.find_element(By.ID,'q')
>>> print(input_first)
<selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-1")>
>>> lis = browser.find_eleniums_by_css_selector(".service-bd li")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    lis = browser.find_eleniums_by_css_selector(".service-bd li")
AttributeError: 'WebDriver' object has no attribute 'find_eleniums_by_css_selector'
>>> lis = browser.find_elements_by_css_selector(".service-bd li")
>>> print(lis)
[<selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-2")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-3")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-4")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-5")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-6")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-7")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-8")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-9")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-10")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-11")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-12")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-13")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-14")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-15")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-16")>, <selenium.webdriver.remote.webelement.WebElement (session="1935a9f42c3f5aee5f17d4a88a840c23", element="0.8495564765198382-17")>]
>>> print(list[:3])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(list[:3])
TypeError: 'type' object is not subscriptable
>>> input = browser.find_element_by_id('q')
>>> input.send_keys('mx6')
>>> button = browser.find_element_by_class_name("btn-search")
>>> button.click()
>>> input.clear()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    input.clear()
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webelement.py", line 95, in clear
    self._execute(Command.CLEAR_ELEMENT)
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webelement.py", line 501, in _execute
    return self._parent.execute(command, params)
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 308, in execute
    self.error_handler.check_response(response)
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
  (Session info: chrome=61.0.3163.100)
  (Driver info: chromedriver=2.32.498550 (9dec58e66c31bcc53a9ce3c7226f0c1c5810906a),platform=Windows NT 10.0.15063 x86_64)

>>> browser.get("https://www.zhihu.com/explore")
>>> browser.execute_script("windows.scrollTo(0,document.body.scrollHeight)")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    browser.execute_script("windows.scrollTo(0,document.body.scrollHeight)")
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 543, in execute_script
    'args': converted_args})['value']
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 308, in execute
    self.error_handler.check_response(response)
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: windows is not defined
  (Session info: chrome=61.0.3163.100)
  (Driver info: chromedriver=2.32.498550 (9dec58e66c31bcc53a9ce3c7226f0c1c5810906a),platform=Windows NT 10.0.15063 x86_64)

>>> browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
>>> browser.execute_script("alert('To Bottom')")
>>> url = 'https://www,zhihu.com/explore'
>>> browser.get(url)
>>> input = browser.find_element_by_class_name('zu-top-add-question')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    input = browser.find_element_by_class_name('zu-top-add-question')
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 485, in find_element_by_class_name
    return self.find_element(by=By.CLASS_NAME, value=name)
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 843, in find_element
    'value': value})['value']
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 308, in execute
    self.error_handler.check_response(response)
  File "D:\python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"class name","selector":"zu-top-add-question"}
  (Session info: chrome=61.0.3163.100)
  (Driver info: chromedriver=2.32.498550 (9dec58e66c31bcc53a9ce3c7226f0c1c5810906a),platform=Windows NT 10.0.15063 x86_64)

>>> url = 'https://www.zhihu.com/explore'
>>> browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
>>> input = browser.find_element_by_class_name('zu-top-add-question')
>>> print(input.text)
提问
>>> input = browser.find_element_by_class_name("question_link")
>>> print(input.text)
高铁的一等座和二等座有哪些区别？
>>> print(input.id)
0.6625121901404363-2
>>> print(input.location)
{'x': 28, 'y': 315}
>>> print(input.tag_name)
a
>>> print(input.size)
{'height': 16, 'width': 224}
>>> 

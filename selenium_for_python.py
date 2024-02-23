
# 1、导包
import random
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 账号
user_list = [
    'aaaaaa',
    'bbbbbb',
    'ccccc',
    'ddddd',
    'eeeee'

]

for user in user_list:
    # 2、实例化浏览器对象：类名（）
    browser = webdriver.Chrome()
    # 设置窗口大小
    browser.set_window_size(1500, 1080)

# 浏览器缩放比例
    browser.get('chrome://settings/')
    browser.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')

    # 将窗口移动到主显示器的左上角
    browser.set_window_position(0, 0)
    url = 'https://de.fi/dashboard/portfolio-overview'
    # 3、打开网页包含协议头
    browser.get(url)

    browser.implicitly_wait(5)
    # sleep random
    sleep(random.randint(1, 3))

    # got it button
    alert_one = browser.find_element('xpath', '//button[text()="Got It"]')
    alert_one.click()

    browser.implicitly_wait(2)
    sleep(random.randint(3, 6))

    # later 按钮
    alert_two = browser.find_element('xpath', '//button[text()="Later"]')
    alert_two.click()

    browser.implicitly_wait(1)
    # 4、实施操作  点击登录button
    element = browser.find_element('xpath', '//*[@id="main-scroller"]/div[1]/div/div[2]/div[2]/button/p')
    element.click()

    browser.implicitly_wait(random.randint(3, 6))
    sleep(random.randint(3, 5))

    # user name
    u_name = browser.find_element('xpath', '/html/body/div[2]/div[3]/div/div[1]/div/form/div[1]/label/div[2]/input')
    u_name.clear()
    u_name.send_keys(user)

    sleep(random.randint(1, 3))

    # user pwd
    u_pwd = browser.find_element('xpath', '/html/body/div[2]/div[3]/div/div[1]/div/form/div[2]/div/label/div[2]/input')
    u_pwd.clear()
    u_pwd.send_keys('12345678abc') #这是密码

    sleep(random.randint(1, 3))

    # login button
    submit_btn = browser.find_element('xpath', '//button[text()="Continue"]')
    submit_btn.click()

    browser.implicitly_wait(random.randint(4, 6))
    sleep(random.randint(6, 8))

    print('当前用户:',user + '~~~~~~~~~')
    # 通过try except 判断元素是否存在 如果不存在也不会crash~
    try:
        print('用户指南已显示 ~~~~~~~~~')
        alert_three1 = browser.find_element('xpath', '//*[@id="react-joyride-step-0"]/div/div/div/div/div/div/button')
        alert_three1.click()
        sleep(random.randint(2, 4))
        browser.implicitly_wait(random.randint(3, 6))

        alert_three2 = browser.find_element('xpath',
                                            '//*[@id="react-joyride-step-1"]/div/div/div/div/div/div/button[2]')
        alert_three2.click()
        sleep(random.randint(2, 3))

        alert_three3 = browser.find_element('xpath',
                                            '//*[@id="react-joyride-step-2"]/div/div/div/div/div/div/button[2]')
        alert_three3.click()
        sleep(random.randint(2, 3))

        alert_three4 = browser.find_element('xpath',
                                            '//*[@id="react-joyride-step-3"]/div/div/div/div/div/div/button[2]')
        alert_three4.click()

    except NoSuchElementException:
        print("用户指南弹框不存在")
    finally:
        sleep(random.randint(2, 4))

# 判断progress按钮是否显示
    is_show_progress_btn = browser.find_element('xpath',
                                        '/html/body/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div[1]/div/div[3]/div/div[2]/div/button[3]').is_displayed()
    if is_show_progress_btn:
        # 点击progress 按钮
        progress_btn = browser.find_element('xpath',
                                            '/html/body/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div[1]/div/div[3]/div/div[2]/div/button[3]')
        progress_btn.click()
        print('点击progress~~~~~~~~~')
        browser.implicitly_wait(random.randint(3, 6))
        sleep(random.randint(3, 5))
    else:
        browser.refresh()
        browser.implicitly_wait(random.randint(4,6))
        sleep(random.randint(3, 6))
        # 点击progress 按钮
        progress_btn = browser.find_element('xpath',
                                            '/html/body/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div[1]/div/div[3]/div/div[2]/div/button[3]')
        progress_btn.click()
        print('点击progress~~~~~~~~~')

    sleep(random.randint(3, 6))
    browser.implicitly_wait(random.randint(4, 6))
    # is_enabled() 检测元素当前状态是否启用
    is_enable_checkin_btn = browser.find_element('xpath', '//*[@id="pushable"]/div/main/div[2]/div[2]/div/div[2]/div[1]/button').is_enabled()
    if is_enable_checkin_btn:
        checkin_btn = browser.find_element('xpath', '//*[@id="pushable"]/div/main/div[2]/div[2]/div/div[2]/div[1]/button')
        # 点击签到按钮
        checkin_btn.click()
        print('签到Ok ~~~~~~~~~')
        sleep(random.randint(5, 15))
        browser.quit()
    else:
        print('已经签到过了 ~~~~~~~~~')
        sleep(random.randint(5, 15))
        browser.quit()

    sleep(random.randint(3, 6))




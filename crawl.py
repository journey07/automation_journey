import time, random
import telegram
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler

# telegram 연결
my_token = '1452258160:AAE-vBhMASThkE90ZD0X7SygYyxIBemnm9c'
bot = telegram.Bot(token=my_token)

# 커리어 연세 접속
driver = webdriver.Chrome("C:\\Users\\user\\PycharmProjects\\chromedriver_win32\\chromedriver")
url = 'https://career.yonsei.ac.kr/intro.do'
driver.get(url)

# 로그인 버튼 클릭
time.sleep(random.uniform(0, 1))
driver.find_element_by_class_name('log_btn1').click()

# 로그인
time.sleep(random.uniform(0, 1))
driver.find_element_by_id('loginId').send_keys("2013147045")
driver.find_element_by_id('loginPasswd').send_keys("1167623")
driver.find_element_by_class_name('submit').click()

# 채용공고
time.sleep(random.uniform(0, 1))
driver.find_element_by_css_selector('#mainWidgetUseLstWrap > li.m_box.box08.first > div > a').click()


# 확인용 리스트
check_if_new = ['hi']


# 첫 공고 update 알려주는 함수
def send_new_job():
    driver.refresh()
    new_job = driver.find_element_by_css_selector(
        '#ptfolCareerProgramSearch > div.table_wrap.pc_view > table > tbody > tr.first > td.title.td_btn > a').text
    if new_job not in check_if_new:
        check_if_new[0] = new_job
        bot.sendMessage(chat_id='1560973451', text=check_if_new[0])
    else:
        print(check_if_new)


# 일정 주기로 반복
schedule = BlockingScheduler()
schedule.add_job(send_new_job, 'interval', seconds=10)
schedule.start()

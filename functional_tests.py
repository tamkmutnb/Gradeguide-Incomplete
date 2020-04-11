# import selenium webdriver, time and unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    # check opening FireFox
    def setUp(self):
        self.browser = webdriver.Firefox()

    # check quit FireFox
    def tearDown(self):
        self.browser.quit()

    # test index Page
    def test_index(self):
        # เอิร์ธได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        # จึงเข้าเว็บไปที่หน้า Homepage

        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        # find element 'h1' as text = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link

        # find element 'link'  = homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text

        # check if 'Home page' is in homepage_link var
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        # check if 'Sign up' is in signup_link var
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        # check if 'Log in' is in login_link var
        self.assertIn('Log in', login_link)

        # find element 'h2'  = welcome_text var
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        # check if 'Welcome to GradeGuide !' is in welcome_text var
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # find element 'p'  = totaluser_text var
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        # check if 'Total users registered:' is in totaluser_text var
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        # find element 'link'  = login_click var
        login_click = self.browser.find_element_by_link_text('Log in')
        # click the login_click
        login_click.click()

        #check if browser title is empty as it should
        self.assertIn('', self.browser.title)
        # find element 'h1'  = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        # find element 'link'  = homepage_link var
        # check if 'Home page' is in homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        # check if 'Sign up' is in signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        # check if 'Log in' is in login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        # find element 'h2'  = login_h2 var
        # check if 'Log in' is in login_h2 var
        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)

        # check Label Username:
        # find element 'label@for'  = username_label var
        # check if 'Username:' is in username_label var
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # check Label Input Box
        # find element 'id'  = username_box var
        # check if 'text' is equal to username_box.attribute var
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # check Label Password:
        # find element 'label@for'  = password_label var
        # check if 'Password:' is in password_label var
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)

        # check Label Input Pasword Box
        # find element 'id'  = password_box var
        # check if 'password' is equal to password_box.attribute var
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        # find element 'id'  = login_button var
        # check if 'submit' is equal to login_button.attribute var
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

    def test_login_fail(self):
        # BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        # find element 'h1' as text = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link

        # find element 'link'  = homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        # check if 'Home page' is in homepage_link var
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        # check if 'Sign up' is in signup_link var
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        # check if 'Log in' is in login_link var
        self.assertIn('Log in', login_link)

        # find element 'h2'  = welcome_text var
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        # check if 'Welcome to GradeGuide !' is in welcome_text var
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # find element 'p'  = totaluser_text var
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        # check if 'Total users registered:' is in totaluser_text var
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        # find element 'link'  = login_click var
        login_click = self.browser.find_element_by_link_text('Log in')
        # click the login_click
        login_click.click()

        # check if browser title is empty as it should
        self.assertIn('', self.browser.title)
        # find element 'h1'  = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        # find element 'link'  = homepage_link var
        # check if 'Home page' is in homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        # check if 'Sign up' is in signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        # check if 'Log in' is in login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        # find element 'h2'  = login_h2 var
        # check if 'Log in' is in login_h2 var
        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)

        # check Label Username:
        # find element 'label@for'  = username_label var
        # check if 'Username:' is in username_label var
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # check Label Input Box
        # find element 'id'  = username_box var
        # check if 'text' is equal to username_box.attribute var
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # check Label Password:
        # find element 'label@for'  = password_label var
        # check if 'Password:' is in password_label var
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)

        # check Label Input Pasword Box
        # find element 'id'  = password_box var
        # check if 'password' is equal to password_box.attribute var
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        # find element 'id'  = login_button var
        # check if 'submit' is equal to login_button.attribute var
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        # END BASIC TEST

        # find element 'ul'  = error_message var
        # check if 'following text' is in error_message var
        error_message = self.browser.find_element_by_tag_name('ul').text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)

        # wait for 20s
        time.sleep(20)
        # check if broswer title is empty
        self.assertIn('', self.browser.title)

        # find element 'h1' as text = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # find element 'link'  = homepage_link var
        # check if 'Home page' is in homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        # check if 'Sign up' is in signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        # check if 'Log in' is in login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        # find element 'ul'  = error_message var
        # check if 'following text' is in error_message var
        error_message = self.browser.find_elements_by_xpath("//ul[@class='errorlist nonfield']").text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)

    def test_login_pass(self):
        # basic test
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        # find element 'h1' as text = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link

        # find element 'link'  = homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text

        # check if 'Home page' is in homepage_link var
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        # check if 'Sign up' is in signup_link var
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        # check if 'Log in' is in login_link var
        self.assertIn('Log in', login_link)

        # find element 'h2'  = welcome_text var
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        # check if 'Welcome to GradeGuide !' is in welcome_text var
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # find element 'p'  = totaluser_text var
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        # check if 'Total users registered:' is in totaluser_text var
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        # find element 'link'  = login_click var
        login_click = self.browser.find_element_by_link_text('Log in')
        # click the login_click
        login_click.click()

        # check if browser title is empty as it should
        self.assertIn('', self.browser.title)
        # find element 'h1'  = header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        # find element 'link'  = homepage_link var
        # check if 'Home page' is in homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = signup_link var
        # check if 'Sign up' is in signup_link var
        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        # find element 'link'  = login_link var
        # check if 'Log in' is in login_link var
        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        # find element 'h2'  = login_h2 var
        # check if 'Log in' is in login_h2 var
        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)

        # check Label Username:
        # find element 'label@for'  = username_label var
        # check if 'Username:' is in username_label var
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)

        # check Label Input Box
        # find element 'id'  = username_box var
        # check if 'text' is equal to username_box.attribute var
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )

        # check Label Password:
        # find element 'label@for'  = password_label var
        # check if 'Password:' is in password_label var
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)

        # check Label Input Pasword Box
        # find element 'id'  = password_box var
        # check if 'password' is equal to password_box.attribute var
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        # find element 'id'  = login_button var
        # check if 'submit' is equal to login_button.attribute var
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        # end basic test

        # Check Type Username Pass RIGHT !
        # User input username
        # User in put password
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        # username_box.send_keys('tamtong007')
        # password_box.send_keys('o87525o135')
        # click login button
        login_button.click()

        # Check Redirect !!!!!

        self.assertIn('', self.browser.title)
        # find element 'h1' as text = header_text var
        # check if 'GradeGuide' is in header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        # find element 'link'  = homepage_link var
        # check if 'Home page' is in homepage_link var
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        # find element 'link'  = logout_link var
        # check if 'Log out' is in logout_link var
        logout_link = self.browser.find_element_by_link_text('Log out').text
        self.assertIn('Log out', logout_link)

        # find element 'h4'  = id_text var
        # check if 'ID : jesselingard' is in id_text var
        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : jesselingard', id_text)

        '''Check Click Link
        homepage_click = self.browser.find_element_by_link_text('Home page')
        homepage_click.click()
        time.sleep(2)'''

        '''End of Checking Login'''

    def test_subjects_button_flow(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test Flow H1 text
        # เธอเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Flow', header_text)

        # เธอเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
        defination = self.browser.find_element_by_tag_name('p1').text
        self.assertEqual("If you can't remember the subject's name , The Subjects button will help you. :)", defination)

        # test subjects button
        # เธอจำชื่อวิชาไม่ได้
        # เธอจึงคลิกไปที่ปุ่ม subjects เพื่อที่เธอจะได้ดูชื่อวิชา
        subject_button = self.browser.find_element_by_id("subject_button")
        subject_button.click()
        time.sleep(5)

        self.fail('Finish the test!')

    def test_search_flow(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('', self.browser.title)

        # test search box
        # เธอเห็นช่องสำหรับใส่ชื่อวิชาเพื่อค้นหาวิชาที่เป็นตัวต่อกัน
        # เธอจึงพิมพ์วิชา Programming Fundamental ลงไป
        subject_placeholder = self.browser.find_element_by_id("search_placeholder")
        self.assertEqual(
            subject_placeholder.get_attribute('type'),
            'text'
        )

        subject_placeholder.send_keys('Programming Fundamental')
        time.sleep(5)

        # test submit button
        # เธอจึงกดปุ่ม search เพื่อทำการหาตัวต่อของวิชา Programming Fundamental
        submit_button = self.browser.find_element_by_id("submit_button")
        self.assertEqual(
            submit_button.get_attribute('type'),
            'submit'
        )
        submit_button.click()
        time.sleep(10)

        # test input Search text
        # เธอเห็นหัวข้อ subject
        # หลังจากที่เธอกด search แล้ว เธอพบว่าวิชาที่เธฮ search ไปปรากฏอยู่หลังหัวข้อ subject
        subject_head = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('subject : Programming Fundamental', subject_head)

        # test search result
        # เธอเห็นผลของการ search ของเธอ หลังจากที่กดปุ่ม search ไป
        result_search = self.browser.find_element_by_tag_name('p2').text
        self.assertEqual("Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems", result_search)

        # test Note
        # เธอเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
        note = self.browser.find_element_by_tag_name('p3').text
        self.assertEqual(
            "Note : Elective Subjects don't connect to each other but I want to show how many elective subjects are in this flow.",
            note)

        self.fail('Finish the test!')

    def test_flow_pic(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test fullflow button
        # เธออยากดูภาพรวมของวิชาทั้งหมดที่เธอต้องเรียน
        # เธอจึงคลิกไปที่ปุ่ม Full Flow เพื่อไปยังรูป flow
        flow_button = self.browser.find_element_by_id("fullflow_button")
        flow_button.click()

        # test can find the flow picture
        # เธอเห็นภาพวิชาตัวต่อทั้งหมด
        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(10)

        self.fail('Finish the test!')

    def test_home(self):
        # เมื่อเขากดเข้าไปที่หน้า signup
        self.browser.get('http://localhost:8000/signup')

        username_box = self.browser.find_element_by_id("id_username")

        password_box = self.browser.find_element_by_id("id_password1")

        password_box2 = self.browser.find_element_by_id("id_password2")

        # เขาทำการสมัคร username jesselingard
        # password lingard123456789
        # password2 lingard123456789
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        password_box2.send_keys('lingard123456789')
        # เขาทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_tag_name("button")
        signup_button.click()
        time.sleep(2)
        # เขาเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', header_text)

        username_login_box = self.browser.find_element_by_id("id_username")

        password_login_box = self.browser.find_element_by_id("id_password")
        # เขาใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')
        # เขากดปุ่ม login
        login_button = self.browser.find_element_by_tag_name("button")
        login_button.click()
        time.sleep(2)
        # เขาเข้าไปที่หน้า homepage
        self.browser.get('http://127.0.0.1:8000/home')
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)
        # เขาใส่ unit
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')
        # เขาใส่ Grade
        unit_text = self.browser.find_element_by_id('subject1Gradeid')
        unit_text.send_keys('Grade: 2.5&nbsp; (C+)')
        time.sleep(3)
        # เขาเห็นเกรดแสดงขึ้นมา
        submit_button = self.browser.find_element_by_id("submit")
        submit_button.click()
        time.sleep(3)
        submit_text = self.browser.find_element_by_id('gradeshow').text
        self.assertIn('2.5', submit_text)
        time.sleep(6)
        # เขาเห็นสาถานะนักศึกษาของเขา
        self.assertIn('Normal State', submit_text)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

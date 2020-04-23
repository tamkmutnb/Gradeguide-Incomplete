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
        # ! find element 'h1' as text = header_text var
        # ! header_text = self.browser.find_element_by_tag_name('h1').text
        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADGUIDE', header_link)

        # Check HomePage, Sign Up and Log in Link

        # ! find element 'link'  = homepage_link var
        # ! homepage_link = self.browser.find_element_by_link_text('Home page').text

        # check if 'Home page' is in homepage_link var
        # ! self.assertIn

        # find element 'link'  = about_link var
        about_link = self.browser.find_element_by_link_text('ABOUT').text
        # check if 'ABOUT' is in signup_link var
        self.assertIn('ABOUT', about_link)

        # find element 'link'  = about_link var
        help_link = self.browser.find_element_by_link_text('HELP').text
        # check if 'HELP' is in signup_link var
        self.assertIn('HELP', help_link)

        # find element 'link'  = about_link var
        signup_link = self.browser.find_element_by_partial_link_text('SIGNU').text
        # check if 'SIGNUP' is in signup_link var
        self.assertIn('SIGNU', signup_link)

        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN').text
        # check if 'LOGIN' is in signup_link var
        self.assertIn('LOGIN', login_link)

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
        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN')
        # check if 'LOGIN' is in signup_link var
        login_link.click()
        time.sleep(2)

        #check if browser title is empty as it should
        self.assertIn('', self.browser.title)

        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADGUIDE', header_link)

        # Check HomePage, Sign Up and Log in Link

        # find element 'link'  = about_link var
        help_link = self.browser.find_element_by_link_text('HELP').text
        # check if 'HELP' is in signup_link var
        self.assertIn('HELP', help_link)

        # find element 'link'  = about_link var
        signup_link = self.browser.find_element_by_partial_link_text('SIGNU').text
        # check if 'SIGNUP' is in signup_link var
        self.assertIn('SIGNU', signup_link)

        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN').text
        # check if 'LOGIN' is in signup_link var
        self.assertIn('LOGIN', login_link)

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

    def test_login_fail(self):
        # BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)

        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADGUIDE', header_link)

        # Check HomePage, Sign Up and Log in Link

        # find element 'link'  = about_link var
        about_link = self.browser.find_element_by_link_text('ABOUT').text
        # check if 'ABOUT' is in signup_link var
        self.assertIn('ABOUT', about_link)

        # find element 'link'  = about_link var
        help_link = self.browser.find_element_by_link_text('HELP').text
        # check if 'HELP' is in signup_link var
        self.assertIn('HELP', help_link)

        # find element 'link'  = about_link var
        signup_link = self.browser.find_element_by_partial_link_text('SIGNU').text
        # check if 'SIGNUP' is in signup_link var
        self.assertIn('SIGNU', signup_link)

        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN').text
        # check if 'LOGIN' is in signup_link var
        self.assertIn('LOGIN', login_link)

        # find element 'h2'  = welcome_text var
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        # check if 'Welcome to GradeGuide !' is in welcome_text var
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # find element 'p'  = totaluser_text var
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        # check if 'Total users registered:' is in totaluser_text var
        self.assertIn('Total users registered:', totaluser_text)

        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN')
        # check if 'LOGIN' is in signup_link var
        login_link.click()
        time.sleep(2)

        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        time.sleep(2)

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
            'button'
        )
        # END BASIC TEST

        username_box.send_keys('wrongusername')
        time.sleep(2)
        password_box.send_keys('wrongpsw')
        time.sleep(2)
        login_buttonnew = self.browser.find_element_by_name('login_button_name')
        #login_class = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_buttonnew.click()
        #login_class.click()
        time.sleep(2)
        # find element 'ul'  = error_message var
        # check if 'following text' is in error_message var
        error_message = self.browser.find_element_by_xpath("//form[@id='login_form']/ul[1]").text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)
        time.sleep(2)

    def test_login_pass(self):
        # BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)

        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADGUIDE', header_link)

        # Check HomePage, Sign Up and Log in Link

        # find element 'link'  = about_link var
        about_link = self.browser.find_element_by_link_text('ABOUT').text
        # check if 'ABOUT' is in signup_link var
        self.assertIn('ABOUT', about_link)

        # find element 'link'  = about_link var
        help_link = self.browser.find_element_by_link_text('HELP').text
        # check if 'HELP' is in signup_link var
        self.assertIn('HELP', help_link)

        # find element 'link'  = about_link var
        signup_link = self.browser.find_element_by_partial_link_text('SIGNU').text
        # check if 'SIGNUP' is in signup_link var
        self.assertIn('SIGNU', signup_link)

        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN').text
        # check if 'LOGIN' is in signup_link var
        self.assertIn('LOGIN', login_link)

        # find element 'h2'  = welcome_text var
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        # check if 'Welcome to GradeGuide !' is in welcome_text var
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        # find element 'p'  = totaluser_text var
        totaluser_text = self.browser.find_element_by_tag_name('p').text
        # check if 'Total users registered:' is in totaluser_text var
        self.assertIn('Total users registered:', totaluser_text)

        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN')
        # check if 'LOGIN' is in signup_link var
        login_link.click()
        time.sleep(2)

        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        time.sleep(2)

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
            'button'
        )
        # END BASIC TEST

        # Check Type Username Pass RIGHT !
        # User input username
        # User in put password
        username_box.send_keys('tamtong007')
        time.sleep(2)
        password_box.send_keys('O87525o135@')
        time.sleep(2)
        login_buttonnew = self.browser.find_element_by_name('login_button_name')
        # login_class = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_buttonnew.click()
        # login_class.click()
        time.sleep(2)

        # Check Redirect !!!!!
        broswer_title = self.browser.title
        self.assertIn('Home', broswer_title)

    def test_subjects_button_flow(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test Flow H1 text
        # เธอเห็นคำว่า Flow ซึ่งเป็นหัวข้อใหญ่
        # find element 'h1'  = header_text var
        # check if 'Flow' is in header_text var
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Flow', header_text)

        # เธอเห็นประโยคที่อยู่ก่อนหน้าปุ่ม subjects
        # find element 'p1'  = defination var
        # check if 'following text' is equal to defination var
        defination = self.browser.find_element_by_tag_name('p1').text
        self.assertEqual("If you can't remember the subject's name , The Subjects button will help you. :)", defination)

        # test subjects button
        # เธอจำชื่อวิชาไม่ได้
        # เธอจึงคลิกไปที่ปุ่ม subjects เพื่อที่เธอจะได้ดูชื่อวิชา
        # find element 'p1'  = subject_button var
        subject_button = self.browser.find_element_by_id("subject_button")
        # click subject_button
        subject_button.click()
        # wait for 5s
        time.sleep(5)
        # test finish text
        #self.fail('Finish the test!')

    def test_search_flow(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('', self.browser.title)

        # test search box
        # เธอเห็นช่องสำหรับใส่ชื่อวิชาเพื่อค้นหาวิชาที่เป็นตัวต่อกัน
        # เธอจึงพิมพ์วิชา Programming Fundamental ลงไป
        # find element 'id'  = subject_placeholder var
        # check if 'text' is equal to subject_placeholder.attribute var
        subject_placeholder = self.browser.find_element_by_id("search_placeholder")
        self.assertEqual(
            subject_placeholder.get_attribute('type'),
            'text'
        )

        # subject_placeholder input 'Programming Fundamental'
        subject_placeholder.send_keys('Programming Fundamental')
        # wait for 5s
        time.sleep(5)

        # test submit button
        # เธอจึงกดปุ่ม search เพื่อทำการหาตัวต่อของวิชา Programming Fundamental
        # find element 'id'  = submit_button var
        # check if 'submit' is equal to submit_button.attribute var
        submit_button = self.browser.find_element_by_id("submit_button")
        self.assertEqual(
            submit_button.get_attribute('type'),
            'submit'
        )
        # click submit_button
        # wait for 10s
        submit_button.click()
        time.sleep(10)

        # test input Search text
        # เธอเห็นหัวข้อ subject
        # หลังจากที่เธอกด search แล้ว เธอพบว่าวิชาที่เธฮ search ไปปรากฏอยู่หลังหัวข้อ subject
        # find element 'h2'  = subject_head var
        # check if 'following text' is equal to subject_head var
        subject_head = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('subject : Programming Fundamental', subject_head)

        # test search result
        # เธอเห็นผลของการ search ของเธอ หลังจากที่กดปุ่ม search ไป
        # find element 'p2'  = result_search var
        # check if 'following text' is equal to result_search var
        result_search = self.browser.find_element_by_tag_name('p2').text
        self.assertEqual("Semister2 : Algorithms and Data Structures\nSemister5 : Operating Systems", result_search)

        # test Note
        # เธอเห็นประโยคด้านล่างเกี่ยวกับวิชาเลือก
        # find element 'p3'  = note var
        # check if 'following text' is equal to note var
        note = self.browser.find_element_by_tag_name('p3').text
        self.assertEqual(
            "Note : Elective Subjects don't connect to each other but I want to show how many elective subjects are in this flow.",
            note)
        # finish test text
        #self.fail('Finish the test!')

    def test_flow_pic(self):
        # เธอคลิกเข้ามาที่ link flow
        # go to flow page
        # wait for 5s
        self.browser.get('http://localhost:8000/flow.html')
        time.sleep(5)

        # test fullflow button
        # เธออยากดูภาพรวมของวิชาทั้งหมดที่เธอต้องเรียน
        # เธอจึงคลิกไปที่ปุ่ม Full Flow เพื่อไปยังรูป flow

        # find element 'id'  = flow_button var
        # click flow button
        flow_button = self.browser.find_element_by_id("fullflow_button")
        flow_button.click()

        # test can find the flow picture
        # เธอเห็นภาพวิชาตัวต่อทั้งหมด
        # find element 'id'  = flow_image var
        # check if 'image' is equal to flow_image.attribute var
        # wait for 10s
        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(10)

        # finish test text
        #self.fail('Finish the test!')

    def test_home(self):
        # เมื่อเขากดเข้าไปที่หน้า signup
        # go to signup page
        self.browser.get('http://localhost:8000/signup')

        # find element 'id'  = username_box var
        # find element 'id'  = password_box var
        # find element 'id'  = password_box2 var

        username_box = self.browser.find_element_by_id("id_username")

        password_box = self.browser.find_element_by_id("id_password1")

        password_box2 = self.browser.find_element_by_id("id_password2")

        # เขาทำการสมัคร username jesselingard
        # password lingard123456789
        # password2 lingard123456789

        # username_box input
        # password_box input
        # password_box2 input
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        password_box2.send_keys('lingard123456789')

        # เขาทำการกดปุ่ม signup
        # find element 'id'  = signup_button var
        # click signup_button
        # wait for 2s
        signup_button = self.browser.find_element_by_tag_name("button")
        signup_button.click()
        time.sleep(2)

        # เขาเข้าไปที่หน้า login
        # go to login page
        # find element 'h2'  = header_text var
        # check if 'Log in' is in header_text var
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', header_text)

        # find element 'id'  = username_login_box var
        # find element 'id'  = password_login_box var
        username_login_box = self.browser.find_element_by_id("id_username")

        password_login_box = self.browser.find_element_by_id("id_password")

        # เขาใส่ id password
        # username_login_box input
        # password_login_box input
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')

        # เขากดปุ่ม login
        # find element 'name'  = login_button var
        # click login_button
        # wait for 2s
        login_button = self.browser.find_element_by_tag_name("button")
        login_button.click()
        time.sleep(2)

        # เขาเข้าไปที่หน้า homepage
        # go to home page
        # find element 'h4'  = id_user var
        # check if 'jesselingard' is in id_user var
        self.browser.get('http://127.0.0.1:8000/home')
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)

        # เขาใส่ unit
        # find element 'id'  = unit_text var
        # unit_text input
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')

        # เขาใส่ Grade
        # find element 'id'  = unit_text var
        # unit_text input
        # wait for 3s
        unit_text = self.browser.find_element_by_id('subject1Gradeid')
        unit_text.send_keys('Grade: 2.5&nbsp; (C+)')
        time.sleep(3)

        # เขาเห็นเกรดแสดงขึ้นมา
        # find element 'id'  = submit_button var
        # click submit_button
        # wait for 3s
        submit_button = self.browser.find_element_by_id("submit")
        submit_button.click()
        time.sleep(3)
        # find element 'id'  = submit_text var
        # check if '2.5' is in submit_text var
        # wait for 6s
        submit_text = self.browser.find_element_by_id('gradeshow').text
        self.assertIn('2.5', submit_text)
        time.sleep(6)

        # เขาเห็นสาถานะนักศึกษาของเขา
        # check if 'Normal ' is in submit_text var
        self.assertIn('Normal State', submit_text)
        # finish test
        #self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

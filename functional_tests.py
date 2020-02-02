from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #เอิร์ธได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        #จึงเข้าเว็บไปที่หน้า Homepage

        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        #เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        #Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        #Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        #check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        #check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        #check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        #check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        #check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        #Checking type Username Password ##!WRONG PASSWORD
        '''
        username_box.send_keys('jesselingard')
        password_box.send_keys('123456789')
        login_button.click()
        time.sleep(2)
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        error_message = self.browser.find_elements_by_xpath("//ul[@class='errorlist nonfield']").text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.', error_message)
        time.sleep(20)'''
        #Check Type Username Pass RIGHT !
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        login_button.click()
        time.sleep(2)
        #Check Redirect !!!!!
        
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)


        logout_link = self.browser.find_element_by_link_text('Log out').text
        self.assertIn('Log out', logout_link)

        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : jesselingard', id_text)

        time.sleep(20)




        '''Check Click Link
        homepage_click = self.browser.find_element_by_link_text('Home page')
        homepage_click.click()
        time.sleep(2)'''

        '''End of Checking Login'''

        #เขาพบว่ามี 2 link ให้เลือกคือ Flow กับหน้า grade calculator
        link_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('Grade calculation', link_text)
        self.assertIn('Flow', link_text)


        #เขาสังเกตุเห็น term ที่เขาจะต้องเลือก
        term_text = self.browser.find_element_by_tag_name('term').text
        self.assertIn('Select your term :', term_text)

        #พอคลิกเข้าไปเขาจะต้องเห็น term ต่างๆให้เลือก
        self.assertIn('term 1', term_text)
        self.assertIn('term 2', term_text)
        self.assertIn('term 3', term_text)
        self.assertIn('term 4', term_text)
        self.assertIn('term 5', term_text)
        self.assertIn('term 6', term_text)
        self.assertIn('term 7', term_text)
        self.assertIn('term 8', term_text)

        #เขาจะเห็นช่องสำหรับใส่วิชาเรียน
        inputbox = self.browser.find_element_by_id('subject1')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter subject'
        )

        #เขาเห็นช่องสำหรับใส่หน่วยกิจ
        unit_text = self.browser.find_element_by_tag_name('subject1').text

        #จะมีหน่วยกิจต่างๆให้เลือก
        self.assertIn('Unit: 1', unit_text)
        self.assertIn('Unit: 2', unit_text)
        self.assertIn('Unit: 3', unit_text)
        self.assertIn('Unit: 4', unit_text)

        #เขาเห็นช่องสำหรับใส่เกรด
        grade_text = self.browser.find_element_by_tag_name('subject1').text

        #จะมีเกรดต่างๆให้เลือก
        self.assertIn('Grade: A', grade_text)
        self.assertIn('Grade: B', grade_text)
        self.assertIn('Grade: C', grade_text)
        self.assertIn('Grade: D', grade_text)

        #เขาเห็นส่วนสำหรับแสดงเกรด
        grade_show = self.browser.find_element_by_tag_name('showgrade').text
        self.assertIn('GPA', grade_show)
        self.assertIn('GPAX', grade_show)

        #เขาเห็นส่วนที่จะแสดงกราฟ


        #เขาเลือกเทอมแล้วกดปุ่ม select

        #เขาใส่วิชา circuit ลงไป
        inputbox.send_keys('Circuits')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Circuits' for row in rows),
            "Subject item did not appear in table"
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

if __name__ == '__main__':
    unittest.main(warnings='ignore')

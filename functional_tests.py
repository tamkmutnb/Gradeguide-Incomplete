# import selenium webdriver, time and unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
    def test_can_check_index_page_element(self):
        # เอิร์ธได้ยินมาว่ามีเว็บในการคำนวณเกรดและอยากจะใช้งาน
        # จึงเข้าเว็บไปที่หน้า Homepage

        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('GradeGuide', self.browser.title)
        # ! find element 'h1' as text = header_text var
        # ! header_text = self.browser.find_element_by_tag_name('h1').text
        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADEGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADEGUIDE', header_link)

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
        time.sleep(5)

        # Check User Loging in
        # find element 'link'  = login_click var
        # find element 'link'  = about_link var
        login_link = self.browser.find_element_by_partial_link_text('LOGIN')
        # check if 'LOGIN' is in signup_link var
        login_link.click()
        self.assertIn('Login_Page', self.browser.title)
        time.sleep(2)

        # check if browser title is empty as it should
        self.assertIn('', self.browser.title)

        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADEGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADEGUIDE', header_link)

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

    def test_can_check_wrong_userlogin_errormessage(self):
        # BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('GradeGuide', self.browser.title)

        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADEGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADEGUIDE', header_link)

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
        self.assertIn('Login_Page', self.browser.title)
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
        # login_class = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_buttonnew.click()
        # login_class.click()
        time.sleep(2)
        # find element 'ul'  = error_message var
        # check if 'following text' is in error_message var
        error_message = self.browser.find_element_by_xpath("//form[@id='login_form']/ul[1]").text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)
        time.sleep(2)

    def test_can_check_correct_userlogin(self):
        # BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('GradeGuide', self.browser.title)

        # find element 'link' as text
        header_link = self.browser.find_element_by_link_text('GRADEGUIDE').text
        # check if 'GradeGuide' is in header_text var
        self.assertIn('GRADEGUIDE', header_link)

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
        # time.sleep(2)
        password_box.send_keys('O87525o135@')
        # time.sleep(2)
        login_buttonnew = self.browser.find_element_by_name('login_button_name')
        # login_class = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_buttonnew.click()
        # login_class.click()
        # time.sleep(2)

        # Check Redirect !!!!!
        ''' will add home_page element test later'''
        broswer_title = self.browser.title
        self.assertIn('Home', broswer_title)

        # check if username shown is right
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('tamtong007', id_user)

        subject_dropdown = self.browser.find_element_by_name('subjectTerm').text
        self.assertIn('Term: 1\nTerm: 2\nTerm: 3\nTerm: 4\nTerm: 5\nTerm: 6\nTerm: 7\nTerm: 8', subject_dropdown)
        # time.sleep(2)

        # subject_dropdown.Select('Term: 1')
        # time.sleep(2)

        dropdown_click = self.browser.find_element_by_id('subjectTermid')
        dropdown_click.click()
        # time.sleep(2)

        # select = Select(driver.find_element_by_xpath("//select[@name='name']"))
        # all_selected_options = select.all_selected_options

        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        term1_selected_options = select_term.select_by_value('1')
        # time.sleep(2)

        '''check table header from 1-4'''

        table_element_1 = self.browser.find_element_by_xpath("//tr[@id='table']/th[1]").text
        self.assertIn('No.', table_element_1)

        table_element_2 = self.browser.find_element_by_xpath("//tr[@id='table']/th[2]").text
        self.assertIn('Subject', table_element_2)

        table_element_3 = self.browser.find_element_by_xpath("//tr[@id='table']/th[3]").text
        self.assertIn('Unit', table_element_3)

        table_element_4 = self.browser.find_element_by_xpath("//tr[@id='table']/th[4]").text
        self.assertIn('Grade', table_element_4)

        '''
        Check  of subject (1-9)
        -1 table number
        -2 subject input box
        -3 unit value
        -4 grade value
        -
         '''
        for i in range(1, 10, 1):
            subject_table_num = self.browser.find_element_by_id("table_number_" + str(i)).text
            table_num = self.browser.find_element_by_id("table_number_" + str(i)).text
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name').text
            self.assertIn(str(i), subject_table_num)
            self.assertIn(str(i), table_num)
            self.assertIn('', subject_input_box)
            for j in range(1, 10, 1):
                if (j <= 5):
                    subject_unit = self.browser.find_element_by_xpath(
                        '//select[@id='+"'subject" + str(i) + "Unitid']/option[" + str(j) + ']').text

                subject_grade = self.browser.find_element_by_xpath('//select[@id='+"'subject" + str(i) + "Gradeid']/option["+str(j)+ ']').text

                if (j == 1):
                    self.assertIn('', subject_unit)
                    self.assertIn('', subject_grade)
                if (j == 2):
                    self.assertIn('Unit: 1', subject_unit)
                    self.assertIn('  Grade: 4  (A)', subject_grade)
                if (j == 3):
                    self.assertIn('Unit: 2', subject_unit)
                    self.assertIn('Grade: 3.5 (B+)', subject_grade)
                if (j == 4):
                    self.assertIn('Unit: 3', subject_unit)
                    self.assertIn(' Grade: 3  (B)', subject_grade)
                if (j == 5):
                    self.assertIn('Unit: 4', subject_unit)
                    self.assertIn('Grade: 2.5  (C+)', subject_grade)
                if (j == 6):
                    self.assertIn(' Grade: 2  (C)', subject_grade)
                if (j == 7):
                    self.assertIn('Grade: 1.5  (D+)', subject_grade)
                if (j == 8):
                    self.assertIn('  Grade: 1  (D)', subject_grade)
                if (j == 9):
                    self.assertIn('Grade: 0  (F)', subject_grade)

                # Check submit and save button
                submit_button = self.browser.find_element_by_id('submit_button').text
                save_button = self.browser.find_element_by_id('save_button').text
                self.assertIn('Submit', submit_button)
                self.assertIn('', save_button)
                # Check your gpa and student status element
                your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
                student_status_text = self.browser.find_element_by_name('student_status_text').text
                self.assertIn('Your GPA :', your_gpa_text)
                self.assertIn('Student Status :', student_status_text)

    def test_can_check_user_grade_input_each_term(self):
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
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

        # Check Type Username Pass RIGHT !
        # User input username
        # User in put password
        username_box.send_keys('tamtong007')
        # time.sleep(2)
        password_box.send_keys('O87525o135@')
        # time.sleep(2)
        login_buttonnew = self.browser.find_element_by_name('login_button_name')
        # login_class = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_buttonnew.click()
        # login_class.click()
        # time.sleep(2)

        broswer_title = self.browser.title
        self.assertIn('Home', broswer_title)

        # check if username shown is right
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('tamtong007', id_user)

        subject_dropdown = self.browser.find_element_by_name('subjectTerm').text
        self.assertIn('Term: 1\nTerm: 2\nTerm: 3\nTerm: 4\nTerm: 5\nTerm: 6\nTerm: 7\nTerm: 8', subject_dropdown)
        # time.sleep(2)

        # subject_dropdown.Select('Term: 1')
        # time.sleep(2)

        '''check table header from 1-4'''

        table_element_1 = self.browser.find_element_by_xpath("//tr[@id='table']/th[1]").text
        self.assertIn('No.', table_element_1)

        table_element_2 = self.browser.find_element_by_xpath("//tr[@id='table']/th[2]").text
        self.assertIn('Subject', table_element_2)

        table_element_3 = self.browser.find_element_by_xpath("//tr[@id='table']/th[3]").text
        self.assertIn('Unit', table_element_3)

        table_element_4 = self.browser.find_element_by_xpath("//tr[@id='table']/th[4]").text
        self.assertIn('Grade', table_element_4)

        '''
        Check  of subject (1-9)
        -1 table number
        -2 subject input box
        -3 unit value
        -4 grade value
        -
         '''
        for i in range(1, 10, 1):
            subject_table_num = self.browser.find_element_by_id("table_number_" + str(i)).text
            table_num = self.browser.find_element_by_id("table_number_" + str(i)).text
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name').text
            self.assertIn(str(i), subject_table_num)
            self.assertIn(str(i), table_num)
            self.assertIn('', subject_input_box)
            for j in range(1, 10, 1):
                if (j <= 5):
                    subject_unit = self.browser.find_element_by_xpath(
                        '//select[@id=' + "'subject" + str(i) + "Unitid']/option[" + str(j) + ']').text

                subject_grade = self.browser.find_element_by_xpath(
                    '//select[@id=' + "'subject" + str(i) + "Gradeid']/option[" + str(j) + ']').text

                if (j == 1):
                    self.assertIn('', subject_unit)
                    self.assertIn('', subject_grade)
                if (j == 2):
                    self.assertIn('Unit: 1', subject_unit)
                    self.assertIn('  Grade: 4  (A)', subject_grade)
                if (j == 3):
                    self.assertIn('Unit: 2', subject_unit)
                    self.assertIn('Grade: 3.5 (B+)', subject_grade)
                if (j == 4):
                    self.assertIn('Unit: 3', subject_unit)
                    self.assertIn(' Grade: 3  (B)', subject_grade)
                if (j == 5):
                    self.assertIn('Unit: 4', subject_unit)
                    self.assertIn('Grade: 2.5  (C+)', subject_grade)
                if (j == 6):
                    self.assertIn(' Grade: 2  (C)', subject_grade)
                if (j == 7):
                    self.assertIn('Grade: 1.5  (D+)', subject_grade)
                if (j == 8):
                    self.assertIn('  Grade: 1  (D)', subject_grade)
                if (j == 9):
                    self.assertIn('Grade: 0  (F)', subject_grade)

                # Check submit and save button
                submit_button = self.browser.find_element_by_id('submit_button').text
                save_button = self.browser.find_element_by_id('save_button').text
                self.assertIn('Submit', submit_button)
                self.assertIn('', save_button)
                # Check your gpa and student status element
                your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
                student_status_text = self.browser.find_element_by_name('student_status_text').text
                self.assertIn('Your GPA :', your_gpa_text)
                self.assertIn('Student Status :', student_status_text)

        # create list subject first contain 9 index
        list_subject_term1 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term2 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term3 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term4 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term5 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term6 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term7 = ['', '', '', '', '', '', '', '', '', '']
        list_subject_term8 = ['', '', '', '', '', '', '', '', '', '']

        for i in range(0, 10, 1):
            # create input each term subject
            list_subject_term1[i] = 'term1_subject' + str(i)
            list_subject_term2[i] = 'term2_subject' + str(i)
            list_subject_term3[i] = 'term3_subject' + str(i)
            list_subject_term4[i] = 'term4_subject' + str(i)
            list_subject_term5[i] = 'term5_subject' + str(i)
            list_subject_term6[i] = 'term6_subject' + str(i)
            list_subject_term7[i] = 'term7_subject' + str(i)
            list_subject_term8[i] = 'term8_subject' + str(i)

        '''term 1 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('1')
        for i in range (1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term1[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject'+str(i)+'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject'+str(i)+'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 2 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('2')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term2[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 3 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('3')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term3[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 4 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('4')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term4[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 5 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('5')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term5[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 6 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('6')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term6[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 7 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('7')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term7[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #time.sleep(2)
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

        '''term 8 user input'''
        # Check submit and save button
        submit_button = self.browser.find_element_by_id('submit_button').text
        save_button = self.browser.find_element_by_id('save_button').text
        self.assertIn('Submit', submit_button)
        self.assertIn('', save_button)

        # get element submit and save button for clicking
        submit_click = self.browser.find_element_by_id('submit_button')
        save_click = self.browser.find_element_by_id('save_button')

        # Check your gpa and student status element
        your_gpa_text = self.browser.find_element_by_name('your_gpa_text').text
        student_status_text = self.browser.find_element_by_name('student_status_text').text
        self.assertIn('Your GPA :', your_gpa_text)
        self.assertIn('Student Status :', student_status_text)

        # user click dropdown to select term
        select_term = Select(self.browser.find_element_by_id('subjectTermid'))
        select_term.select_by_value('8')
        for i in range(1, 10, 1):
            # user input
            # input subject name
            subject_input_box = self.browser.find_element_by_name('subject' + str(i) + 'name')

            subject_input_box.send_keys(list_subject_term8[i])

            print(subject_input_box.text)
            # input subject unit
            unit_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Unitid')
            unit_dropdown.send_keys('Unit: 3')
            # input subject grade
            grade_dropdown = self.browser.find_element_by_id('subject' + str(i) + 'Gradeid')
            grade_dropdown.send_keys('Grade: 2.5&nbsp; (C+)')
            #
        # user click submit button
        submit_click.click()
        # user click save button
        save_click.click()
        #time.sleep(2)

    def test_can_check_element(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get("http://127.0.0.1:8000/r'fifthTerm'")
        time.sleep(20)


    def test_can_check_flow_page_element(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')
        self.assertIn('Flow', self.browser.title)
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
        # self.fail('Finish the test!')

    def test_can_check_search_fucntion_and_button(self):
        # เธอคลิกเข้ามาที่ link flow
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('Flow', self.browser.title)

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
        # self.fail('Finish the test!')

    def test_can_recieve_userinput_and_return_flow_image(self):
        # เธอคลิกเข้ามาที่ link flow
        # go to flow page
        # wait for 5s
        self.browser.get('http://localhost:8000/flow.html')
        self.assertIn('Flow', self.browser.title)
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
        # check image id of stat picture and image in picFlow.html
        # wait for 10s
        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(10)

        # finish test text
        # self.fail('Finish the test!')

    def grade_calculator_check_element(self):
        # เมื่อเขากดเข้าไปที่หน้า signup
        # go to signup page
        self.browser.get('http://localhost:8000/signup')
        self.assertIn('Signup_Page', self.browser.title)

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
        # signup_button = self.browser.find_element_by_tag_name("button")
        # signup_button.click()
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
        self.assertIn('Home', header_text)
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)

        # เขาใส่ unit
        # find element 'id'  = unit_text var
        # unit_text input
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')

        '''*should add grade input for all 8 in term'''
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
        # self.fail('Finish the test!')

    def test_home(self):
        # เมื่อเขากดเข้าไปที่หน้า signup
        # go to signup page
        self.browser.get('http://localhost:8000/signup')
        self.assertIn('Signup_Page', self.browser.title)

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
        # signup_button = self.browser.find_element_by_tag_name("button")
        # signup_button.click()
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
        self.assertIn('Home', header_text)
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)

        # เขาใส่ unit
        # find element 'id'  = unit_text var
        # unit_text input
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')

        '''*should add grade input for all 8 in term'''
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
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

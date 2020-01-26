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

        #เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('Grade-Guide', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Grade-Guide', header_text)

        #เขาพบว่ามี 2 link ให้เลือกคือ Flow กับหน้า grade calculator
        link_text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('Grade Calulator', link_text)
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

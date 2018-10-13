import unittest
from make_website import *


class TestMakeWebsite(unittest.TestCase):
    def test_detect_name(self):
        self.assertEqual('Riddhi', detect_name('Riddhi'), 'Name detected incorrectly')
        self.assertEqual('Riddhi123', detect_name('Riddhi123'), 'Name detected incorrectly')
        self.assertEqual('R123iddhi', detect_name('R123iddhi'), 'Name detected incorrectly')
        self.assertRaises( Exception, lambda: detect_name('riddhi'), 'Name detected incorrectly')
        self.assertRaises(Exception, lambda: detect_name('12riddhi'), 'Name detected incorrectly')

    def test_get_index(self):
        test_list = ['@', ',', 'Projects', 'Courses', 'Name']

        self.assertEqual(4, get_index('Name', test_list))
        self.assertEqual(-1, get_index('inexistent_string', test_list), 'Index not fetched successfully')

    def test_check_email_validity(self):
        self.assertEqual(False, check_email_validity('abc@g-mail.com'), 'Invalid E-mail')
        self.assertEqual(False, check_email_validity('lbrandon@wharton.upenn.edu'), 'Invalid E-mail')
        self.assertEqual(False, check_email_validity('Abc@gmail.com'), 'Invalid E-mail')

        self.assertEqual(True, check_email_validity('abc2@Gmail.com'), 'Invalid E-mail')
        self.assertEqual(True, check_email_validity('ab-c@Gmail.com'), 'Invalid E-mail')
        self.assertEqual(True, check_email_validity('brandon.l@wharton.upenn.com'), 'Invalid E-mail')
        self.assertEqual(True, check_email_validity('lbrandon2@wharton.upenn.com'), 'Invalid E-mail')

    def test_detect_email(self):
        self.assertEqual('abc@g-mail.com', detect_email('abc@g-mail.com'), 'Detecting e-mail failed')
        self.assertEqual('lbrandon@wharton.upenn.edu', detect_email('lbrandon@wharton.upenn.edu'), 'Detecting e-mail failed')
        self.assertEqual('Abc@gmail.com', detect_email('Abc@gmail.com'), 'Detecting e-mail failed')

        self.assertEqual('', detect_email('lbrandon2@wharton.upenn.com'), 'Detecting e-mail failed')
        self.assertEqual('', detect_email('ab-c@Gmail.com'), 'Detecting e-mail failed')
        self.assertEqual('', detect_email('abc2@Gmail.com'), 'Detecting e-mail failed')

    def test_detect_courses(self):
        test_courses_string = 'Courses - CIS 540 - Operating Systems, ESE 532 - System on Chip, ' \
                         'CIT 590 - Programming Languages and Techniques, ESE 519 - Real-time Embedded Systems'
        response_list = ['CIS 540 - Operating Systems', ' ESE 532 - System on Chip', ' CIT 590 - Programming Languages and Techniques', ' ESE 519 - Real-time Embedded Systems']

        test_courses_string1 = 'Courses   CIT 590,ESE 532,CIS 548'
        response_list1 = ['CIT 590', 'ESE 532', 'CIS 548']

        test_courses_string2 = 'Courses :- CIT 590,ESE 532,CIS 548'
        response_list2 = ['CIT 590', 'ESE 532', 'CIS 548']

        test_courses_string3 = 'Courses : CIT 590,ESE 532,CIS 548'
        response_list3 = ['CIT 590', 'ESE 532', 'CIS 548']

        test_courses_string4 = 'Courses- CIT 590,ESE 532,CIS 548'
        response_list4 = ['CIT 590', 'ESE 532', 'CIS 548']

        self.assertEqual(response_list, detect_courses(test_courses_string), 'Courses detected incorrectly')
        self.assertEqual(response_list1, detect_courses(test_courses_string1), 'Courses detected incorrectly')
        self.assertEqual(response_list2, detect_courses(test_courses_string2), 'Courses detected incorrectly')
        self.assertEqual(response_list3, detect_courses(test_courses_string3), 'Courses detected incorrectly')
        self.assertEqual(response_list4, detect_courses(test_courses_string4), 'Courses detected incorrectly')

    def test_detect_projects(self):
        test_file_list1 = ['   Projects', 'A', 'B', 'C', '  D', '-'*10]
        test_file_list2 = ['   Projects', 'A', 'B', 'C', '  D', '-'*4]
        test_file_list3 = ['Projects', 'A', 'B', 'C', '  D', '-'*50]
        test_file_list4 = ['   Projects', 'A', 'B', ' \n', '  D', '-'*10]
        test_file_list5 = ['   Projects', 'A', 'B', '    ', '  D', '-'*10]

        self.assertEqual(['A', 'B', 'C', 'D'], detect_projects(test_file_list1), "The project detection is incorrect")
        self.assertEqual([], detect_projects(test_file_list2), "The project detection is incorrect")
        self.assertEqual(['A', 'B', 'C', 'D'], detect_projects(test_file_list3), "The project detection is incorrect")
        self.assertEqual(['A', 'B', 'D'], detect_projects(test_file_list4), "The project detection is incorrect")
        self.assertEqual(['A', 'B', 'D'], detect_projects(test_file_list5), "The project detection is incorrect")

    def test_surround_block(self):
        self.assertEqual('<h1>test_text</h1>', surround_block('h1', 'test_text   '),
                         'The formatted string with HTML tags not formed correctly')
        self.assertEqual('<h1>test_text</h1>', surround_block('h1', 'test_text'),
                         'The formatted string with HTML tags not formed correctly')
        self.assertEqual('<h1>test_text</h1>', surround_block('h1    ', 'test_text   '),
                         'The formatted string with HTML tags not formed correctly')


if __name__ == '__main__':
    unittest.main()

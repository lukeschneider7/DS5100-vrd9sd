import unittest
from student import Student

class StudentTestCase(unittest.TestCase):
    def test_01(self):
        student1 = Student('katherine', ['ds5100'] )
        student1.enroll_in_course('CS 200')
        actual = student1.num_courses
        expected = 2
        self.assertEqual(actual, expected)

    def test_02(self):
        pass

    def test_03(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=3)
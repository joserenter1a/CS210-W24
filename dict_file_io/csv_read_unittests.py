from csv_read_sol import create_student_roster
import unittest

class TestCases(unittest.TestCase):

    def test_whole_dict(self):
        roster = {'Senior': [('Jose', 22), ('Jessica', 26), ('Ashley', 25), ('Brandon', 26), ('Victoria', 25), ('Emma', 26), ('Evelyn', 25)], 'Freshman': [('John', 18), ('Ali', 18), ('William', 19), ('Isabella', 20), ('Natalie', 20), ('Ethan', 19), ('Aiden', 20), ('Emily', 20), ('Noah', 19), ('Harper', 19)], 'Sophomore': [('Michael', 20), ('Miguel', 19), ('Olivia', 22), ('Daniel', 21), ('Jacob', 22), ('Ava', 21), ('Madison', 22), ('Chloe', 21), ('Jacob', 22), ('Michael', 21), ('Grace', 22), ('Avery', 21), ('Elijah', 22), ('Mia', 21)], 'Graduate': [('Kevin', 28), ('Josephine', 38), ('David', 32), ('Richard', 28), ('Samantha', 27), ('Christopher', 31), ('Sophia', 29), ('Lily', 27), ('Benjamin', 30), ('Abigail', 28), ('Logan', 30), ('Makayla', 27)], 'Junior': [('Sara', 20), ('Alexa', 21), ('Emily', 23), ('Megan', 24), ('Anthony', 23), ('Nicholas', 24), ('Andrew', 23), ('Caleb', 24), ('Ethan', 24)]}
        output = create_student_roster('roster.csv')
        self.assertEqual(output, roster)

    def test_just_freshmen(self):
        freshmen = [('John', 18), ('Ali', 18), ('William', 19), ('Isabella', 20), ('Natalie', 20), ('Ethan', 19), ('Aiden', 20), ('Emily', 20), ('Noah', 19), ('Harper', 19)]
        output = create_student_roster('roster.csv', 'Freshman')
        self.assertEqual(output, freshmen)

    def test_just_sophs(self):
        seniors =  [('Michael', 20), ('Miguel', 19), ('Olivia', 22), ('Daniel', 21), ('Jacob', 22), ('Ava', 21), ('Madison', 22), ('Chloe', 21), ('Jacob', 22), ('Michael', 21), ('Grace', 22), ('Avery', 21), ('Elijah', 22), ('Mia', 21)]
        output = create_student_roster('roster.csv', 'Sophomore')
        self.assertEqual(output, seniors)

    def test_just_juniors(self):
        seniors =  [('Sara', 20), ('Alexa', 21), ('Emily', 23), ('Megan', 24), ('Anthony', 23), ('Nicholas', 24), ('Andrew', 23), ('Caleb', 24), ('Ethan', 24)]
        output = create_student_roster('roster.csv', 'Junior')
        self.assertEqual(output, seniors)

    def test_just_seniors(self):
        seniors =  [('Jose', 22), ('Jessica', 26), ('Ashley', 25), ('Brandon', 26), ('Victoria', 25), ('Emma', 26), ('Evelyn', 25)]
        output = create_student_roster('roster.csv', 'Senior')
        self.assertEqual(output, seniors)



if __name__ == '__main__':
    unittest.main()
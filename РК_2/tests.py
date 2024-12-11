import unittest
from main import Group, Faculty, GroupFaculty, task1, task2, task3


class TestTasks(unittest.TestCase):

    def setUp(self):
        self.faculties = [
            Faculty(1, "Информатика и системы управления"),
            Faculty(2, "Инженерный бизнес и менеджмент"),
            Faculty(3, "Робототехника и комплексная автоматизация"),
            Faculty(4, "Фундаментальные науки"),
            Faculty(5, "Энергомашиностроение")
        ]

        self.groups = [
            Group(1, "ИУ5ц", 5, 1, 1, 28),
            Group(2, "ИУ6ц", 5, 2, 1, 24),
            Group(3, "ИУ7", 3, 3, 1, 29),
            Group(4, "ИБМ7", 3, 4, 2, 27),
            Group(5, "РК6", 3, 5, 3, 28),
            Group(6, "РК9", 3, 1, 3, 27),
            Group(7, "ФН12", 3, 2, 4, 21),
            Group(8, "ФН12", 3, 3, 4, 26),
            Group(9, "Э9ц", 5, 4, 5, 24)
        ]

        self.groups_faculties = [
            GroupFaculty(1, 1),
            GroupFaculty(2, 1),
            GroupFaculty(3, 1),
            GroupFaculty(4, 2),
            GroupFaculty(5, 3),
            GroupFaculty(6, 3),
            GroupFaculty(7, 4),
            GroupFaculty(8, 4),
            GroupFaculty(9, 5)
        ]

    def test_task1(self):
        result = task1(self.faculties, self.groups)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0].name, "ИУ5ц-51")
        self.assertEqual(result[0][1].title, "Информатика и системы управления")

    def test_task2(self):
        result = task2(self.faculties, self.groups)
        self.assertEqual(result["Информатика и системы управления"], 29)
        self.assertEqual(result["Инженерный бизнес и менеджмент"], 27)
        self.assertEqual(result["Робототехника и комплексная автоматизация"], 28)
        self.assertEqual(result["Фундаментальные науки"], 26)
        self.assertEqual(result["Энергомашиностроение"], 24)

    def test_task3(self):
        result = task3(self.faculties, self.groups, self.groups_faculties)
        self.assertEqual(len(result), 9)
        self.assertEqual(result[0][0].name, "ИБМ7-34")
        self.assertEqual(result[0][1].title, "Инженерный бизнес и менеджмент")
        self.assertEqual(result[8][0].name, "Э9ц-54")
        self.assertEqual(result[8][1].title, "Энергомашиностроение")


if __name__ == "__main__":
    unittest.main()
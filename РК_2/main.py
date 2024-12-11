class Group:
    def __init__(self, id: int, department: str, sem: int, index: int, faculty_id: int, students: int):
        self._id = id
        self._name = f"{department}-{sem}{index}"
        self._faculty_id = faculty_id
        self._students = students

    @property
    def id(self) -> int:
        return self._id

    @property
    def faculty_id(self) -> int:
        return self._faculty_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def students(self) -> int:
        return self._students


class Faculty:
    def __init__(self, id: int, title: str):
        self._id = id
        self._title = title

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title


class GroupFaculty:
    def __init__(self, group_id: int, faculty_id: int):
        self._group_id = group_id
        self._faculty_id = faculty_id

    @property
    def faculty_id(self) -> int:
        return self._faculty_id

    @property
    def group_id(self) -> int:
        return self._group_id


def task1(faculties: list[Faculty], groups: list[Group]) -> list[tuple[Group, Faculty]]:
    return [(g, c)
            for g in groups
            for c in faculties
            if (g.faculty_id == c.id and g.name.startswith("ИУ"))]


def task2(faculties: list[Faculty], groups: list[Group]) -> dict[str, int]:
    data = {}
    for faculty in faculties:
        faculty_students = [g.students
                            for g in groups
                            if (g.faculty_id == faculty.id)]
        if faculty_students:
            data[faculty.title] = max(faculty_students)
    return data


def task3(faculties: list[Faculty], groups: list[Group], groups_faculties: list[GroupFaculty]) -> list[tuple[Group, Faculty]]:
    data = [(g, f)
            for gf in groups_faculties
            for g in groups
            for f in faculties
            if gf.group_id == g.id and gf.faculty_id == f.id]

    data.sort(key=lambda x: x[0].name)
    return data


def main():
    faculties = [
        Faculty(1, "Информатика и системы управления"),
        Faculty(2, "Инженерный бизнес и менеджмент"),
        Faculty(3, "Робототехника и комплексная автоматизация"),
        Faculty(4, "Фундаментальные науки"),
        Faculty(5, "Энергомашиностроение")
    ]

    groups = [
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

    groups_faculties = [
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

    # Вывод результатов
    print("Запрос № 1")
    for (g, c) in task1(faculties, groups):
        print(g.name, c.title)
    print()

    print("Запрос № 2")
    data_items = list(task2(faculties, groups).items())
    data_items.sort(key=lambda x: x[1])
    for (faculty, max_students) in data_items:
        print(faculty, max_students)
    print()

    print("Запрос № 3")
    for (group, course) in task3(faculties, groups, groups_faculties):
        print(group.name, course.title)
    print()


if __name__ == "__main__":
    main()
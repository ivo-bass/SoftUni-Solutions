from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('S2', {'python': ['some note']})

    def test_student_init(self):
        student_2 = Student('S1')
        self.assertEqual('S1', student_2.name)
        self.assertDictEqual({}, student_2.courses)
        self.assertDictEqual({'python': ['some note']}, self.student.courses)

    def test_leave_course__should_return_msg(self):
        expected = "Course has been removed"
        actual = self.student.leave_course('python')
        self.assertEqual(expected, actual)

    def test_leave_course__should_empty_dict(self):
        self.student.leave_course('python')
        self.assertDictEqual({}, self.student.courses)

    def test_leave_course__with_invalid_name__should_raise_exception(self):
        with self.assertRaises(Exception) as exc:
            self.student.leave_course('java')
        msg = "Cannot remove course. Course not found."
        self.assertEqual(msg, str(exc.exception))

    def test_add_notes__should_return_msg(self):
        expected = "Notes have been updated"
        actual = self.student.add_notes('python', 'a note')
        self.assertEqual(expected, actual)

    def test_add_notes__should_add_note_to_list(self):
        self.student.add_notes('python', 'a note')
        expected = ['some note', 'a note']
        actual = self.student.courses['python']
        self.assertListEqual(expected, actual)

    def test_add_notes__with_invalid_course__should_raise_exception(self):
        with self.assertRaises(Exception) as exc:
            self.student.add_notes('java', 'note')
        msg = "Cannot add notes. Course not found."
        self.assertEqual(msg, str(exc.exception))

    def test_enroll__with_old_course__should_return_msg(self):
        expected = "Course already added. Notes have been updated."
        actual = self.student.enroll('python', 'a note')
        self.assertEqual(expected, actual)

    def test_enroll__with_old_course__should_update_notes(self):
        self.student.enroll('python', ['a note'])
        expected = ['some note', 'a note']
        actual = self.student.courses['python']
        self.assertEqual(expected, actual)

    def test_enroll__with_new_course_and_Y_for_notes__should_return_msg(self):
        expected = "Course and course notes have been added."
        actual = self.student.enroll('java', ['note', 'note'], add_course_notes='Y')
        self.assertEqual(expected, actual)
        actual2 = self.student.enroll('JS', ['note', 'note'])
        self.assertEqual(expected, actual2)

    def test_enroll__with_new_course_and_Y_for_notes__should_add_notes(self):
        self.student.enroll('java', ['note', 'note'], add_course_notes='Y')
        self.student.enroll('JS', ['note', 'note'])
        expected = ['note', 'note']
        actual = self.student.courses['java']
        actual2 = self.student.courses['JS']
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual2)

    def test_enroll__with_new_course_and_N_for_add_notes__should_return_msg(self):
        expected = "Course has been added."
        actual = self.student.enroll('java', ['note', 'note'], add_course_notes='No')
        self.assertEqual(expected, actual)

    def test_enroll__with_new_course_and_N_for_add_notes__should_add_course_without_notes(self):
        self.student.enroll('java', ['note', 'note'], add_course_notes='No')
        self.assertListEqual([], self.student.courses['java'])


if __name__ == '__main__':
    main()

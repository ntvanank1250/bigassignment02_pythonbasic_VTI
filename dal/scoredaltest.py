import unittest

from dal import ScoreDAL
from dto import ScoreDto


class ScoreDALTest(unittest.TestCase):
    def setUp(self):
        self.scoreDAL = ScoreDAL()
    
    def tearDown(self):
        pass

    def testInsert(self):
        studentCode = "PY000003"
        subjectCode = "111"
        scoreQT = 44
        scoreKT = 33
        a = ScoreDto(studentCode, subjectCode, scoreQT, scoreKT)

        self.scoreDAL.insert(a)
        b = self.scoreDAL.getByCode(studentCode, subjectCode)

        self.assertEqual(studentCode, b[0])
        self.assertEqual(subjectCode, b[1])
        self.assertEqual(scoreQT, b[2])
        self.assertEqual(scoreKT, b[3])

        # Tear down
        self.scoreDAL.delete(studentCode, subjectCode)

#!/bin/env python3

import unittest

class MangoTestCase(unittest.TestCase):

    def __ใส่ตะกร้า(self, ตะกร้า, ผลไม้, จำนวน):
        for _ in range(จำนวน):
            ตะกร้า.append(ผลไม้)

    def setUp(self):
        # ค่าคงที่จากโจทย์
        self.จำนวนมะม่วงของจอย = 12
        self.โจ้เก็บได้มากกว่าจอย = 8

        # คำตอบ
        self.นักเรียนตอบ_จำนวนมะม่วงของโจ้ = 20
        self.ครูเฉลย_จำนวนมะม่วงของโจ้ = 4

        # กำหนดค่าเริ่มต้น
        self.มะม่วง = '🥭'
        self.ตะกร้าของจอย = list()
        self.ตะกร้าของโจ้ = list()

        # จอยเก็บมะม่วงได้ 12 ผล
        self.__ใส่ตะกร้า(self.ตะกร้าของจอย, self.มะม่วง, self.จำนวนมะม่วงของจอย)

        # โจ้เก็บมะม่วงได้มากกว่าจอย 8 ผล
        # โจ้เริ่มต้นเก็บมะม่วงให้เท่าจอย
        self.__ใส่ตะกร้า(self.ตะกร้าของโจ้, self.มะม่วง, self.จำนวนมะม่วงของจอย)

        # แล้วโจ้เก็บต่อไปอีก 8 ผล
        self.__ใส่ตะกร้า(self.ตะกร้าของโจ้, self.มะม่วง, self.โจ้เก็บได้มากกว่าจอย)

    def test_1_จอยมีมะม่วง_12ผล(self):
        self.assertEqual(
            len(self.ตะกร้าของจอย), 12
        )

    def test_2_โจ้มีมะม่วงมากกว่าจอย(self):
        self.assertGreater(
            len(self.ตะกร้าของโจ้), len(self.ตะกร้าของจอย)
        )

    def test_3_โจ้มีมะม่วงมากกว่าจอย_8ผล(self):
        self.assertEqual(
            (len(self.ตะกร้าของโจ้) - len(self.ตะกร้าของจอย)), 8
        )

    def test_4_คำตอบของนักเรียนถูก(self):
        self.assertEqual(
            self.นักเรียนตอบ_จำนวนมะม่วงของโจ้, len(self.ตะกร้าของโจ้)
        )

    @unittest.expectedFailure
    def test_5_เฉลยของครูถูก(self):
        self.assertEqual(
            self.ครูเฉลย_จำนวนมะม่วงของโจ้, len(self.ตะกร้าของโจ้)
        )

    def test_6_คำตอบของนักเรียนไม่ขัดแย้งกับโจทย์(self):
        self.assertGreater(
            self.นักเรียนตอบ_จำนวนมะม่วงของโจ้, len(self.ตะกร้าของจอย)
        )

    @unittest.expectedFailure
    def test_7_เฉลยของครูไม่ขัดแย้งกับโจทย์(self):
        self.assertGreater(
            self.ครูเฉลย_จำนวนมะม่วงของโจ้, len(self.ตะกร้าของจอย)
        )

    def test_8_แสดงมะม่วงในตะกร้า(self):
        print('')
        print('\tมะม่วงของจอย\t: ' + ' '.join(self.ตะกร้าของจอย))
        print('\tมะม่วงของโจ้\t: ' + ' '.join(self.ตะกร้าของโจ้))


if __name__ == '__main__':
    unittest.main()

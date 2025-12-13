import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):
    def test_normal_bmi(self):
        # 測試正常BMI計算
        bmi = calculate_bmi(70, 1.75)
        self.assertAlmostEqual(bmi, 22.857142857142858, places=5)

    def test_underweight_bmi(self):
        # 測試體重過輕
        bmi = calculate_bmi(50, 1.75)
        self.assertAlmostEqual(bmi, 16.3265306122449, places=5)

    def test_overweight_bmi(self):
        # 測試過重
        bmi = calculate_bmi(80, 1.75)
        self.assertAlmostEqual(bmi, 26.122448979591837, places=5)

    def test_obese_bmi(self):
        # 測試肥胖
        bmi = calculate_bmi(100, 1.75)
        self.assertAlmostEqual(bmi, 32.6530612244898, places=5)

    def test_zero_weight(self):
        # 測試體重為0
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)

    def test_negative_weight(self):
        # 測試負體重
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.75)

    def test_zero_height(self):
        # 測試身高為0
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_negative_height(self):
        # 測試負身高
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)

if __name__ == '__main__':
    unittest.main()

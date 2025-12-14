# ..... 成績計算函式：輸入國文、英文、數學成績，回傳平均分數與等第（90以上A，80以上B，70以上C，60以上D，其他F）
def calculate_grade(chinese, english, math):
    # 輸入驗證：需為數值且介於 0 到 100 之間
    for name, score in [("國文", chinese), ("英文", english), ("數學", math)]:
        if not isinstance(score, (int, float)):
            raise TypeError(f"{name}成績必須為數值")
        if score < 0 or score > 100:
            raise ValueError(f"{name}成績需介於0到100")

    average = (chinese + english + math) / 3

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return average, grade

# ..... 互動主程式：輸入三科成績後回傳平均與等第
def input_and_calculate():
    chinese = float(input("請輸入國文成績："))
    english = float(input("請輸入英文成績："))
    math = float(input("請輸入數學成績："))

    average, grade = calculate_grade(chinese, english, math)
    print(f"平均分數：{average:.2f}，等第：{grade}")
    return average, grade

    # 備註：此函式不在測試中自動呼叫，避免互動輸入影響測試執行。

# ..... 主程式：互動取得使用者輸入並顯示等第結果
def main():
    try:
        input_and_calculate()
    except (ValueError, TypeError) as e:
        print(f"輸入錯誤：{e}")
    except Exception as e:
        print(f"發生未預期錯誤：{e}")


if __name__ == "__main__":
    main()


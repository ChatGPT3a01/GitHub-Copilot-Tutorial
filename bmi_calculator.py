def calculate_bmi(weight, height):
    """
    計算 BMI (Body Mass Index)。

    參數:
    weight (float): 體重，單位為公斤
    height (float): 身高，單位為公尺

    返回:
    float: BMI 值

    拋出:
    ValueError: 如果身高或體重不是正數
    """
    if height <= 0 or weight <= 0:
        raise ValueError("身高和體重必須是正數")
    
    return weight / (height ** 2)

# 範例使用
if __name__ == "__main__":
    # 範例：體重 70kg，身高 1.75m
    bmi = calculate_bmi(70, 1.75)
    print(f"BMI: {bmi:.2f}")
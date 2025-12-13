# 寫一個檢測BMI的程式，讓使用者輸入體重(KG)以及身高(CM)後，可以得到正確的數值

# 定義一個函數來根據BMI值提供健康建議
def get_bmi_advice(bmi):
    """
    根據 BMI 值返回對應的健康建議。

    參數:
    bmi (float): 身體質量指數 (BMI) 值。

    返回值:
    str: 根據 BMI 範圍對應的健康建議字符串。
    """
    # 定義BMI分類和對應建議的列表，每個元組包含閾值和建議
    categories = [
        (18.5, "體重過輕，建議增加營養攝取。"),
        (24, "體重正常，請保持健康的生活方式。"),
        (27, "體重過重，建議適度運動並注意飲食。"),
        (30, "輕度肥胖，建議加強運動並控制飲食。"),
        (float('inf'), "尋求醫療幫助並制定嚴格的健康管理計劃。")
    ]
    # 初始化前一個閾值為0
    prev_threshold = 0
    # 遍歷分類列表，找到BMI對應的建議
    for threshold, advice in categories:
        # 如果BMI在當前範圍內，返回對應建議
        if prev_threshold <= bmi < threshold:
            return advice
        # 更新前一個閾值
        prev_threshold = threshold
    # 如果沒有匹配，返回未知
    return "未知"

# 嘗試執行主要程式碼，處理可能的錯誤
try:
    # 提示使用者輸入體重，並轉換為浮點數
    weight = float(input("請輸入體重(公斤): "))
    # 提示使用者輸入身高，並轉換為浮點數
    height_cm = float(input("請輸入身高(公分): "))
    # 檢查身高和體重是否為正數
    if height_cm <= 0 or weight <= 0:
        # 如果不是正數，輸出錯誤訊息
        print("身高和體重必須是正數")
    else:
        # 將身高從公分轉換為公尺
        height_m = height_cm / 100  # 將身高轉換為公尺
        # 計算BMI值
        bmi = weight / (height_m ** 2)  # 計算BMI
        # 輸出BMI值，保留兩位小數
        print(f"你的BMI值為: {bmi:.2f}")
        # 獲取對應的健康建議
        advice = get_bmi_advice(bmi)
        # 輸出健康建議
        print(advice)
# 如果輸入不是有效數字，捕獲ValueError並輸出錯誤訊息
except ValueError:
    print("請輸入有效的數字")
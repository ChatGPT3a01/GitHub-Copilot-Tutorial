class 學生:
    """
    學生類別，用於儲存學生的基本資訊和分數。
    """
    def __init__(self, 姓名, 分數):
        """
        初始化學生物件。
        
        參數:
        姓名 (str): 學生的姓名。
        分數 (float): 學生的分數。
        
        拋出:
        ValueError: 當姓名為空或分數不在有效範圍內時。
        TypeError: 當參數類型不正確時。
        """
        # 驗證姓名
        if not isinstance(姓名, str):
            raise TypeError("姓名必須是字串類型")
        if not 姓名 or not 姓名.strip():
            raise ValueError("姓名不能為空")
        
        # 驗證分數
        try:
            分數 = float(分數)
        except (ValueError, TypeError):
            raise TypeError("分數必須是數字類型")
        
        if not (0 <= 分數 <= 100):
            raise ValueError(f"分數必須在 0 到 100 之間，目前為 {分數}")
        
        self.姓名 = 姓名.strip()
        self.分數 = 分數
    
    def __str__(self):
        """返回學生資訊的字串表示。"""
        return f"學生姓名: {self.姓名}, 分數: {self.分數}"


def 計算班級平均分數(學生列表):
    """
    計算班級學生的平均分數。
    
    參數:
    學生列表 (list): 包含學生物件的列表。
    
    回傳:
    float: 班級平均分數。如果列表為空，回傳 0.0。
    
    拋出:
    TypeError: 當輸入不是列表或列表中包含非學生物件時。
    ValueError: 當列表為空時。
    """
    # 驗證輸入類型
    if not isinstance(學生列表, list):
        raise TypeError("輸入必須是列表類型")
    
    # 檢查列表是否為空
    if not 學生列表:
        raise ValueError("學生列表不能為空")
    
    # 驗證列表中的每個元素都是學生物件
    for i, 項目 in enumerate(學生列表):
        if not isinstance(項目, 學生):
            raise TypeError(f"列表索引 {i} 的元素不是學生物件")
    
    try:
        總分 = sum(項目.分數 for 項目 in 學生列表)
        學生數量 = len(學生列表)
        return 總分 / 學生數量
    except AttributeError as e:
        raise TypeError(f"列表中的物件缺少必要的屬性: {e}")
    except Exception as e:
        raise RuntimeError(f"計算平均分數時發生錯誤: {e}")


# 測試範例
if __name__ == "__main__":
    print("=== 測試範例 1: 正常情況 ===")
    try:
        # 建立學生物件
        學生1 = 學生("王小明", 85)
        學生2 = 學生("李小華", 92)
        學生3 = 學生("陳大同", 78)
        學生4 = 學生("林美玲", 88)
        學生5 = 學生("張志明", 95)
        
        # 建立學生列表
        班級學生 = [學生1, 學生2, 學生3, 學生4, 學生5]
        
        # 顯示所有學生資訊
        print("班級學生名單:")
        for 某學生 in 班級學生:
            print(f"  {某學生}")
        
        # 計算並顯示平均分數
        平均分數 = 計算班級平均分數(班級學生)
        print(f"班級平均分數: {平均分數:.2f}")
    except Exception as e:
        print(f"錯誤: {e}")
    
    print("\n=== 測試範例 2: 錯誤處理 - 分數超出範圍 ===")
    try:
        無效學生 = 學生("測試學生", 150)
    except ValueError as e:
        print(f"捕獲到錯誤: {e}")
    
    print("\n=== 測試範例 3: 錯誤處理 - 姓名為空 ===")
    try:
        無效學生 = 學生("", 85)
    except ValueError as e:
        print(f"捕獲到錯誤: {e}")
    
    print("\n=== 測試範例 4: 錯誤處理 - 分數類型錯誤 ===")
    try:
        無效學生 = 學生("測試學生", "不是數字")
    except TypeError as e:
        print(f"捕獲到錯誤: {e}")
    
    print("\n=== 測試範例 5: 錯誤處理 - 空列表 ===")
    try:
        空列表 = []
        平均 = 計算班級平均分數(空列表)
    except ValueError as e:
        print(f"捕獲到錯誤: {e}")
    
    print("\n=== 測試範例 6: 錯誤處理 - 輸入非列表 ===")
    try:
        平均 = 計算班級平均分數("不是列表")
    except TypeError as e:
        print(f"捕獲到錯誤: {e}")

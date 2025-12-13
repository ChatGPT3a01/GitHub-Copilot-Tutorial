# 簡單的迭代範例，包含暫停詢問是否繼續
def main():
    counter = 1
    while True:
        print(f"這是第 {counter} 次迭代")
        # 這裡可以加入您的迭代邏輯

        # 暫停並詢問是否繼續
        response = input("要繼續迭次嗎？ (y/n): ").strip().lower()
        if response != 'y':
            print("迭代結束")
            break
        counter += 1

if __name__ == "__main__":
    main()

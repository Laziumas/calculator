def calculator():
    print("简易计算器")
    print("支持的运算：+ - * /")
    print("输入 q 退出\n")

    while True:
        expr = input("请输入算式（如 3 + 5）：").strip()

        if expr.lower() == "q":
            print("已退出，再见！")
            break

        try:
            parts = expr.split()
            if len(parts) != 3:
                print("格式错误，请按 “数字 运算符 数字” 输入，如 3 + 5\n")
                continue

            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    print("错误：除数不能为 0\n")
                    continue
                result = a / b
            else:
                print(f"不支持的运算符：{op}\n")
                continue

            print(f"结果：{result}\n")

        except ValueError:
            print("输入包含非法数字，请重试\n")


if __name__ == "__main__":
    calculator()

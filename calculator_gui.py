import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("简易计算器")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""

        # 显示屏
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Consolas", 24),
            bd=10,
            relief=tk.RIDGE,
            justify=tk.RIGHT,
            state="readonly",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # 按键布局
        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2),
        ]

        for text, row, col, *span in buttons:
            colspan = span[0] if span else 1
            btn = tk.Button(
                root, text=text, font=("Arial", 16),
                width=5, height=2,
                command=lambda t=text: self.on_click(t),
            )
            btn.grid(row=row, column=col, columnspan=colspan,
                     sticky="nsew", padx=2, pady=2)

        # 让按钮随窗口拉伸
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        # 键盘绑定
        root.bind("<Return>", lambda e: self.on_click("="))
        root.bind("<BackSpace>", lambda e: self.on_click("⌫"))
        root.bind("<Escape>", lambda e: self.on_click("C"))

    def on_click(self, key):
        if key == "C":
            self.expression = ""
            self.display_var.set("0")
        elif key == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif key == "=":
            self.calculate()
        else:
            # 防止表达式过长
            if len(self.expression) < 30:
                self.expression += key
                self.display_var.set(self.expression)

    def calculate(self):
        try:
            # 允许 % 作为取模运算，替换为 Python 的 %
            expr = self.expression.replace("×", "*").replace("÷", "/")
            result = eval(expr, {"__builtins__": None}, {})
            # 整数结果去掉小数点
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("错误", "除数不能为 0")
            self.expression = ""
            self.display_var.set("0")
        except Exception:
            messagebox.showerror("错误", "表达式无效")
            self.expression = ""
            self.display_var.set("0")


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

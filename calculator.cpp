#include <iostream>
#include <limits>

using namespace std;

int main() {
    cout << "简易计算器" << endl;
    cout << "支持的运算：+ - * /" << endl;
    cout << "输入格式：数字 运算符 数字（如 3 + 5）" << endl;
    cout << "输入 q 退出\n" << endl;

    double a, b;
    char op;

    while (true) {
        cout << "请输入算式：";

        // 检测是否输入 q 退出
        cin >> ws;
        if (cin.peek() == 'q' || cin.peek() == 'Q') {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "已退出，再见！" << endl;
            break;
        }

        if (!(cin >> a >> op >> b)) {
            cout << "输入格式错误，请按 “数字 运算符 数字” 输入，如 3 + 5\n" << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        double result;

        switch (op) {
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            case '/':
                if (b == 0) {
                    cout << "错误：除数不能为 0\n" << endl;
                    continue;
                }
                result = a / b;
                break;
            default:
                cout << "不支持的运算符：" << op << "\n" << endl;
                continue;
        }

        cout << "结果：" << result << "\n" << endl;
    }

    return 0;
}

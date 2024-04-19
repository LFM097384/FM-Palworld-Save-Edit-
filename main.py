import json
import sys
import tkinter as tk
import tkinter.font as tkFont
import paths
from tkinter import filedialog

#修改数值
def edit_value(new_value, json_data, path):
    """
    修改特定路径下的值

    参数：
    new_value: 要设置的新值
    json_data: JSON 数据
    path: 路径列表，用于指定要修改的值的位置

    返回：
    无
    """
    print(f"开始修改{path}的数值为{new_value}")
    #box_write(app.message_box,f"开始修改{path}的数值为{new_value}")
    if(verify_path(json_data, path)==False): 
        print("路径错误")
        return False
    else:
        print("路径:\n",path,"\n是正确的")
    try:
        target = json_data
        for key in path[:-1]:  # 遍历路径中的每个键，但不包括最后一个键，因为最后一个键是要修改的值的键
            if isinstance(target, list):  # 如果当前路径对应的值是列表
                target = target[int(key)]  # 将键转换为整数索引
            else:
                target = target[key]  # 否则，正常访问字典的键
        
        # 确保最后一个键对应的值是一个字典
        if isinstance(target, dict):
            target[path[-1]] = new_value
        else:
            print("错误：最后一个键对应的值不是字典。")
            return False
    except (KeyError, IndexError, ValueError) as e:
        print(f"访问路径或索引时出错：{e}") 
        return False
    print("修改成功!")
    return True

#确认路径
def verify_path(json_data, path):
    """
    判断特定路径是否存在

    参数：
    json_data: JSON 数据
    path: 路径列表，用于指定要修改的值的位置

    返回：
    存在True 不存在False
    """
    target = json_data
    for key in path:
        if isinstance(key, int):  # 如果路径是数字，应当对应列表
            if not isinstance(target, list) or not (0 <= key < len(target)):
                return False
            target = target[key]
        else:  # 如果路径是字符串，应当对应字典
            if not isinstance(target, dict) or key not in target:
                return False
            target = target[key]
    return True

def box_write(widget, content):
        """
        向指定的文本框组件写入内容并换行。

        参数：
        widget: Tkinter Text组件。
        content: 写入的内容。

        返回：
        none
        """
        try:
            widget.config(state='normal')
            widget.insert(tk.END, content + "\n")
            widget.config(state='disabled')
            widget.see(tk.END)  # 将文本框滚动到底部
        except Exception as e:
            print(f"Error writing to box: {e}")

#左右居中
def xcenter_element(element):
    # 获取父容器
    parent = element.master

    # 获取元素的实际大小
    element.update()
    element_width = element.winfo_width()
    element_height = element.winfo_height()

    # 获取父容器的大小
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    # 计算元素的位置
    x = (parent_width - element_width) // 2
    y = (parent_height - element_height) // 2

    # 设置元素的位置
    element.place(x=x)

#上下居中
def ycenter_element(element):
    # 获取父容器
    parent = element.master

    # 获取元素的实际大小
    element.update()
    element_width = element.winfo_width()
    element_height = element.winfo_height()

    # 获取父容器的大小
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    # 计算元素的位置
    x = (parent_width - element_width) // 2
    y = (parent_height - element_height) // 2

    # 设置元素的位置
    element.place(y=y)

#靠近底部
def place_at_bottom(element, distance):
    # 获取父容器
    parent = element.master

    # 获取父容器的高度
    parent_height = parent.winfo_height()

    # 获取元素的高度
    element_height = element.winfo_height()

    # 计算元素的位置
    y = parent_height - element_height  # 在底部

    # 设置元素的位置
    element.place(y=y-distance)

#靠近顶部
def place_at_top(element, distance):
    # 获取元素的父容器
    parent = element.master

    # 计算元素的位置
    y = distance  # 顶部位置

    # 设置元素的位置
    element.place(y=y)

class GUI:
    def __init__(self):
        # 创建窗口
        self.window = tk.Tk()
        self.window.geometry("1920x1080")
        # 设置窗口标题
        self.window.title("FM Palworld Save Edit")

        # 添加其他部件和布局
        self.add_widgets()
        self.temp()

        # 运行主事件循环
        self.window.mainloop()
    
    def add_widgets(self):
        # 在这里添加其他部件和布局
        label = tk.Label(self.window, text="Welcome to FM Palworld Save Edit")
        label.pack()
        self.message_box = tk.Text(self.window, height=8, width=120)
        # 添加文本框
        self.message_box.pack(expand=True, fill=tk.BOTH)
        self.message_box.place(width=660,height=150)
        xcenter_element(self.message_box)
        place_at_bottom(self.message_box,100)

        button = tk.Button(self.window, text="Select File", command=self.select_file)
        #button.place(x=960,y=800,width=480,height=250)
        button.pack()

    def select_file(self):
        # 打开文件对话框
        filepath = filedialog.askopenfilename()
        return filepath
    def temp(self):
        print("check")

# 加载JSON数据
filepath = r'C:\Users\刘丰铭\AppData\Local\Pal\辅助工具\palworld-save-tools-windows-v0.22.0\Level.sav.json'

# 将更新后的JSON数据写回文件
def write(local_save, filepath):
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(local_save, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing JSON data back to file: {e}")
    print("保存成功")

def read(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        local_save = json.load(file)
    return local_save

Palsave = read(filepath)

#edit_value("Fruit_attack_01",Palsave,paths.Storage_hero(1))
#edit_value("Accessory_HeatColdResist_3",Palsave,paths.Storage_hero(40))
#edit_value(1,Palsave,paths.amount(paths.Storage_hero(40)))
edit_value(1000000000000,Palsave,paths.WorldTime)

write(Palsave,filepath)
    
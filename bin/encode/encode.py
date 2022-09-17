# All rights Reserved, Designed By www.xysama.cn
# @projectName huffman en-decoding
# @title     huffman encode   
# @author ky0ha     
# @date   2021.05.29  
# @version V1.0.0
# @copyright www.xysama.cn
# 注意 本内容仅限于学习交流使用，禁止用作商业用途

from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog, dialog
import os, pickle, tkinter.messagebox
from tkinter.simpledialog import askstring

class huffman:
    times = 0
    class node:
        def __init__(self, value='', weight=0):
            super().__init__()
            self.value = value
            self.weight = weight
            self.lchild = None
            self.rchild = None
    
        def add_lchild(self, child):
            self.lchild = child
    
        def add_rchild(self, child):
            self.rchild = child

    def __init__(self, parent, string):
        self.parent = parent
        self.string = string
        self.decode = {}
        self.root = self.create_huffman_tree(self.string)
        self.get_decode(self.root)
        self.binary_data = ''.join(i for i in map(lambda x : str(self.decode[x]), string))
        self.code_len = len(self.binary_data)
        # self.save()


    def print_tree(self, root, times=times):
        #self.parent.result_data_Text.delete(1.0,END)
        self.parent.result_data_Text.insert(END,"{}|---- {} {}\n".format("|    "*times, root.weight, root.value))
        if root.lchild==None and root.rchild==None:
            return
        self.print_tree(root.lchild, times+1)
        self.print_tree(root.rchild, times+1)

    def create_huffman_tree(self, string):
        self.weight_dict = {}
        for value in string:
            self.weight_dict[value] = self.weight_dict.setdefault(value, 0) + 1
        print(self.weight_dict)
    
        node_list = []
        len_list = len(node_list)
        for key, value in self.weight_dict.items():
            node_list.append(self.node(key, value))
            len_list+=1
        node_list.sort(key=lambda x:(x.weight, -len(x.value), x.value))
    
        while len_list>1:
            root = self.node()
            root.add_lchild(node_list.pop(0))
            root.add_rchild(node_list.pop(0))
            root.weight = root.lchild.weight + root.rchild.weight
            for index, value in enumerate(node_list):
                if root.weight < value.weight:
                    node_list.insert(index, root)
                    self.print_tree(root)
                    # print('insert!')
                    self.print_tree(root)
            else:
                node_list.append(root)
                self.print_tree(root)
                # print('addend!')
            len_list-=1
    
        root = node_list.pop(0)
        if node_list==[]:
            del node_list, len_list
        else:
            print("Warning: something wrong in creating huffman tree! And the node_list not empty when finish creating!")
    
        return root

    def get_decode(self, root, way=''):       # 函数参数 root 和 way 中，如果 way 参数没有传入，则默认为''空字符
        # 递归遍历整个树
        if root.lchild==None and root.rchild==None:     # 传入的 root 结点没有任何子节点的时候，证明取到了值
            if root.value!=None and way!='':        # 避免端点结点值为空的意外
                self.decode[root.value] = way        # 将值和路径组成键值对，加入到 decode 字典内
            else:
                print("Something wrong! And the root.value is {}, root.weight is {}, way is {}, when error appear!".format(root.value, root.weight, way))
            return
        
        self.get_decode(root.lchild, way+'0')        # 向左遍历为0
        self.get_decode(root.rchild, way+'1')        # 向右遍历为1

    def save(self, file_path):
        def to_bit(s):
            return eval('0b1'+s)

        save_file = {
            'binary_data': to_bit(self.binary_data),
            'code_len':int(self.code_len),
            'decode': dict(zip(self.decode.keys(), list(map(to_bit, self.decode.values())))),
        }
        # save_file = {
        #     'binary_data': to_bit(self.binary_data),
        #     'code_len':int(self.code_len),
        #     'decode': self.decode,
        # }
        print(save_file['binary_data'])
        print(save_file['code_len'])
        print(save_file['decode'])
        with open(file_path+'.svd', 'ab+') as f:
            pickle.dump(save_file, f)
            f.close()

class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("哈夫曼编码")
        self.init_window_name.geometry('1024x768+20+20')
        #self.__read_config()

        self.init_data_label = Label(self.init_window_name,text="哈夫曼编码",font=tkFont.Font(size=30,weight=tkFont.BOLD))
        self.init_data_label.pack(pady=10)

        self.read_from_input_button = Button(self.init_window_name,bd=3,text="输入待编码内容",font=tkFont.Font(size=20,family="KaiTi"),command=self.read_from_input)
        self.read_from_input_button.pack(side=TOP,anchor=W,padx=70)

        self.result_data_label = Label(self.init_window_name, text="结果：", font=tkFont.Font(size=25, weight=tkFont.BOLD))
        self.result_data_label.pack(side=TOP,anchor=W,padx=5,pady=15)

        

        self.result_data_Text = Text(self.init_window_name,width=60,height=15,font=tkFont.Font(size=20, weight=tkFont.BOLD))
        self.result_data_Text.pack(side=TOP,expand=NO,fill=X)

        
        self.read_from_file_button = Button(self.init_window_name,bd=3,text="读取待编码文件",font=tkFont.Font(size=20,family="KaiTi"),command=self.read_from_file)
        self.read_from_file_button.place(x=736, y=65)
        self.print_tree_button = Button(self.init_window_name,bd=3,text="显示哈夫曼树",font=tkFont.Font(size=20,family="KaiTi"),command=self.display_tree)
        self.print_tree_button.pack(expand=YES,side=LEFT)
        self.print_decode_rule_button = Button(self.init_window_name,bd=3,text="显示编码规则",font=tkFont.Font(size=20,family="KaiTi"),command=self.display_decode_rules)
        self.print_decode_rule_button.pack(expand=YES,side=LEFT)
        self.print_code_len_button = Button(self.init_window_name,bd=3,text="显示编码长度",font=tkFont.Font(size=20,family="KaiTi"),command=self.display_weight)
        self.print_code_len_button.pack(expand=YES,side=LEFT)
        self.save_file_button = Button(self.init_window_name,bd=3,text="保存编码文件",font=tkFont.Font(size=20,family="KaiTi"),command=self.save_file)
        self.save_file_button.pack(expand=YES,side=LEFT)

    def read_from_input(self):
        self.string=askstring("输入待编码内容","输入待编码内容：")
        self.start()

    def read_from_file(self):
        # fpath=filedialog.askopenfilename(title=u'选择文本文件',initialdir=(os.path.expanduser(os.path.abspath(os.path.dirname(__file__)))), filetypes=[("文本文件",".txt")])
        fpath=filedialog.askopenfilename(title=u'选择文本文件',initialdir=("C:\\Users\\25315\\Desktop\\huffman\\resources\\test_file"), filetypes=[("文本文件",".txt")])
        if fpath=="":
            # self.message_error01()
            tkinter.messagebox.showerror("错误！", "未选择文件！")
            return
        with open(fpath,"r",encoding="utf-8") as f:
            self.string = f.read()
            f.close()
            # self.message_showinfo01()
        
        self.start()

    def start(self):
        self.huf=huffman(self, self.string)
        if self.huf.code_len <= 1000:
            self.result_data_Text.delete(1.0, END)
            self.result_data_Text.insert(END,"哈夫曼编码为:\n")
            self.result_data_Text.insert(END,"{}\n".format(self.huf.binary_data))
        else:
            self.result_data_Text.delete(1.0, END)
            self.result_data_Text.insert(END,"编码后内容过长，无法显示。\n")
    
    def display_tree(self):
        # self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(END,"\n********************************************************************\n")
        self.result_data_Text.insert(END,"哈夫曼树为:\n")
        self.result_data_Text.insert(END,".\n")
        self.huf.print_tree(self.huf.root)
    
    def display_decode_rules(self):
        # print(self.huf.decode)
        # self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(END,"\n********************************************************************\n")
        self.result_data_Text.insert(END,"编码规则为:\n")
        self.result_data_Text.insert(END,"{}\n".format(self.huf.decode))

    def display_weight(self):
        # print(self.huf.weight_dict)
        # self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(END,"\n********************************************************************\n")
        self.result_data_Text.insert(END,"编码长度为:\n")
        self.result_data_Text.insert(END,"{}\n".format(self.huf.code_len))
    
    def save_file(self):
        file_path=filedialog.asksaveasfilename(title=u"选择存储位置",filetypes=[("哈夫曼编码文件",".svd")])
        self.huf.save(file_path)
        tkinter.messagebox.showinfo("保存成功！", "保存编码文件成功！")
        
def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

gui_start()
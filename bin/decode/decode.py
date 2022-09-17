# All rights Reserved, Designed By www.xysama.cn
# @projectName huffman en-decoding
# @title     huffman decode   
# @author ky0ha     
# @date   2021.05.29  
# @version V1.0.0
# @copyright www.xysama.cn
# 注意 本内容仅限于学习交流使用，禁止用作商业用途

from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog, dialog, messagebox, ttk
import tkinter.messagebox
import json, os, time, pickle, random
from tkinter.simpledialog import askstring

binary_data, code_len, decode = None, None, None
mark_point = True

class MY_GUI():
    result = ''
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
    
    def set_init_window(self):
        self.init_window_name.title("哈夫曼译码器_v1.0")
        self.init_window_name.geometry('1024x768+100+100')

        self.init_data_label = Label(self.init_window_name, text="哈夫曼译码器", font=tkFont.Font(family='KaiTi', size=30, weight=tkFont.BOLD))
        self.init_data_label.pack()
        self.result_data_label = Label(self.init_window_name, text="解码结果：", font=tkFont.Font(family='KaiTi', size=25, weight=tkFont.BOLD))
        self.result_data_label.pack(side='top', anchor='w', expand='no')
        self.empty_label = Label(self.init_window_name, text='', font=tkFont.Font(size=5))
        self.empty_label.pack(side='top', expand='no')
        
        self.result_data_text = Text(self.init_window_name, font=tkFont.Font(family='KaiTi', size=15), height=33)
        self.result_data_text.pack(side='top', fill='both', expand='no')

        self.choose_file_button = Button(self.init_window_name, text="选择压缩的编码文件", bd=3, font=tkFont.Font(family='KaiTi', size=20), command=self.choose_file)
        self.choose_file_button.place(x=740, y=38)

    def choose_file(self):
        fpath = filedialog.askopenfilename(title=u'选择压缩的编码文件', initialdir=("C:\\Users\\25315\\Desktop\\huffman\\resources\\test_file"), filetypes=[("哈夫曼编码文件",".svd")]) 
        global binary_data, code_len, decode, mark_point

        if fpath=='':
            self.message_error01()
            return 0
        
        # try:
        with open(fpath, "rb") as json_file:        
            temp = pickle.load(json_file)        # 用 json 库的 load 方法读取 json 文件内容，并将其转化为字典类型
            def to_str(s):
                return bin(s)[3:]
            save_file = {
                'binary_data': to_str(temp['binary_data']),
                'code_len':int(temp['code_len']),
                'decode': dict(zip(temp['decode'].keys(), list(map(to_str, temp['decode'].values())))),
            }
            # save_file = {
            #     'binary_data': to_str(temp['binary_data']),
            #     'code_len':int(temp['code_len']),
            #     'decode': temp['decode'],
            # }
            print(save_file['binary_data'])
            print(save_file['code_len'])
            print(save_file['decode'])
            globals().update(save_file)         # 利用字典的 update 方法，将字典 a 内的所以键值对更新到 globals 字典内， globals() 返回全局变量字典
            json_file.close()
            
        decode = dict(zip(decode.values(), decode.keys()))
        code_len = int(code_len)
        # self.message_showinfo()
        # except:
        #     self.message_error02()
        #     return 0

        # try:
        pw = popup_display(self.init_window_name)       #弹窗对象的创建和储存
        # except:
        #     self.message_error03()
        
        try:
            self.result_data_text.delete(1.0, END)
            self.result_data_text.insert(END, "解码完成！\n")
            self.result_data_text.insert(END, '\n')
            if code_len <= 1000:
                self.result_data_text.insert(END, "原编码为：\n")
                self.result_data_text.insert(END, "    {}\n\n".format(binary_data))
            else:
                self.result_data_text.insert(END, "原编码内容过长，无法显示！\n")
            self.result_data_text.insert(END, "解码后的内容为：\n")
            self.result_data_text.insert(END, "    {}\n".format(self.result))
        except:
            self.message_error04()
    
    def message_showinfo(self):
        '''
        成功打开文件
        '''
        top = tkinter.Tk()
        top.withdraw()  # ****实现主窗口隐藏
        top.update()  # *********需要update一下
        tkinter.messagebox.showinfo(title="提示", message="打开文件成功！")
        top.destroy()

    def message_error01(self):
        '''
        打开文件失败
        '''
        top = tkinter.Tk()
        top.withdraw()
        top.update()
        tkinter.messagebox.showerror(title="错误01", message="打开文件失败，请检查文件路径是否正确！错误代码：01")
        top.destroy()

    def message_error02(self):
        '''
        文件格式错误
        '''
        top = tkinter.Tk()
        top.withdraw()
        top.update()
        tkinter.messagebox.showerror(title="错误02", message="发生意外错误，请检查选择的文件是否是.svd文件！错误代码：02")
        top.destroy()

    def message_error03(self):
        '''
        解码时错误
        '''
        top = tkinter.Tk()
        top.withdraw()
        top.update()
        tkinter.messagebox.showerror(title="错误03", message="解码意外停止！！错误代码：03")
        top.destroy

    def message_error04(self):
        '''
        输出时错误
        '''
        top = tkinter.Tk()
        top.withdraw()
        top.update()
        tkinter.messagebox.showerror(title="错误04", message="发生了一个预期之外的错误！错误代码：04")
        top.destroy()

class popup_display(Toplevel):
    '''
    弹窗部分
    通过构造函数继承父类MY_GUI，并在按钮内显性的更新父类的simulate_mode属性
    更新完成后自动关闭弹窗
    '''
    def __init__(self, parent):
        super().__init__()
        self.init_window_name = self
        self.speed = 0
        self.parents = MY_GUI
        self.set_init_window()
        self.start_to_decode()
    
    def set_init_window(self):
        self.init_window_name.title("解码进度")
        self.init_window_name.geometry('800x300+200+200')

        self.message_title_label = Label(self.init_window_name, text="正在解码：", font=tkFont.Font(family='KaiTi', size=30))
        self.message_title_label.pack(expand='yes')
        self.progress_bar = ttk.Progressbar(self.init_window_name, mode='determinate', length=600)
        self.progress_bar['maximum'] = 10000
        self.progress_bar['value'] = 0
        self.progress_bar.pack(expand='yes')

        self.s = StringVar()
        self.s.set("解码进度：{:.2f}%".format(self.speed/100))
        self.speed_label = Label(self.init_window_name, textvariable=self.s, font=tkFont.Font(family='KaiTi', size=20))
        self.speed_label.pack(expand='yes')
    
    def start_to_decode(self):
        global binary_data, code_len, decode, mark_point
        left, right = 0, 1
        self.parents.result = ''
        self.speed = 0
        flag = 3
        count = 0

        while right<=code_len:
            if count%10==0:
                self.speed = right*10000//code_len
            if self.speed%500==0:
                self.progress_bar['value'] = self.speed
                self.init_window_name.update()
            if self.speed%flag==0: 
                self.s.set("解码进度：{:.2f}%".format(self.speed/100))
                flag = random.randint(7,100)
                self.init_window_name.update()
            count+=1
            if binary_data[left:right] in decode:
                self.parents.result+=decode[binary_data[left:right]]
                left = right
                right = left+1
            else:
                right += 1
        else:
            # time.sleep(1)
            self.progress_bar['value'] = 10000
            # self.s.set("解码进度：{:.2f}%".format(self.speed/100))
        time.sleep(1)
        # self.progress_bar['value'] = 10000
        self.init_window_name.destroy()

def gui_start():
        init_window = Tk()
        ZMJ_PORTAL = MY_GUI(init_window)
        ZMJ_PORTAL.set_init_window()
        init_window.mainloop()

gui_start()
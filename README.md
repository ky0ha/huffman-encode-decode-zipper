# All rights Reserved, Designed By www.xysama.cn
# @projectName huffman en-decoding
# @author ky0ha     
# @date   2021.05.29  
# @version V1.0.0
# @copyright www.xysama.cn
# 注意 本内容仅限于学习交流使用，禁止用作商业用途

哈夫曼编码程序文件

./decode 和 ./encode 为本体程序的编码端和解码端的快捷方式，其中 decode 为编码端，encode 为解码端

程序使用 python 语言实现，gui 的实现使用 python 的 tkinter 库
程序使用的库有：tkinter，json，os，time，random，pickle
由于exe未经过真正意义的打包，故必须在拥有上述库以及 python 3.x 运行环境下使用

压缩后的 *.svd 文件为自定义文件格式 save data file，本质为 *.json 文件，
文件的格式为
{
    "binary_data": "11111110110111010101100000011",
    "code_len": "29",
    "decode": {
        "E": "00",
        "C": "01",
        "D": "100",
        "B": "101",
        "A": "11"
    }
}
其中 "binary_data" 和 "decode" 内的 01 数据由 python 更改为二进制数据，并直接存储于 *.json 文件内，
当解码的时候再根据二进制数据翻译为字符串，进行解码

注意：程序并未使用 python 的 pyinstaller 进行打包，所以文件内的各个部分理论上可以随意移动且不受影响，但是最好不要随意改动，
因为程序代码并没有进行十分完善的 debug 环节和 bug 捕获。
如果程序出现不知名的 bug 导致无法正常运行，请尝试重新解压。如果问题依旧存在，请联系制作者。
`# All rights Reserved, Designed By www.xysama.cn`
`# @projectName huffman en-decoding`
`# @author ky0ha     `
`# @date   2021.05.29  `
`# @version V1.0.0`
`# @copyright www.xysama.cn`
`# 注意 本内容仅限于学习交流使用，禁止用作商业用途`

哈夫曼编码程序文件
huffman encoding program source

./decode 和 ./encode 为本体程序的编码端和解码端的快捷方式，其中 decode 为编码端，encode 为解码端
`./decode.ink` and `./encode.ink` is the ink for encoder and decoder

程序使用 python 语言实现，gui 的实现使用 python 的 tkinter 库
程序使用的库有：tkinter，json，os，time，random，pickle
由于exe未经过真正意义的打包，故必须在拥有上述库以及 python 3.x 运行环境下使用
Program base on python and the gui is built by tkinter module.
So, the module has been used in this project is : tkinter, json, os, time, random, pickle.
Because the .exe file is not the truly .exe, it just be made by zipper, so what i mean is that .exe is just a specially .zip file. As that reason, the project must running in python3.x env.

压缩后的 *.svd 文件为自定义文件格式 saved data file，本质为 *.json 文件，
The file be zipped by huffman encoder is *.svd file, the name means 'saved data file'. The file is essentially a json file.
文件的格式为
The content of that json file is:
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
The 01 data in 'binary_data' and 'decode' is changed from Python to binary data and stored directly in the *. JSON file,

当解码的时候再根据二进制数据翻译为字符串，进行解码
It will translate by binary data when decode to string.

注意：程序并未使用 python 的 pyinstaller 进行打包，所以文件内的各个部分理论上可以随意移动且不受影响，但是最好不要随意改动，
因为程序代码并没有进行十分完善的 debug 环节和 bug 捕获。
如果程序出现不知名的 bug 导致无法正常运行，请尝试重新解压。如果问题依旧存在，请联系制作者。
Note: The program is not packaged using Python's pyinstaller, so theoretically, various parts of the file can be moved freely and unaffected, but it is best not to make arbitrary changes,
Because the program code has not undergone a very comprehensive debugging process and bug capture.
If the program encounters an unknown bug that prevents it from running properly, please try decompressing it again. If the problem persists, please contact the producer.

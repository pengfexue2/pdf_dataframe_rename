#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-10-24 21:39

__author__ = 'Ted'

import tabula
import re
import os


# 将提取单一 PDF 文件内批号数据的过程定义成 get_target("pdf名称") 函数，最终函数将数据返回
def get_target(filename):
    df = tabula.read_pdf(filename)
    pattern = r'[A-Z0-9]+[\s]*[A-Z0-9]*'

    for item_sub in df[df.columns[1]]:
        if "批号" in str(item_sub):
            result = re.search(pattern,item_sub).group()
            return result
    return False


if __name__=="__main__":
    # 获取 PDF 所在文件夹
    folder = "test"
    # os 模块定位到该文件夹
    os.chdir(folder)
    # 获取文件夹内文件列表
    pdflist = os.listdir()
    # 打印该文件列表
    print(pdflist)

    # 对文件列表 for 循环处理
    for item in pdflist:
        # 如果该文件名称最后四位是 .pdf 或 .PDF,即我们要找的 PDF 文件
        if item[-4:] in [".pdf",".PDF"] :
            # 对该文件进行提取批号函数操作，将批号数据赋值给 new_name
            new_name = get_target(item)
            # 如果不为空，即获取到了批号数据
            if new_name:
                # 对文件进行重命名操作
                os.rename(item,f"{new_name}.pdf")
    print("重命名成功！")


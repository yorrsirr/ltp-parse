# -*- coding:utf-8 -*-
from Tkinter import *
import parser_ltp
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

root = Tk()
root.title('快想个组名')
root.geometry('480x420')

Label(root, text='统计句法分析实验').pack()

insert_text = Text(root, height=10)
insert_text.pack()

button_fram = Frame(root, height=5)

##MM_button
seg_text = ''
on_hit = False  # 默认初始状态为 False

def par_hit_me():
    row_text = insert_text.get("0.0", "end")
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        output_text_seg.insert('insert', "\t".join(parser_ltp.seg(str(row_text))))
        output_text_pos.insert('insert', "\t".join(parser_ltp.pos(str(row_text))))
        output_text_par.insert('insert', "\t".join("%d:%s" % (arc.head, arc.relation) for arc in parser_ltp.par(str(row_text))))
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        output_text_seg.insert('end','') # 设置 文字为空
        output_text_pos.insert('end', '')  # 设置 文字为空
        output_text_par.insert('end', '')  # 设置 文字为空

##FMM_button
Button(button_fram, text='seg+pos+par', command=par_hit_me).pack(side=LEFT)
button_fram.pack()

Label(root, text='Results of Seg:').pack()
output_text_seg = Text(root, height=3)
output_text_seg.pack()

Label(root, text='Results of Pos:').pack()
output_text_pos = Text(root, height=3)
output_text_pos.pack()

Label(root, text='Results of Par:').pack()
output_text_par = Text(root, height=3)
output_text_par.pack()


root.mainloop()

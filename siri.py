#-*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.messagebox as tkm
import pya3rt

apikey = "DZZWyhnSmLVGmguL7ZtFnRtimf4D7OQM"
client = pya3rt.TalkClient(apikey)

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'Sori')

# ここでウインドウサイズを定義する
root.geometry('500x500')
# ボタンが押されたらリストボックスに、Entryの中身を追加
def addList(text):
    mysay = 'あなた: ' + text
    print(mysay)
    ListBox1.insert(tk.END, mysay)
    Seri = 'Sori: ' + talk(text)
    Entry1.delete(0, tk.END)
    addRep(Seri)

def addRep(Seri):
    ListBox1.insert(tk.END, Seri)

def talk(say):
    if say == 'end':
        return('んじゃ')
    else:
        ans_json = client.talk(say)
        ans = ans_json['results'][0]['reply']
        return(ans)

# ラベルを使って文字を画面上に出す
Static1 = tk.Label(text=u'▼　Soriに文章を送りましょう!　▼')
Static1.pack()


# Entryを出現させる
Entry1 = tk.Entry(width=50)                   # widthプロパティで大きさを変える
Entry1.insert(tk.END, u'こんにちは')        # 最初から文字を入れておく
Entry1.pack()


# Buttonを設置してみる
Button1 = tk.Button(text=u'送信', width=50, command=lambda: addList(Entry1.get()))        # 関数に引数を渡す場合は、commandオプションとlambda式を使う
Button1.pack()


# リストボックスを設置してみる
ListBox1 = tk.Listbox(width=80, height=60,bg='pink')
ListBox1.pack()

root.mainloop()
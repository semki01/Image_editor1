import os
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5 import Qt

app = QApplication([])
win = QWidget()
win.setWindowTitle('Image Editor Pro')
win.resize(700, 500)

lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_bw = QPushButton('Ч/Б')
btn_sharp = QPushButton('Резкость')
btn_mirror = QPushButton('Зеркало')
lw_files = QListWidget()


row = QHBoxLayout()
main_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

col_1.addWidget(btn_dir)
col_1.addWidget(lw_files)
row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_bw)
row.addWidget(btn_sharp)
row.addWidget(btn_mirror)

col_2.addWidget(lb_image)
col_2.addLayout(row)
main_layout.addLayout(col_1, 2)
main_layout.addLayout(col_2, 8)

work_dir = ''

def choose_work_dir():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result

def show_file_name_list():
    choose_work_dir()
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    filenames = filter(os.listdir(work_dir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(show_file_name_list)        

win.setLayout(main_layout)
win.show()
app.exec_()

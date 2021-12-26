import os
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image



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

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
    
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

workimage = ImageProcessor()

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(work_dir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
win.setLayout(main_layout)
win.show()
app.exec_()

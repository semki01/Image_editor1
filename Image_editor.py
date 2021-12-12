from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('mops-mops-457.jpg') as pic_original:
    print('Изображение открыто\nРазмер:',pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()

    #Делаем картинку серую
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print('Изображение открыто\nРазмер:',pic_gray.size)
    print('Формат:', pic_gray.format)
    print('Тип:', pic_gray.mode)
    pic_gray.show()

    #Делаем картинку размытой
    pic_blured = pic_original.convert('L')
    pic_blured.save('blured.jpg')
    print('Изображение открыто\nРазмер:',pic_blured.size)
    print('Формат:', pic_blured.format)
    print('Тип:', pic_blured.mode)
    pic_blured.show()

    #Зеркальное отражение
    pic_mirror = pic_original.convert('L')
    pic_mirror.save('mirror.jpg')
    print('Изображение открыто\nРазмер:',pic_mirror.size)
    print('Формат:', pic_mirror.format)
    print('Тип:', pic_mirror.mode)
    pic_mirror.show()
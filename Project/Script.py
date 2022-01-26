import docx
import io
import re

C16 = open('SRC/C16.txt', 'w', encoding='ANSI')

K16 = docx.Document('SRC/к16.docx')
all_paras = K16.paragraphs
for para in all_paras:
    C16.write(para.text + '\n')
C16.close()



monday = open('result/Понедельник.txt', 'w', encoding='UTF-16')
tuesday = open('result/Вторник.txt', 'w', encoding='UTF-16')
wednesday = open('result/Среда.txt', 'w', encoding='UTF-16')
thusday = open('result/Четверг.txt', 'w', encoding='UTF-16')
friday = open('result/Пятница.txt', 'w', encoding='UTF-16')
saturday = open('result/Суббота.txt', 'w', encoding='UTF-16')
sunday = open('result/Воскресенье.txt', 'w', encoding='UTF-16')

mon = u'Понедельник'
tue = u'Вторник'
wed = u'Среда,'
thu = u'Четверг'
fri = u'Пятница'
sat = u'Суббота'
sun = u'Воскресенье'

with open('SRC/(R)1TV.txt', 'r+') as f1:
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)1TV.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)1TV.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)


##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)1TV.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)1TV.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)1TV.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)1TV.txt', 'r+', encoding='ANSI') as TV1:    ##Функция распределения программы Первого канала
    monday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    tuesday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    wednesday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    thusday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    friday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    saturday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    sunday.write('<UNICODE-WIN> \n<pstyle:Программа канал>Первый \n<pstyle:Программа текст>')
    
    for line in TV1:
        
        line.translate('@[]')
        
        if mon in line:                                         ##Понедельник
            for line in TV1:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
            
                
        if tue in line:                                         ##Вторник
            for line in TV1:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in TV1:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in TV1:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in TV1:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in TV1:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in TV1:
                sunday.write(line)


##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)RTR.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)RTR.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)RTR.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)RTR.txt', 'r', encoding='ANSI') as RTR:    ##Функция распределения программы канала Россия
    monday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Россия \n<pstyle:Программа текст>')
    
    for line in RTR:
        
        if mon in line:                                         ##Понедельник
            for line in RTR:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in RTR:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in RTR:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in RTR:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in RTR:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in RTR:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in RTR:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)NTV.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)NTV.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)NTV.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)NTV.txt', 'r', encoding='ANSI') as NTV:    ##Функция распределения программы канала НТВ
    monday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>НТВ \n<pstyle:Программа текст>')
    
    for line in NTV:
        
        if mon in line:                                         ##Понедельник
            for line in NTV:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in NTV:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in NTV:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in NTV:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in NTV:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in NTV:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in NTV:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/C16.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/C16.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/C16.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/C16.txt', 'r', encoding='ANSI') as CH16:    ##Функция распределения программы канала К16
    monday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>К16 \n<pstyle:Программа текст>')
    
    for line in CH16:
        
        if mon in line:                                         ##Понедельник
            for line in CH16:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in CH16:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in CH16:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in CH16:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in CH16:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in CH16:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in CH16:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)Piter5_RUS.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)Piter5_RUS.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)Piter5_RUS.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)Piter5_RUS.txt', 'r', encoding='ANSI') as Piter5:    ##Функция распределения программы канала Пятый
    monday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Пятый \n<pstyle:Программа текст>')
    
    for line in Piter5:
        
        if mon in line:                                         ##Понедельник
            for line in Piter5:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Piter5:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Piter5:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Piter5:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Piter5:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Piter5:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Piter5:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)KUL.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)KUL.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)KUL.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)KUL.txt', 'r', encoding='ANSI') as CUL:    ##Функция распределения программы канала Культура
    monday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Культура \n<pstyle:Программа текст>')
    
    for line in CUL:
        
        if mon in line:                                         ##Понедельник
            for line in CUL:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in CUL:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in CUL:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in CUL:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in CUL:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in CUL:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in CUL:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)MatchTV.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)MatchTV.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)MatchTV.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)MatchTV.txt', 'r', encoding='ANSI') as Match:    ##Функция распределения программы канала Матч ТВ
    monday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Матч ТВ \n<pstyle:Программа текст>')
    
    for line in Match:
        
        if mon in line:                                         ##Понедельник
            for line in Match:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Match:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Match:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Match:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Match:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Match:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Match:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)ntv+13.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)ntv+13.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)ntv+13.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)ntv+13.txt', 'r', encoding='ANSI') as Euro:    ##Функция распределения программы канала Евроспорт
    monday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Евроспорт \n<pstyle:Программа текст>')
    
    for line in Euro:
        
        if mon in line:                                         ##Понедельник
            for line in Euro:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Euro:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Euro:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Euro:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Euro:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Euro:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Euro:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)Euro-2.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)Euro-2.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)Euro-2.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)Euro-2.txt', 'r', encoding='ANSI') as Euro2:    ##Функция распределения программы канала Евроспорт 2
    monday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Евроспорт 2 \n<pstyle:Программа текст>')
    
    for line in Euro2:
        
        if mon in line:                                         ##Понедельник
            for line in Euro2:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Euro2:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Euro2:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Euro2:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Euro2:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Euro2:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Euro2:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)RenTV.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)RenTV.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)RenTV.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)RenTV.txt', 'r', encoding='ANSI') as Ren:    ##Функция распределения программы канала Рен-ТВ
    monday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Рен-ТВ \n<pstyle:Программа текст>')
    
    for line in Ren:
        
        if mon in line:                                         ##Понедельник
            for line in Ren:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Ren:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Ren:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Ren:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Ren:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Ren:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Ren:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)MIR.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)MIR.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)MIR.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)MIR.txt', 'r', encoding='ANSI') as Mir:    ##Функция распределения программы канала Мир
    monday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Мир \n<pstyle:Программа текст>')
    
    for line in Mir:
        
        if mon in line:                                         ##Понедельник
            for line in Mir:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Mir:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Mir:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Mir:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Mir:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Mir:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Mir:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)MIR.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)MIR.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)MIR.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)TVC.txt', 'r', encoding='ANSI') as Tvc:    ##Функция распределения программы канала ТВЦ
    monday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ТВЦ \n<pstyle:Программа текст>')
    
    for line in Tvc:
        
        if mon in line:                                         ##Понедельник
            for line in Tvc:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Tvc:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Tvc:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Tvc:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Tvc:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Tvc:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Tvc:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)DOMASHNIY.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)DOMASHNIY.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)DOMASHNIY.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)DOMASHNIY.txt', 'r', encoding='ANSI') as Dom:    ##Функция распределения программы канала Домашний
    monday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Домашний \n<pstyle:Программа текст>')
    
    for line in Dom:
        
        if mon in line:                                         ##Понедельник
            for line in Dom:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Dom:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Dom:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Dom:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Dom:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Dom:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Dom:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)ZVEZDA.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)ZVEZDA.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)ZVEZDA.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)ZVEZDA.txt', 'r', encoding='ANSI') as Star:    ##Функция распределения программы канала Звезда
    monday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Звезда \n<pstyle:Программа текст>')
    
    for line in Star:
        
        if mon in line:                                         ##Понедельник
            for line in Star:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Star:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Star:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Star:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Star:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Star:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Star:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)Che.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)Che.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)Che.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)Che.txt', 'r', encoding='ANSI') as Che:    ##Функция распределения программы канала ЧЕ!
    monday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ЧЕ! \n<pstyle:Программа текст>')
    
    for line in Che:
        
        if mon in line:                                         ##Понедельник
            for line in Che:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Che:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Che:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Che:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Che:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Che:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Che:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)TV3.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)TV3.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)TV3.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)TV3.txt', 'r', encoding='ANSI') as Tv3:    ##Функция распределения программы канала ТВ3
    monday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ТВ3 \n<pstyle:Программа текст>')
    
    for line in Tv3:
        
        if mon in line:                                         ##Понедельник
            for line in Tv3:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Tv3:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Tv3:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Tv3:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Tv3:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Tv3:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Tv3:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)STS.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)STS.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)STS.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)STS.txt', 'r', encoding='ANSI') as Sts:    ##Функция распределения программы канала СТС
    monday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>СТС \n<pstyle:Программа текст>')
    
    for line in Sts:
        
        if mon in line:                                         ##Понедельник
            for line in Sts:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Sts:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Sts:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Sts:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Sts:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Sts:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Sts:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)TNT.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)TNT.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)TNT.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)TNT.txt', 'r', encoding='ANSI') as Tnt:    ##Функция распределения программы канала ТНТ
    monday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ТНТ \n<pstyle:Программа текст>')
    
    for line in Tnt:
        
        if mon in line:                                         ##Понедельник
            for line in Tnt:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Tnt:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Tnt:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Tnt:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Tnt:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Tnt:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Tnt:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)OTR.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)OTR.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)OTR.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)OTR.txt', 'r', encoding='ANSI') as Otr:    ##Функция распределения программы канала ОТР
    monday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ОТР \n<pstyle:Программа текст>')
    
    for line in Otr:
        
        if mon in line:                                         ##Понедельник
            for line in Otr:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Otr:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Otr:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Otr:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Otr:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Otr:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Otr:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)Histor.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)Histor.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)Histor.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)Histor.txt', 'r', encoding='ANSI') as History:    ##Функция распределения программы канала History
    monday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>History \n<pstyle:Программа текст>')
    
    for line in History:
        
        if mon in line:                                         ##Понедельник
            for line in History:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in History:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in History:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in History:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in History:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in History:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in History:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)RU_ILLusio.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)RU_ILLusio.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)RU_ILLusio.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)RU_ILLusio.txt', 'r', encoding='ANSI') as Rui:    ##Функция распределения программы канала Русский иллюзион
    monday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Русский иллюзион \n<pstyle:Программа текст>')
    
    for line in Rui:
        
        if mon in line:                                         ##Понедельник
            for line in Rui:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Rui:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Rui:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Rui:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Rui:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Rui:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Rui:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)ILLUSION+.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)ILLUSION+.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)ILLUSION+.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)ILLUSION+.txt', 'r', encoding='ANSI') as Illu:    ##Функция распределения программы канала Иллюзион +
    monday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>Иллюзион + \n<pstyle:Программа текст>')
    
    for line in Illu:
        
        if mon in line:                                         ##Понедельник
            for line in Illu:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Illu:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Illu:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Illu:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Illu:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Illu:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Illu:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)NNTV_NN.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)NNTV_NN.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)NNTV_NN.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)NNTV_NN.txt', 'r', encoding='ANSI') as Nntv:    ##Функция распределения программы канала ННТВ - Нижний Новгород
    monday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ННТВ - Нижний Новгород \n<pstyle:Программа текст>')
    
    for line in Nntv:
        
        if mon in line:                                         ##Понедельник
            for line in Nntv:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Nntv:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Nntv:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Nntv:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Nntv:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Nntv:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Nntv:
                sunday.write(line)

##==============================================================================================================
##==============================================================================================================
with open('SRC/(R)Volga_NN.txt', 'r+') as f1:                        ##Убираем символы []@
    txt1 = f1.read().replace('[', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt1)

with open('SRC/(R)Volga_NN.txt', 'r+') as f1:
    txt2 = f1.read().replace(']', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt2)

with open('SRC/(R)Volga_NN.txt', 'r+') as f1:
    txt3 = f1.read().replace('@', '')
    f1.seek(0)
    f1.truncate()
    f1.write(txt3)



with io.open('SRC/(R)Volga_NN.txt', 'r', encoding='ANSI') as Volga:    ##Функция распределения программы канала ВОЛГА
    monday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    tuesday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    wednesday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    thusday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    friday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    saturday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    sunday.write('<pstyle:Программа канал>ВОЛГА \n<pstyle:Программа текст>')
    
    for line in Volga:
        
        if mon in line:                                         ##Понедельник
            for line in Volga:
                if tue not in line:
                    monday.write(line)
                else:
                    monday.write('\n')
                    break
                
        if tue in line:                                         ##Вторник
            for line in Volga:
                if wed not in line:
                    tuesday.write(line)
                else:
                    tuesday.write('\n')
                    break

        if wed in line:                                         ##Среда
            for line in Volga:
                if thu not in line:
                    wednesday.write(line)
                else:
                    wednesday.write('\n')
                    break

        if thu in line:                                         ##Четверг
            for line in Volga:
                if fri not in line:
                    thusday.write(line)
                else:
                    thusday.write('\n')
                    break

        if fri in line:                                         ##Пятница
            for line in Volga:
                if sat not in line:
                    friday.write(line)
                else:
                    friday.write('\n')
                    break

        if sat in line:                                         ##Суббота
            for line in Volga:
                if sun not in line:
                    saturday.write(line)
                else:
                    saturday.write('\n')
                    break

        if sun in line:                                         ##Воскресенье
            for line in Volga:
                sunday.write(line)





monday.close()
tuesday.close()
wednesday.close()
thusday.close()
friday.close()
saturday.close()
sunday.close()


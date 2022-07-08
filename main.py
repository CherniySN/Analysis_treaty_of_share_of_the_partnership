import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTextEdit
from PyQt5.QtCore import QThread
import docx2txt
import re


class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.doc = ''
        self.set()


    def open(self): # открываем файловый диалог
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0] # читаем путь до выбранного файла
        if fname:
            self.doc = docx2txt.process(fname) # читаем весь документ получаем огромную строку
            self.w_root.treatyText.setPlainText(self.doc)


    def clear(self):
        self.w_root.treatyText.clear()
        self.w_root.coomon_square.setText('Общая площадь обекта:')
        self.w_root.costumer.setText('Участники ДДУ:')
        self.w_root.deposit_amount.setText('Депонирумая сумма:')
        self.w_root.downpayment_amount.setText('Сумма первоначального взноса:')
        self.w_root.flore.setText('Этаж:')
        self.w_root.number_of_flat.setText('Номер квартиры:')
        self.w_root.numbers_of_flores.setText('Количество этажей:')
        self.w_root.price.setText('Цена обьекта недвижимости:')
        self.w_root.value_of_mortgage.setText('Сумма кредита:')
        self.w_root.value_of_rooms.setText('Количество комнат:')
        self.w_root.adress.setText('Адрес обьекта:')
        self.w_root.id.setText('Паспортные данные:')


    def set(self):
        self.w_root = uic.loadUi('Analysis_treaty_of_share_of_the_partnership.ui')
        self.w_root.openButton.clicked.connect(self.open) # событие нажатие на кнопку
        self.w_root.Clear.clicked.connect(self.clear) # очищаем поле
        self.w_root.RunRe.clicked.connect(self.run)  # событие нажатие на кнопку
        self.w_root.treatyText.clear()
        self.w_root.coomon_square
        self.w_root.costumer
        self.w_root.deposit_amount
        self.w_root.downpayment_amount
        self.w_root.flore
        self.w_root.number_of_flat
        self.w_root.numbers_of_flores
        self.w_root.price
        self.w_root.value_of_mortgage
        self.w_root.value_of_rooms
        self.w_root.adress
        self.w_root.id

        self.w_root.show()

    def run(self):
        reg_expr = r'\w+'  # текст разбиваем на токены
        reg_expr_compiled = re.compile(reg_expr)
        res = reg_expr_compiled.findall(self.doc)
        print(res)

        reg_expr_name = r'РФ ([А-Я]\w+ [А-Я]\w+ [А-Я]\w+)'  # регулярка
        reg_expr_compiled = re.compile(reg_expr_name)
        for g in reg_expr_compiled.findall(self.doc): # ищем ФИО по регулярке
            print(g)
            self.w_root.costumer.setText('Участники ДДУ: %s' % str(g)) # Выводим найденное слово

        reg_expr_id = r'пол: жен.,(.+?)именуемые'
        reg_expr_compiled = re.compile(reg_expr_id)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.id.setText('Паспортные данные: %s' % str(g))
            self.w_root.id.setWordWrap(True)


        reg_expr_price = r'и составляет сумму в размере(.+?)[(]Два'
        reg_expr_compiled = re.compile(reg_expr_price)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.price.setText('Цена обьекта недвижимости: %s' % str(g))

        reg_expr_downpayment_amount = r'-(.+?)[(]Ч'
        reg_expr_compiled = re.compile(reg_expr_downpayment_amount)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.downpayment_amount.setText('Сумма первоначального взноса: %s' % str(g))

        reg_expr_value_of_mortgage = r'-(.+?)[(]Два'
        reg_expr_compiled = re.compile(reg_expr_value_of_mortgage)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.value_of_mortgage.setText('Сумма кредита: %s' % str(g))

        reg_expr_deposit_amount = r'Депонируемая сумма:(.+?)[(]Два'
        reg_expr_compiled = re.compile(reg_expr_deposit_amount)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.deposit_amount.setText('Депонирумая сумма: %s' % str(g))

        reg_expr_numbers_of_flores = r'в Объекте: (.+?)'
        reg_expr_compiled = re.compile(reg_expr_numbers_of_flores)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.numbers_of_flores.setText('Количество этажей: %s' % str(g))

        reg_expr_coomon_square = r'Площадь Объекта долевого строительства, кв м[\n][\n](.+?)[\n]'
        reg_expr_compiled = re.compile(reg_expr_coomon_square)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.coomon_square.setText('Общая площадь обекта: %s' % str(g))

        reg_expr_flore = r'Этаж[\n][\n](.+?)[\n]'
        reg_expr_compiled = re.compile(reg_expr_flore)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.flore.setText('Этаж: %s' % str(g))

        reg_expr_number_of_flat = r'номер[)][\n][\n](.+?)[\n]'
        reg_expr_compiled = re.compile(reg_expr_number_of_flat)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.number_of_flat.setText('Номер квартиры: %s' % str(g))

        reg_expr_value_of_rooms = r'Количество комнат[\n][\n](.+?)[\n]'
        reg_expr_compiled = re.compile(reg_expr_value_of_rooms)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.value_of_rooms.setText('Количество комнат: %s' % str(g))

        reg_expr_adress = r'Объект – (.+?)\n'
        reg_expr_compiled = re.compile(reg_expr_adress)
        for g in reg_expr_compiled.findall(self.doc):
            print(g)
            self.w_root.adress.setText('Адрес обьекта: %s' % str(g))
            self.w_root.adress.setWordWrap(True)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()

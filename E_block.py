from tkinter import *
from tkinter.ttk import Notebook, Frame
from tkinter import ttk, messagebox
import urllib.request
import xml.dom.minidom
from datetime import datetime, timedelta
import matplotlib
from calendar import monthrange
import matplotlib.pyplot as plt


today = datetime.now().strftime("%d/%m/%Y")
response = urllib.request.urlopen("https://cbr.ru/scripts/XML_daily.asp?date_req="+today) #url запрос

####################### Парсинг XML для получения актуальных данных ###################
dom = xml.dom.minidom.parse(response)
dom.normalize()
nodeArray = dom.getElementsByTagName("Valute")

nameList, nominalList, valueList = [], [], []

def get_node_info(tag,nodeArray):
    reslist = []
    for node in nodeArray:
        array = node.getElementsByTagName(tag)
        for item in array:
            list = item.childNodes
            for item in list:
                reslist.append(item.nodeValue)
    return reslist


nameList = get_node_info("Name", nodeArray) # список названий
nominalList = get_node_info("Nominal", nodeArray) # список номиналов
valueList = get_node_info("Value", nodeArray) # список значений
nameList.append("Рубль")
nominalList.append('1')
valueList.append('1')

for i in range(0,len(nominalList)):
    valueList[i] = float(valueList[i].replace(',','.')) / float(nominalList[i].replace(',','.')) # приведенные значения

valuteDict = {} # словарь название - стоимость в рублях
for i in range(0,len(nameList)):
    valuteDict[nameList[i]] = valueList[i]
nameList.sort()
##########################################

window = Tk()
window.title("Конвертер валют")

tabs = Notebook(window)
tab1 = Frame(tabs)
tab2 = Frame(tabs)
tabs.add(tab1, text="Калькулятор валют")
tabs.add(tab2, text = "Динамика курса")
tabs.pack(expand = True, fill = BOTH)

def window_size(*args):
    if(tabs.index(tabs.select())==0):
        window.geometry("600x160")
    else:
        window.geometry("600x160")
tabs.bind("<<NotebookTabChanged>>", window_size)

####################### Вкладка 1 ###################
combobox1 = ttk.Combobox(tab1)
combobox1["values"] = nameList
combobox1.current(0)
combobox1.grid(row = 0, column = 0, padx=15, pady=15, ipadx=65)

combobox2 = ttk.Combobox(tab1)
combobox2["values"] = nameList
combobox2.current(0)
combobox2.grid(row = 1, column = 0, pady=20, ipadx=65)

entry = Entry(tab1)
entry.grid(row=0, column=2, padx=10, pady=15)

label1 = Label(tab1)
label1.grid(row=1, column=2)

#Кнопка
def btn_click():
    window.geometry("600x160")
    if not (entry.get().isdigit()):
        messagebox.showerror(title="Ошибка", message="Некорректный ввод")
    else:
        res = int(entry.get()) * (valuteDict.get(combobox1.get()) / valuteDict.get(combobox2.get()))
        label1.configure(text=res)


btn = Button(tab1, text='Конвертировать', command = btn_click)
btn.grid(row=0, column=3,padx=15)
###############

####################### Вкладка 2 ###################
label2 = Label(tab2, text="Валюта", justify=CENTER)
label2.grid(row=0, column=0)
combobox3 = ttk.Combobox(tab2)
combobox3["values"] = nameList
combobox3.current(0)
combobox3.grid(row = 1, column = 0, padx=15, pady=5, ipadx=65)

label3 = Label(tab2, text="Период", justify=CENTER, padx=25)
label3.grid(row=0, column=1)
var = IntVar()
var.set(1)

def check():
    if(var.get() == 1):
        combobox4_1.grid(row=1, column=2,padx=20)
    else:
        combobox4_1.grid_forget()

    if (var.get() == 2):
        combobox4_2.grid(row=2, column=2, padx=20)
    else:
        combobox4_2.grid_forget()

    if (var.get() == 3):
        combobox4_3.grid(row=3, column=2, padx=20)
    else:
        combobox4_3.grid_forget()

    if (var.get() == 4):
        combobox4_4.grid(row=4, column=2, padx=20)
    else:
        combobox4_4.grid_forget()

radiobutton1 = Radiobutton(tab2, text = "Неделя", variable=var, value = 1, command=check, justify=LEFT)
radiobutton1.grid(row = 1, column = 1)
radiobutton2 = Radiobutton(tab2, text = "Месяц", variable=var, value = 2, command=check, justify=LEFT)
radiobutton2.grid(row = 2, column = 1)
radiobutton3 = Radiobutton(tab2, text = "Квартал", variable=var, value = 3, command=check, justify=LEFT)
radiobutton3.grid(row = 3, column = 1)
radiobutton4 = Radiobutton(tab2, text = "Год", variable=var, value = 4, command=check, justify=LEFT)
radiobutton4.grid(row = 4, column = 1)


label4 = Label(tab2, text="Выбор периода", justify=CENTER)
label4.grid(row=0, column=2)

combobox4_1 = ttk.Combobox(tab2)
combobox4_1["values"] = ("02.05.2022 - 08.05.2022", "25.04.2022 - 01.05.2022", "18.04.2022 - 24.04.2022")
combobox4_1.grid(row=1, column=2,padx=20)
combobox4_1.current(0)

combobox4_2 = ttk.Combobox(tab2)
combobox4_2["values"] = ("Апрель", "Март", "Февраль")
combobox4_2.current(0)

combobox4_3 = ttk.Combobox(tab2)
combobox4_3["values"] = ("Январь Февраль Март", "Октябрь Ноябрь Декабрь", "Июль Август Сентябрь")
combobox4_3.current(0)

combobox4_4 = ttk.Combobox(tab2)
combobox4_4["values"] = ("2021", "2020", "2019")
combobox4_4.current(0)

def btn1_click():
    valute = combobox3.get()
    if valute == "Рубль":
        messagebox.showerror(title="Ошибка", message="Неконвертируемая валюта")
        return

    x, y = [], []
    window.geometry("1300x700")
    matplotlib.use('TkAgg')
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
    plot_widget = canvas.get_tk_widget()
    fig.clear()

    date = ""
    startdate = ""
    enddate = ""
    date_type = ""

    if (var.get() == 1):
        date_type = "week"
        date = combobox4_1.get()
    if (var.get() == 2):
        date_type = "month"
        date = combobox4_2.get()
    if (var.get() == 3):
        date_type = "cvartal"
        date = combobox4_3.get()
    if (var.get() == 4):
        date_type = "year"
        date = combobox4_4.get()

    num_str = {"01":"янв", "02":"фев", "03":"мар", "04":"апр", "05":"май", "06":"июн", "07":"июл", "08":"авг", "09":"сен", "10":"окт", "11":"ноя", "12":"дек"}
    str_num = {"Январь":"01", "Февраль":"02", "Март":"03", "Апрель":"04", "Май":"05", "Июнь":"06", "Июль":"07", "Август":"08", "Сентябрь":"09", "Октябрь":"10", "Ноябрь":"11", "Декабрь":"12"}

    nominal = 0
    def y_fill(response):
        dom = xml.dom.minidom.parse(response)
        dom.normalize()
        nodeArray = dom.getElementsByTagName("Valute")
        names = get_node_info("Name", nodeArray)
        nominals = get_node_info("Nominal", nodeArray)
        values = get_node_info("Value", nodeArray)
        for i in range(0, len(names)):
            if names[i] == valute:
                y.append(float(values[i].replace(',','.')) / float(nominals[i].replace(',','.')))
                break

    if date_type == "week":
        for i in range(0,7):
            if date[0] == '0':
                x.append(date[1:2]+' '+num_str.get(date[3:5]))
            else:
                x.append(date[0:3] + ' ' + num_str.get(date[3:5]))
            response1 = urllib.request.urlopen("https://cbr.ru/scripts/XML_daily.asp?date_req=" + date[0:10].replace('.','/'))
            y_fill(response1)
            date = (datetime.strptime(date[0:10],"%d.%m.%Y") + timedelta(days=1)).strftime("%d.%m.%Y")
    elif date_type == "month":
        days = monthrange(datetime.now().year, int(str_num.get(date)[1]))[1]
        month = str_num.get(date)
        for i in range (1,days+1):
            if i < 10:
                date = '0' + str(i) + '/' + month + '/' + "2022"
            else:
                date = str(i) + '/' + month + '/' + "2022"
            x.append(i)
            response2 = urllib.request.urlopen("https://cbr.ru/scripts/XML_daily.asp?date_req=" + date)
            y_fill(response2)

    if date_type == "cvartal":
        monthes = date.split(' ')
        for month in monthes:
            if month == "Февраль" or month == "Март":
                year = datetime.now().year
            else:
                year = datetime.now().year-1
            for day in range(7,22,7):
                x.append(str(day) + ' ' + num_str.get(str_num.get(month)))
                if day < 10:
                    date = '0' + str(day) + '/' + str_num.get(month) + '/' + str(year)
                else:
                    date = str(day) + '/' + str_num.get(month) + '/' + str(year)
                response3 = urllib.request.urlopen("https://cbr.ru/scripts/XML_daily.asp?date_req=" + date)
                y_fill(response3)

    if date_type == "year":
        year = date
        for i in range(1, 13):
            if(i < 10):
                x.append(num_str.get('0' + str(i)))
            else:
                x.append(num_str.get(str(i)))
            if(i < 10):
                date = "15" +'/'+'0' + str(i) + '/' + year
            else:
                date = "15" + '/' + str(i) + '/' +year
            response4 = urllib.request.urlopen("https://cbr.ru/scripts/XML_daily.asp?date_req=" + date)
            y_fill(response4)

    plt.plot(x, y)
    plt.grid()

    plot_widget.grid(row=5, column=3)

btn1 = Button(tab2, text='Построить график', command = btn1_click)
btn1.grid(column=0,row=3)

window.mainloop()

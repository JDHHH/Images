import tkinter as tk
import tkinter.messagebox
import tensorflow as tf
import numpy as np
from tkinter import *
from tkinter import filedialog
from keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import load_model
from PIL import Image, ImageTk

arr = ['001.Affenpinscher', '002.Afghan_hound', '003.Airedale_terrier', '004.Akita', '005.Alaskan_malamute',
       '006.American_eskimo_dog', '007.American_foxhound', '008.American_staffordshire_terrier',
       '009.American_water_spaniel', '010.Anatolian_shepherd_dog', '011.Australian_cattle_dog',
       '012.Australian_shepherd', '013.Australian_terrier', '014.Basenji', '015.Basset_hound', '016.Beagle',
       '017.Bearded_collie', '018.Beauceron', '019.Bedlington_terrier', '020.Belgian_malinois',
       '021.Belgian_sheepdog', '022.Belgian_tervuren', '023.Bernese_mountain_dog', '024.Bichon_frise',
       '025.Black_and_tan_coonhound', '026.Black_russian_terrier', '027.Bloodhound', '028.Bluetick_coonhound',
       '029.Border_collie', '030.Border_terrier', '031.Borzoi', '032.Boston_terrier', '033.Bouvier_des_flandres',
       '034.Boxer', '035.Boykin_spaniel', '036.Briard', '037.Brittany', '038.Brussels_griffon',
       '039.Bull_terrier', '040.Bulldog', '041.Bullmastiff', '042.Cairn_terrier', '043.Canaan_dog',
       '044.Cane_corso', '045.Cardigan_welsh_corgi', '046.Cavalier_king_charles_spaniel',
       '047.Chesapeake_bay_retriever', '048.Chihuahua', '049.Chinese_crested', '050.Chinese_shar-pei',
       '051.Chow_chow', '052.Clumber_spaniel', '053.Cocker_spaniel', '054.Collie', '055.Curly-coated_retriever',
       '056.Dachshund', '057.Dalmatian', '058.Dandie_dinmont_terrier', '059.Doberman_pinscher',
       '060.Dogue_de_bordeaux', '061.English_cocker_spaniel', '062.English_setter', '063.English_springer_spaniel',
       '064.English_toy_spaniel', '065.Entlebucher_mountain_dog', '066.Field_spaniel', '067.Finnish_spitz',
       '068.Flat-coated_retriever', '069.French_bulldog', '070.German_pinscher', '071.German_shepherd_dog',
       '072.German_shorthaired_pointer', '073.German_wirehaired_pointer', '074.Giant_schnauzer',
       '075.Glen_of_imaal_terrier', '076.Golden_retriever', '077.Gordon_setter', '078.Great_dane',
       '079.Great_pyrenees', '080.Greater_swiss_mountain_dog', '081.Greyhound', '082.Havanese', '083.Ibizan_hound',
       '084.Icelandic_sheepdog', '085.Irish_red_and_white_setter', '086.Irish_setter', '087.Irish_terrier',
       '088.Irish_water_spaniel', '089.Irish_wolfhound', '090.Italian_greyhound', '091.Japanese_chin',
       '092.Keeshond', '093.Kerry_blue_terrier', '094.Komondor', '095.Kuvasz', '096.Labrador_retriever',
       '097.Lakeland_terrier', '098.Leonberger', '099.Lhasa_apso', '100.Lowchen', '101.Maltese',
       '102.Manchester_terrier', '103.Mastiff', '104.Miniature_schnauzer', '105.Neapolitan_mastiff',
       '106.Newfoundland', '107.Norfolk_terrier', '108.Norwegian_buhund', '109.Norwegian_elkhound',
       '110.Norwegian_lundehund', '111.Norwich_terrier', '112.Nova_scotia_duck_tolling_retriever',
       '113.Old_english_sheepdog', '114.Otterhound', '115.Papillon', '116.Parson_russell_terrier',
       '117.Pekingese', '118.Pembroke_welsh_corgi', '119.Petit_basset_griffon_vendeen', '120.Pharaoh_hound',
       '121.Plott', '122.Pointer', '123.Pomeranian', '124.Poodle', '125.Portuguese_water_dog',
       '126.Saint_bernard', '127.Silky_terrier', '128.Smooth_fox_terrier', '129.Tibetan_mastiff',
       '130.Welsh_springer_spaniel', '131.Wirehaired_pointing_griffon', '132.Xoloitzcuintli', '133.Yorkshire_terrier']


class Window(Frame):

    # 获取分类名称的方法之一
    def getfilename(self, filename):
        for root, dirs, files in os.walk(filename):
            array = dirs
            if array:
                return array

    # 实现狗分类的函数
    def dogclassification(self, dogpath):
        # 读取一张待判断的图像
        test_img = tf.keras.preprocessing.image.load_img(dogpath, target_size=(224, 224, 3))  # 此处得到的是pillow图像Image实例
        test_img = tf.keras.preprocessing.image.img_to_array(test_img)  # 将Image实例转化为多维数组
        test_img = test_img / 255  # 此处还需要将0-255转化为0-1
        test_img = np.expand_dims(test_img, 0)  # 将三维输入图像拓展成四维张量
        pred = model.predict(test_img)  # 预测

        classes_name_list = arr
        kind = "".join(filter(str.isalpha, classes_name_list[pred.argmax()]))
        kind = "this is “" + kind + "” ，"
        probability = " the probability is " + str(max(pred[0]))

        t.delete('1.0', 'end')
        t.insert("insert", kind)
        t.insert("end", probability)
        tk.messagebox.showinfo("Finish!", "Finish!")

    # "识别"按钮函数

    def shibie(self):
        # print("输入路径及图片名称\n")
        filename = e.get()
        self.dogclassification(filename)

        load = Image.open(filename)
        load = load.resize((400, 400))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=20)

    # 打开filedialog

    def openfile_filedialog(self):
        Fpath = filedialog.askopenfilename()
        es.set(Fpath)
        load = Image.open(Fpath)
        load = load.resize((400, 400))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=20)

    # "关于"消息框
    def about_dialog(self):
        tk.messagebox.showinfo("关于",
                               "狗类识别，版本 1.0\n作者：纪东贺，沈连鑫，周俊乐，杨东岳\n版权所有(c) 2020")

    # 创建界面

    def createWidgets(self):
        menubar = tk.Menu(root)
        menubar.add_command(label='打开文件', command=self.openfile_filedialog)
        menubar.add_command(label="开始识别", command=self.shibie)

        aboutmenu = tk.Menu(menubar, tearoff=False)
        aboutmenu.add_command(label="关于", command=self.about_dialog)
        aboutmenu.add_separator()
        aboutmenu.add_command(label='退出', command=self.quit)
        menubar.add_cascade(label="其他", menu=aboutmenu)

        root.config(menu=menubar)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()

# 此处导入模型
model = load_model("E:\GoogleDownloads\model.h5")

root = Tk()
app = Window(master=root)
root.wm_title("Intelligence distinguishing")
root.geometry("500x500")

es = StringVar()
e = tk.Entry(root, textvariable=es)
e.pack(padx=10, pady=10, fill=BOTH)
es.set("在此栏键入图片路径或使用打开文件")

t = tk.Text(root, height=2)  # 这里设置文本框高，可以容纳两行
t.pack()
root.mainloop()

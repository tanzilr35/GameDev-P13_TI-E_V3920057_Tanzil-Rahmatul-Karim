import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode

from direct.gui.DirectGui import DirectFrame

# Add some text
bk_text = "Kelompok 2 Hore"
textObject = OnscreenText(text=bk_text, pos=(0.0, 0.70), scale=0.10,
                          fg=(6, 6, 6, 6), align=TextNode.ACenter,
                          mayChange=1)
# Callback function to set text
v = [0]
def setText(status=None):
    bk_text = "CurrentValue : %s"%v
    textObject.setText(bk_text)

def itemSel(arg):
    if arg == "Pilih Anggota Kelompok":
        l1 = DirectLabel(text="Kelompok 2", text_scale=0.07)
        l2 = DirectLabel(text="Kelas E", text_scale=0.08)
        l3 = DirectLabel(text="UNS", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="Dec",
            decButton_text_scale=0.04,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="Inc",
            incButton_text_scale=0.04,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(1,0,0,0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in []:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
        image='welcome.png', pos=(-0.65, 0, -0.45), scale=0.35,)
        
    if arg == "Anggota 1":
        buttons = [DirectRadioButton(text='D3 Teknik Informatika', variable=v, value=[0],
                             scale=0.05, pos=(0.7, 0, -0.45), command=setText),
            DirectRadioButton(text='D3 Teknik Hasil Pertanian', variable=v, value=[1],
                             scale=0.05, pos=(0.7, 0, -0.55), command=setText),
            DirectRadioButton(text='D3 Akuntansi', variable=v, value=[2],
                             scale=0.05, pos=(0.7, 0, -0.65), command=setText)]
        for button in buttons:
            button.setOthers(buttons)

        l1 = DirectLabel(text="Zulfi Masyita", text_scale=0.07)
        l2 = DirectLabel(text="V3920063", text_scale=0.08)
        l3 = DirectLabel(text="Kelas E", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="Dec",
            decButton_text_scale=0.04,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="Inc",
            incButton_text_scale=0.04,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(1,0,1,0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['','HOBI', 'Nonton,', 'Masak']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
        image='zulfi.png', pos=(-0.65, 0, -0.45), scale=0.35,)

    if arg == "Anggota 2":
        l1 = DirectLabel(text="Tanzil R K", text_scale=0.07)
        l2 = DirectLabel(text="V3920057", text_scale=0.08)
        l3 = DirectLabel(text="Kelas E", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="Dec",
            decButton_text_scale=0.04,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="Inc",
            incButton_text_scale=0.04,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(0,0,1,0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['','HOBI', 'Nonton,', 'Desain']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
        image='tanzil.png', pos=(-0.65, 0, -0.45), scale=0.35,)

    if arg == "Anggota 3":
        l1 = DirectLabel(text="Rifqi A", text_scale=0.07)
        l2 = DirectLabel(text="V3920053", text_scale=0.08)
        l3 = DirectLabel(text="Kelas E", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="Dec",
            decButton_text_scale=0.04,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="Inc",
            incButton_text_scale=0.04,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(0,1,0,0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['','HOBI', 'Gamer,', 'Masak']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
        image='rifqi.png', pos=(-0.65, 0, -0.45), scale=0.35,)

    if arg == "Anggota 4":
        l1 = DirectLabel(text="Yuanda", text_scale=0.07)
        l2 = DirectLabel(text="V3920062", text_scale=0.08)
        l3 = DirectLabel(text="Kelas E", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="Dec",
            decButton_text_scale=0.04,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="Inc",
            incButton_text_scale=0.04,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(1,1,0,0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['','HOBI', 'Gamer,', 'Mancing']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
        image='yuanda.png', pos=(-0.65, 0, -0.45), scale=0.35,)

    if arg == "Anggota 5":
        l1 = DirectLabel(text="Ilham H", text_scale=0.07)
        l2 = DirectLabel(text="V3920065", text_scale=0.08)
        l3 = DirectLabel(text="Kelas E", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="Dec",
            decButton_text_scale=0.04,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="Inc",
            incButton_text_scale=0.04,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(0,1,1,0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['','HOBI', 'Olahraga', 'Mancing']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
        image='ilham.png', pos=(-0.65, 0, -0.45), scale=0.35,)

# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=2,
                        items=["Pilih Anggota Kelompok", "Anggota 1",
                               "Anggota 2", "Anggota 3", "Anggota 4", "Anggota 5"],
                        highlightColor=(0.65, 0.1, 0.1, 1),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu

# Procedurally select a item
menu.set(0)

# Run the program
base.run()

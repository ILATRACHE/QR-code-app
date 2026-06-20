import qrcode
import tempfile
from tkinter import*


# url = input("entre the url : ").strip()
# file_path = f"QR_{int(time.time())}.png"
# qr = qrcode.QRCode()
# qr.add_data(url)
# img = qr.make_image()
# img.save(file_path)
# print("QRcode was generated!!")

window = Tk()
window.geometry("600x650")
window.title("Convert to QRcode")

url = Entry(window)
cansave = False
temp_file_path = None
img = None
def converter() : 
    url_qr = url.get().strip()
    if not url_qr :
        
        result_label.config(
        text=f"please entre above a url",
        fg="red"
    )
        return
    global temp_file_path
    temp_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name #explain
    global cansave 
    cansave= True
    qr = qrcode.QRCode()
    qr.add_data(url_qr)
    image = qr.make_image()
    image.save(temp_file_path)
    print("QR code has been coverted ")
    result_label.config(
        text=f"QR code has been coverted ",
        fg="green"
    )
    global img
    img = image
def qr_png(name):
    file_path = f"QR_{name}.png"

    return file_path


convert= Button(window , text="convert url  to QR code")
convert.config(command=converter)



result_label = Label(window, text="")

exist = Button(window , text="Exist " , command=window.destroy)
def save():
    file = file_name.get().strip()
    if not file :
        result_save.config(text='please entre above file where to save',fg="red")
        if cansave == False :
            result_label.config(
        text=f"please entre above a url",
        fg="red"
    )
    else :
        file_path = qr_png(file)
        ###
        img.save(file_path)
        result_save.config(text=f'{file_path} has been creat')
        pass
creat_file = Label(window , text='enrte QR name to save it')
file_name = Entry(window)
ssave = Button(window , text='save',command=save)
result_save = Label(window , text='')
def show():
    if img is None:
        return
    
    imgs = PhotoImage(file=temp_file_path)
    show_label.config(image=imgs)
    show_label.image = imgs  # ✅ KEEP REFERENCE




    pass
sshow = Button(window , text="show QR code" , command=show)
show_label = Label(window ,text='')

first_label = Label(window , text='please entre something')
first_label.pack()
url.pack()
convert.pack()
result_label.pack()
sshow.pack()
show_label.pack()
creat_file.pack()
file_name.pack()
ssave.pack()
result_save.pack()


exist.pack()
window.mainloop()

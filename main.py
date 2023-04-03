import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall
from cameraAD import startapplicationAD
from cameraFD import startapplicationFD
from finknife import knife_detection
from fireDetection import fireDetection

window = tk.Tk()
window.title("Smart Serveillance and Alert System")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart Surveillance And Alert System")
label_font = font.Font(size=20, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/main_icon2.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btnMon_image = Image.open('icons/Mon_icon.png')
btnMon_image = btnMon_image.resize((50,50), Image.ANTIALIAS)
btnMon_image = ImageTk.PhotoImage(btnMon_image)

# btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
# btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
# btn2_image = ImageTk.PhotoImage(btn2_image)




#btn3_image = Image.open('icons/security-camera.png')
#btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
#btn3_image = ImageTk.PhotoImage(btn3_image)

btnIden_image = Image.open('icons/identify_icon.png')
btnIden_image = btnIden_image.resize((50,50), Image.ANTIALIAS)
btnIden_image = ImageTk.PhotoImage(btnIden_image)

btnRec_image = Image.open('icons/recording.png')
btnRec_image = btnRec_image.resize((50,50), Image.ANTIALIAS)
btnRec_image = ImageTk.PhotoImage(btnRec_image)

btnCrash_image = Image.open('icons/crash_icon.png')
btnCrash_image = btnCrash_image.resize((50,50), Image.ANTIALIAS)
btnCrash_image = ImageTk.PhotoImage(btnCrash_image)

btnInOut_image = Image.open('icons/in_out_icon.png')
btnInOut_image = btnInOut_image.resize((50,50), Image.ANTIALIAS)
btnInOut_image = ImageTk.PhotoImage(btnInOut_image)

btnKnifeDet_image = Image.open('icons/knife_icon.png')
btnKnifeDet_image = btnKnifeDet_image.resize((50,50), Image.ANTIALIAS)
btnKnifeDet_image = ImageTk.PhotoImage(btnKnifeDet_image)

btnFallDet_image = Image.open('icons/fall_icon.png')
btnFallDet_image = btnFallDet_image.resize((50,50), Image.ANTIALIAS)
btnFallDet_image = ImageTk.PhotoImage(btnFallDet_image)

btnFireDet_image = Image.open('icons/fire_icon.png')
btnFireDet_image = btnFireDet_image.resize((50,50), Image.ANTIALIAS)
btnFireDet_image = ImageTk.PhotoImage(btnFireDet_image)

btnExit_image = Image.open('icons/exit.png')
btnExit_image = btnExit_image.resize((50,50), Image.ANTIALIAS)
btnExit_image = ImageTk.PhotoImage(btnExit_image)




# --------------- Button -------------------#
btn_font = font.Font(size=25)
btnMon = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green',command = find_motion, image=btnMon_image, compound='left')
btnMon['font'] = btn_font
btnMon.grid(row=3, pady=(20,10))

# btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=rect_noise, compound='left', image=btn2_image)
# btn2['font'] = btn_font




btn_font = font.Font(size=25)

#btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=noise, image=btn3_image, compound='left')
#btn3['font'] = btn_font
#btn3.grid(row=5, pady=(20,10))








btnIden = tk.Button(frame1, text="identify", fg="green",command=maincall, compound='left', image=btnIden_image, height=90, width=180)
btnIden['font'] = btn_font
btnIden.grid(row=3, column=2, pady=(20,10))

btnRec = tk.Button(frame1, text='Record', height=90, width=180, fg='green', command=record, image=btnRec_image, compound='left')
btnRec['font'] = btn_font
btnRec.grid(row=3, pady=(20,10), column=3, padx=(20,5))
# btn4.grid(row=5, pady=(20,10), column=3)

btnCrash = tk.Button(frame1, text="Crash", fg="green",command=startapplicationAD, compound='left', image=btnCrash_image, height=90, width=180)
btnCrash['font'] = btn_font
btnCrash.grid(row=5, pady=(20,10))

btnInOut = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', command=in_out, image=btnInOut_image, compound='left')
btnInOut['font'] = btn_font
btnInOut.grid(row=5, pady=(20,10), column=3)
# btn6.grid(row=5, pady=(20,10), column=2)

btnKnifeDet = tk.Button(frame1, text="Knife", fg="green",command=knife_detection, compound='left', image=btnKnifeDet_image, height=90, width=180)
btnKnifeDet['font'] = btn_font
btnKnifeDet.grid(row=9, pady=(20,10))

btnFallDet = tk.Button(frame1, text="Fall", fg="green",command=startapplicationFD, compound='left', image=btnFallDet_image, height=90, width=180)
btnFallDet['font'] = btn_font
btnFallDet.grid(row=9, column=2, pady=(20,10))

btnFireDet = tk.Button(frame1, text="fire", fg="green",command=fireDetection, compound='left', image=btnFireDet_image, height=90, width=180)
btnFireDet['font'] = btn_font
btnFireDet.grid(row=9, column=3, pady=(20,10))

btnExit = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btnExit_image)
btnExit['font'] = btn_font
btnExit.grid(row=12, pady=(20,10), column=2)

frame1.pack()
window.mainloop()



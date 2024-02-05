#Create training data
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
from tkinter import *
import math  
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import os
#import pandas as pd



def deleteall():
    for child in c.winfo_children():
        if child != keep_me:
            child.destroy()

def dist(x1,y1,x2,y2):  
     ds = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return ds  
 
def drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y):
    global k_lines,r_lines
    l1=c.create_line(tl_x,tl_y,bl_x,bl_y,tl_x,tl_y,tr_x,tr_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,br_x,br_y,width=2,fill="blue")
    for r in range(1,8):
        x1,y1=(tl_x+r/8*(bl_x-tl_x),tl_y+r/8*(bl_y-tl_y))
        x2,y2=(tr_x+r/8*(br_x-tr_x),tr_y+r/8*(br_y-tr_y))
        r_lines[r]=c.create_line(x1,y1,x2,y2)
    
    for k in range(1,8):
        x1,y1=(tl_x+k/8*(tr_x-tl_x),tl_y+k/8*(tr_y-tl_y))
        x2,y2=(bl_x+k/8*(br_x-bl_x),bl_y+k/8*(br_y-bl_y))
        k_lines[k]=c.create_line(x1,y1,x2,y2)

selected  = ""
def selectcorner(event):
    global circle
    global selected
    x1=event.x
    y1=event.y
    if dist(x1,y1,tl_x,tl_y)<10:
        if circle !=-1:
            c.delete(circle) 
        circle = c.create_oval(tl_x-5,tl_y-5 ,tl_x+5,tl_y+5,outline="red", width=2)
        selected = "tl"
    elif dist(x1,y1,tr_x,tr_y)<10:
        if circle !=-1:
            c.delete(circle) 
        circle = c.create_oval(tr_x-5,tr_y-5 ,tr_x+5,tr_y+5,outline="red", width=2)
        selected = "tr"
    elif dist(x1,y1,bl_x,bl_y)<10:
        if circle !=-1:
            c.delete(circle) 
        circle = c.create_oval(bl_x-5,bl_y-5 ,bl_x+5,bl_y+5,outline="red", width=2)
        selected = "bl"
    elif dist(x1,y1,br_x,br_y)<10:
        if circle !=-1:
            c.delete(circle) 
        circle = c.create_oval(br_x-5,br_y-5 ,br_x+5,br_y+5,outline="red", width=2)
        selected = "br"

#Drag corners
def dragcorner(event):
    global tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,circle
    if selected =="tl":
        tl_x,tl_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor=NW, image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y)
        circle = c.create_oval(tl_x-5,tl_y-5 ,tl_x+5,tl_y+5,outline="red", width=2)
    elif selected =="tr":
        tr_x,tr_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor=NW, image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y)
        circle = c.create_oval(tr_x-5,tr_y-5 ,tr_x+5,tr_y+5,outline="red", width=2)
    elif selected =="bl":
        bl_x,bl_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor=NW, image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y)
        circle = c.create_oval(bl_x-5,bl_y-5 ,bl_x+5,bl_y+5,outline="red", width=2)
    elif selected =="br":
        br_x,br_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor=NW, image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y)
        circle = c.create_oval(br_x-5,br_y-5 ,br_x+5,br_y+5,outline="red", width=2)
        
        
Datadir="C:/Users/Access/Board Detection App/"
path = os.path.join(Datadir, "t")
for imgpath in os.listdir(path):
    file_path=os.path.join(path,imgpath)
        
    root=Tk()
    img = Image.open(file_path)
    rr=img.height/600
    img=img.resize((int(img.width*600/img.height),600))
    file = ImageTk.PhotoImage(img)
    root.geometry('800x800')
    c=Canvas(width=img.size[0],height=img.size[1],bg='red')
    image=c.create_image(2, 2, anchor=NW, image=file)



    #Initialize Grid
    circle = -1 
    top_left=(10,10)
    tl_x,tl_y=top_left
    top_right=(590,10)
    tr_x,tr_y=top_right
    buttom_left=(10,590)
    bl_x,bl_y=buttom_left
    buttom_right=(590,590)
    br_x,br_y=buttom_right
    #l1=c.create_line(tl_x,tl_y,bl_x,bl_y,tl_x,tl_y,tr_x,tr_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,br_x,br_y,width=5,fill="green")
    r_lines={}
    k_lines={}
    drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y)
       
    c.bind("<B1-Motion>",dragcorner)
    c.bind("<Button-1>",selectcorner)
    c.pack()
    root.mainloop()
    print('done')

    #Crop and transform image
    image = cv2.imread(file_path)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),0)
    #gray = cv2.equalizeHist(gray)
    gray = cv2.GaussianBlur(gray,(3,3),0)
    contour =np.array([[int(tl_x*rr),int(tl_y*rr)],
           [int(tr_x*rr),int(tr_y*rr)],
           [int(br_x*rr),int(br_y*rr)],
           [int(bl_x*rr),int(bl_y*rr)]],np.float32)
    h = np.array([ [0,0],[511,0],[511,511],[0,511] ],np.float32)
    retval = cv2.getPerspectiveTransform(contour,h)
    warp = cv2.warpPerspective(image,retval,(512,512))
    #warp=cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)
    #file='a b c d e f g h'.split()
    images={}
    w=warp.shape[1]
    h=warp.shape[0]
    #labeled=[]
    #FEN="rnbqkbnr/pppppppp/pkqrbnpk/eknrbbnq/eRKQRBNP/BKQRBNPK/PPPPPPPP/RNBQKBNR".split("/")
    FEN="nBePrkKn/eprebKRQ/beQreBPp/eReRbPNK/qpKqBqNr/ePnRBQBk/kPPKKRRB/bpeBKNPN".split("/")
    for c in range(0,8):
        for r in range(0,8):
            new_image=warp[int((r)*(h/8)):int((r+1)*(h/8)),int(c*(w/8)):int((c+1)*(w/8))]
            cv2.imwrite("C:/Users/Access/Board Detection App/Test/"+str(FEN[r][c])+str(r)+str(c)+imgpath[:-4]+".png",new_image)
            #label=["C:/Users/Access/Board Detection App/test1/"+str(FEN[r][c])+str([r])+ str(c)+"8.png",FEN[r][c]]
            #labeled.append(label)
              
        
#asnum=np.asarray(labeled)
#df=pd.DataFrame(asnum)
#df.to_csv("C:\\Users\\Access\\Board Detection App\\test1.csv",index=False)
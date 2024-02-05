import numpy as np
import cv2
import tkinter as tk
import tkinter.font as font
import math  
from PIL import Image, ImageTk
import sys
import load_models as lm
import pandas as pd
import webbrowser
from tkinter import filedialog
from tkinter.ttk import Style
#import GUI

file_path="C:\\Users\\Access\\Board Detection App\\photo1.jpg"

#split board pieces 
def splitpieces(image):
    file='a b c d e f g h'.split()
    images=pd.DataFrame(columns=['File','Rank','Image','Empty','Piece'])
    w=image.shape[1]
    h=image.shape[0]
    for c in range(0,8):
        for r in range(0,8):
            cell=image[int((8-r-1)*(h/8)):int((8-r)*(h/8)),int(c*(w/8)):int((c+1)*(w/8))]
            cell=cv2.resize(cell,(30,30))
            row=pd.DataFrame([[file[c],str(8-r),cell]],columns=['File','Rank','Image'])
            images=images.append(row, ignore_index=True )
            # if (r+c)%2==0:               
                
            # else:
            #     images[file[c]+str(r+1)]=[cell,'w']           
    return images



def construct_FEN(board):
    
    FEN=''
    if flip.get()==1:
        rng=range(8,0,-1)
        file='hgfedcba'
    else:
        rng=range(1,9)
        file='abcdefgh'
 
    for r in rng:
        rank=board[board['Rank']==str(r)]
        row_FEN=''
        for f in file:
            
            em=rank[rank['File']==f]['Empty'].values[0]
            pi=rank[rank['File']==f]['Piece'].values[0]
            if em == 0:
                row_FEN=row_FEN+'1'
            else:
                row_FEN=row_FEN+pi
                
        FEN=FEN+row_FEN+'/'
       
        
    return FEN
    
    
    
#delete all images in canvas
def deleteall():
    for child in c.winfo_children():
    # Here's where I need help. Don't know how to single-out 'keep_me'
        child.destroy()

def dist(x1,y1,x2,y2):  
     ds = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return ds  
 
def drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,g_on):    
    c.create_line(tl_x,tl_y,bl_x,bl_y,tl_x,tl_y,tr_x,tr_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,br_x,br_y,width=2,fill="blue")
    if g_on==1:
        for r in range(1,8):
            x1,y1=(tl_x+r/8*(bl_x-tl_x),tl_y+r/8*(bl_y-tl_y))
            x2,y2=(tr_x+r/8*(br_x-tr_x),tr_y+r/8*(br_y-tr_y))
            c.create_line(x1,y1,x2,y2)
            #r_lines[r]=
        
        for k in range(1,8):
            x1,y1=(tl_x+k/8*(tr_x-tl_x),tl_y+k/8*(tr_y-tl_y))
            x2,y2=(bl_x+k/8*(br_x-bl_x),bl_y+k/8*(br_y-bl_y))
            c.create_line(x1,y1,x2,y2)
    

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
        image=c.create_image(2, 2, anchor="nw", image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,grid.get())
        circle = c.create_oval(tl_x-5,tl_y-5 ,tl_x+5,tl_y+5,outline="red", width=2)
    elif selected =="tr":
        tr_x,tr_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor="nw", image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,grid.get())
        circle = c.create_oval(tr_x-5,tr_y-5 ,tr_x+5,tr_y+5,outline="red", width=2)
    elif selected =="bl":
        bl_x,bl_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor="nw", image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,grid.get())
        circle = c.create_oval(bl_x-5,bl_y-5 ,bl_x+5,bl_y+5,outline="red", width=2)
    elif selected =="br":
        br_x,br_y=event.x,event.y
        c.delete('all')
        image=c.create_image(2, 2, anchor="nw", image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,grid.get())
        circle = c.create_oval(br_x-5,br_y-5 ,br_x+5,br_y+5,outline="red", width=2)
        
def controlgrid():
    if grid.get()==1:
        c.delete('all')
        image=c.create_image(2, 2, anchor="nw", image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,grid.get())
    else :
        c.delete('all')
        image=c.create_image(2, 2, anchor="nw", image=file)
        drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,grid.get())

def closeapp():
    root.destroy() 

def closebrowse():
    rootb.destroy()
    
def browsefiles():
    global file_path
    file_path=filedialog.askopenfilename(initialdir='/',title='Select image file:',filetype=(('All','*.*'),("jpeg","*.jpg"),("jpg","*.jpg"),("png","*.png")))
    ok['state']='normal'
    
    
def reset():
    GUI()

#Initialize Grid
def initializegrid():
    global  tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,circle
    ch.select()
    c.delete('all')
    image=c.create_image(2, 2, anchor="nw", image=file)
    circle = -1
    top_left=(0.1*new_width,0.1*new_height)
    tl_x,tl_y=top_left
    top_right=(0.9*new_width,0.1*new_height)
    tr_x,tr_y=top_right
    buttom_left=(0.1*new_width,0.9*new_height)
    bl_x,bl_y=buttom_left
    buttom_right=(0.9*new_width,0.9*new_height)
    br_x,br_y=buttom_right
    #l1=c.create_line(tl_x,tl_y,bl_x,bl_y,tl_x,tl_y,tr_x,tr_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,br_x,br_y,width=5,fill="green")
    #r_lines={}
    #k_lines={}
    drawgrid(tl_x,tl_y,tr_x,tr_y,br_x,br_y,bl_x,bl_y,1)
 
def transform_img():
    global warp
    image = cv2.imread(file_path)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),0)
    gray = cv2.equalizeHist(gray)
    #gray = cv2.GaussianBlur(gray,(3,3),0)
    contour =np.array([[int(tl_x*rr),int(tl_y*rr)],
           [int(tr_x*rr),int(tr_y*rr)],
           [int(br_x*rr),int(br_y*rr)],
           [int(bl_x*rr),int(bl_y*rr)]],np.float32)
    h = np.array([ [0,0],[511,0],[511,511],[0,511] ],np.float32)
    retval = cv2.getPerspectiveTransform(contour,h)
    warp = cv2.warpPerspective(image,retval,(512,512))
    warp2=cv2.cvtColor(warp, cv2.COLOR_BGR2RGB)
    imgc=Image.fromarray(warp2)
    return imgc

#Browse file screen
def browse_GUI():
    global f,rootb,ok
    rootb=tk.Tk()
    rootb.title('Choose Image')
    rootb.geometry('300x100')
    f=font.Font(size=12,weight='bold')
    br=tk.Button(rootb,text='Browse',command=browsefiles,height=1, width=10)
    br.pack(side='top',anchor='n')
    br['font']=f
    ok=tk.Button(rootb,text='Ok',command=closebrowse,height=1, width=10,state="disabled")
    ok.pack(side='top',anchor='n')
    ok['font']=f
    rootb.mainloop()



#Build Image GUI
def buildimg_GUI():
    global new_width,new_height,root,rr,c,ch,grid,file,v,flip
    root=tk.Tk()
    root.title('Board Contour Selection')
    style = Style(root) 
    style.configure("TRadiobutton", background = "light green",  
                foreground = "red", font = ("arial", 12, "bold"))
    img = Image.open(file_path)
    rr=img.height/600
    new_height=600
    new_width=int(img.width*new_height/img.height)
    img=img.resize((new_width,new_height))
    file = ImageTk.PhotoImage(img)    
    root.geometry(str(new_width+300)+"x"+str(new_height))
    c=tk.Canvas(width=img.size[0],height=img.size[1])
    selected  = ""
    
    #Add GUI buttons
    #font=font.Font(size=12,weight='bold')
  
    
    c.bind("<B1-Motion>",dragcorner)
    c.bind("<Button-1>",selectcorner)
    c.pack(side='left',anchor='nw')
    b=tk.Button(root,text='Finish',command=closeapp,height=1, width=10)
    b.pack(side='top',anchor='n')
    b['font']=f
    b2=tk.Button(root,text='Reset',command=initializegrid,height=1, width=10)
    b2.pack(side='top',anchor='n')
    b2['font']=f
    grid=tk.IntVar()
    ch=tk.Checkbutton(root,text='Show grid (only for flat images)',variable=grid,command=controlgrid)
    ch.select()
    ch['font']=f
    ch.pack(side='top',anchor='n')
    ch.pack(side='top',anchor='n')
    flip=tk.IntVar()
    fl=tk.Checkbutton(root,text='Flipped',variable=flip)
    fl.deselect()
    fl['font']=f
    fl.pack(side='top',anchor='n')
   
    l1=tk.Label(root,text='Select which side to play:')
    l1.pack(side='top',anchor='n',ipady=10)
    l1['font']=f
    
    v = tk.StringVar(root, "w") 
    values = {"White to play" : "w", 
          "Black to play" : "b"} 
    for (text, value) in values.items(): 
        tk.Radiobutton(root, text = text, variable = v, 
        value = value).pack(side ='top', ipady = 5) 
    initializegrid()   
    root.mainloop()

def retryselect():
    rootI.destroy()
    buildimg_GUI()
    imgc=transform_img()
    ImageC_GUI(imgc)
    
def closetransform():
    rootI.destroy()
    
def ImageC_GUI(imgc):
    global f,rootI,ok
    rootI=tk.Tk()
    rootI.title("Image Preview")
    rootI.geometry('600x512')
    cc=tk.Canvas(width=512,height=512)
    imgtk = ImageTk.PhotoImage(imgc)
    imagec=cc.create_image(2, 2, anchor="nw", image=imgtk)
    cc.pack(side='left',anchor='nw')
    f=font.Font(size=12,weight='bold')
    retry=tk.Button(rootI,text='Retry',command=retryselect,height=1, width=10)
    retry.pack(side='top',anchor='n')
    retry['font']=f
    ok2=tk.Button(rootI,text='Ok',command=closetransform,height=1, width=10)
    ok2.pack(side='top',anchor='n')
    ok2['font']=f
    rootI.mainloop()
    

def predictpositions():
    gray_warp=cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)
    #gray_warp = cv2.GaussianBlur(gray_warp,(3,3),0)
    gray_warp = cv2.equalizeHist(gray_warp)
    
    #Load Models
    pieces_model=lm.create_model_pieces()
    empty_model=lm.create_model_empty()
    
    
    
    #Run the model over the board
    images=splitpieces(gray_warp)
    x=np.array(images['Image'].tolist()).reshape((-1,30,30,1))
    
    
    #Empty cells model prepare set
    xe=(x*1).astype(int)
    xe[xe>255]=255
    xe=xe/255.0
    
    x=x/255.0
    
    #Predict empty cells
    empty_predict=empty_model.predict(xe)
    empty_predict=[round(num.max()) for num in empty_predict]
    images['Empty']=empty_predict
    
    #Predict pieces
    pieces_predict=pieces_model.predict(x)
    
    #Predict empty cells
    empty_predict=empty_model.predict([xe,pieces_predict])
    empty_predict=[round(num.max()) for num in empty_predict]
    images['Empty']=empty_predict
    
    
    pieces_predict=pieces_predict.argmax(axis=1)
    pieces_predict=['KQRBNPkqrbnp'[i] for i in pieces_predict]
    images['Piece']=pieces_predict
    FEN=construct_FEN(images)
    lichess="https://lichess.org/editor/" + FEN[:-1] + "_"+v.get()+"_-_-_0_1"
    print(lichess)
    webbrowser.open(lichess, new=2)






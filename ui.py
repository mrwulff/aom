import graphics
from graphics5 import *
import os
import fnmatch
from urllib import *
import xlrd
from xlrd import *
import xlwt
from string import *
import exifread
import ExifTags
from string import  *
from os import listdir
import glob
from os.path import isfile, join
from geopy.distance import great_circle
from geopy.distance import vincenty
from timeit import default_timer as timer
from xlutils.copy import copy
from msvcrt import getch
#import Tkinter as tk
from PIL import  Image as Image2
aomw=1280
aomh=720

def get_gps(win,img,la,lo):
    errortext=Text(Point(600,150), '')
    lat=0,0,0/1
    lon=0,0,0/1
    #print img
    tags = exifread.process_file(open(img, 'rb'))                                              

    geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}

    #print geo
    #print geo.keys()
    try:
        lon=geo['GPS GPSLongitude']
        lat= geo['GPS GPSLatitude']
       #print lon,lat
    except:
        #lon=0
        #lat=0
        #win.getMouse()
        print 'omg'
    #print type(lon)
    
    #print lon
    #print len(lon)
    dlon=conv(lon)
    dlon=dlon*-1.0
    dlat=conv(lat)

    imglocation=( dlat,dlon)
    closest=10000
    closest=long(closest)
    for a in range(1,len(la)):
        maplocation=(la[a],lo[a])

        distance= vincenty(imglocation,maplocation).miles
        #print distance,a

        if distance<closest:
            #print 'yes'
            number=a
            closest=distance
    #print closest,number
    if closest>1:
        print
        img2=img.replace('pics/','')
        errortext=Text(Point(400,350), img+' was '+str(closest)+' miles from nearest location')
        errortext.draw(win)
        
        cwd = os.getcwd()
        cwd2=cwd+'/'+img
        print cwd2
        #os.system(cwd2)
        sett=Text(Point(400,375), 'Set Location Number')
        

        background = Rectangle(Point(300,360), Point(500,390))
        background.setFill('Green')
        background.draw(win)
        sett.draw(win)

        ent=Entry(Point(510,375),5)
        ent.draw(win)

        skip =  Rectangle(Point(300,395), Point(500,425))
        skip.setFill('Gray')
        skip.draw(win)

        skipt=Text(Point(400,415), 'Skip')
        skipt.draw(win)
        
        print img2
        convert2gif(img2)
        img3='temp/'+img2+'.gif'
        
        excel=Image(Point(1050,(aomh/2)-50), img3)
        excel.draw(win)
        win.getMouse()
        errortext.undraw()
    return closest,number,
        
        
def conv(deg):
    deg=str(deg)
    deg=deg[1:]
    deg=deg[:-1]
    d,m,s=split(deg,',')
    #print d,m,s
    #print s
    try:
        ss,sss=split(s,'/')
    except:
        ss=s
        sss=1
    #print ss,sss
    ss=int(ss)
    ss=ss*1.0
    sss=int(sss)
    ssss=ss/sss
    rs= ssss/3600
    #print rs

    m=int(m)
    m=m*1.0
    rm=m/60
    #print rm

    d=int(d)
    rd=d*1.0

    realloc=rd+rm+rs
    #print realloc
    return realloc


def make_list():
    lilat=[0]
    lilon=[0]
    liadd=[0]
    mypath="urls"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    for a in range(1,len(onlyfiles)):
        #print onlyfiles[a]
        lat,lon,add=parseloc(str(a)+'.html')
        #print lat
        junk,lat=split(lat,": ")
        lat=lat[:-2]
        lat=float(lat)
        

        junk,lon=split(lon,": ")
        lon=float(lon)
        #print lat,lon
        lilat.append(lat)
        lilon.append(lon)
        liadd.append(add)
    
        
    return lilat,lilon,liadd

def parseloc(f):
    a=open("urls/"+f,'r')
    i=0
    for line in a.readlines():
        #print line
        if '"location" : {' in line:
            #print line
            locationofline=i
            #print i
        if 'formatted_address' in line:
            locationofadd=i
        i=i+1
        #print i
    #print locationofline
    a.close()
    a=open("urls/"+f,'r')
    i=0
    for line in a.readlines():
        #print i
        if i==locationofline+1:
            lat=line
        if i==locationofline+2:
            lon=line
        if i==locationofadd:
            add=line
    



        i=i+1

    #print add
    add=split(add,'"')
    add=add[3]
    ad=split(add,',')
    add=ad[0]
    #print ad
    #b=raw_input('stop::::')
    return lat,lon,add

def findjpg(la,lo,add,win):
    startr=timer()
    end=0
    start=0
    cc=0
    aomlogot2=Text(Point(600,80+(25*int(1))), '')
    aomlogot2.draw(win)

    aomlogot32=Text(Point(600,80+(25*int(1))), '')
    aomlogot32.draw(win)

    aomlogot33=Text(Point(600,80+(25*int(1))), '')
    aomlogot33.draw(win)

    aomlogot34=Text(Point(600,80+(25*int(1))), '')
    aomlogot34.draw(win)

    aomlogot35=Text(Point(600,80+(25*int(1))), '')
    aomlogot35.draw(win)
    
    #print add
    #add='test'
    
    a= glob.glob('pics/*.JPG')
    #print len(a)
    #print type(a)
    for b in range(len(a)):
        cc=cc+1
        if cc%20==0:
            aomlogot2.undraw()
            aomlogot32.undraw()
            aomlogot33.undraw()
            aomlogot34.undraw()
            aomlogot35.undraw()
        mapn=0
        #distance,mapn=get_gps(a[b],la,lo)
        fou="Found"+str(len(a))+'pics'
        #print fou
        #print cc,len(a)
        #try:
        if 1==1:
            #end = timer()
            distance,mapn=get_gps(win,a[b],la,lo)
           
            
            #start = timer()
            
            
            #print(end - start)   

            #aomlogot2=Text(Point(600,80+(25*int(1))), "Found"+len[a]+'pics')
            
            if cc%20==0 or cc==len(a):
                
                if cc==len(a):
                    aomlogot2.undraw()
                    aomlogot32.undraw()
                    aomlogot33.undraw()
                    aomlogot34.undraw()
                    aomlogot35.undraw()
                    #aomlogot33.undraw()
                    
                    
                aomlogot2=Text(Point(600,80), "Found"+str(len(a))+'pics')
                aomlogot2.draw(win)

                aomlogot32=Text(Point(600,105), a[b])
                aomlogot32.draw(win)

                aomlogot33=Text(Point(600,130), str(len(a)-cc)+'pics remaining')
                aomlogot33.draw(win)
                perc=1.0*cc/len(a)
                #print perc
                #perc=perc*100
                nw=perc*aomw
                #print nw
                #nw=nw*100
                background = Rectangle(Point(0,190), Point(nw,210))
                background.setFill('green')
                background.draw(win)
                end=timer()
                tim=(end - start)
                #print tim
                timleft=tim/20*(len(a)-cc)
                #print timleft
                timleft=format(timleft, '.2f')

                aomlogot34=Text(Point(600,150), str(timleft)+' seconds left')
                aomlogot34.draw(win)


                
                start = timer()
                totaltime=end-startr
                #print totaltime
                totaltime=format(totaltime, '.2f')
                aomlogot35=Text(Point(600,170), str(totaltime)+'  total time')
                aomlogot35.draw(win)
                
            
            
        #except:
        #    print a[b],'NO DATA'
           # aomlogot2=Text(Point(600,80), "Found"+len[a]+'pics')
           # aomlogot2.draw(win)

        #print str(mapn)
        #print add[mapn]

        aa=str(mapn)+"__"+str(add[mapn])
        if mapn==0:
            aa="NO DATA"

        try:
            os.stat(aa)
            
        except:
            os.mkdir(aa)
            print "Making Folder "+str(mapn)
        #print a[b]
        dd= aa+"/"+a[b]
        dd=dd.replace('/pics','')
        #dd='sorted/'+dd
        #print dd
        ####DEBUG#####
        #os.rename(a[b],dd)
    return 0
        
        

def getcord(test,mnv):
    try:
        b=open('urls/test.html','w')
        #os.makedirs(d)
    except:
        os.makedirs('urls')
    flag=0
    aa=("https://maps.googleapis.com/maps/api/geocode/json?address="+test+"&key=AIzaSyBffb8Hm38qJihiAktFwYqWJWoykGpSP6Q")
    #print aa
    try:
        b=open('urls/'+mnv+'.html')
        #print "success"
        flag=1
    except:
        
        urlretrieve(aa,'urls/'+mnv+'.html')
        print 'downloaded'
        b=open('urls/'+mnv+'.html')
        flag=0
    bbb=0
    #for line in b.readlines():
    #    if '"location" : {' in line:
    #        add=bbb 
    #    bbb=bbb+1
    #bbb=0
    #print add
    #for line in b.readlines():
    #    if bbb==add:
    #        print line
    myNames = b.readlines()
    #print myNames
    for f in range(len(myNames)):
        #print myNames[f]
        if '"location" : {' in myNames[f] :
            #print "OMG",f
            if flag==0:
                ''
                #print myNames[f+1],myNames[f+2]
            lat=myNames[f+1]
            lon=myNames[f+2]
            junk,lat=split(lat,': ')
            lat,junk=split(lat,',')
            junk,lon=split(lon,': ')
            lon=lon[:-2]
            #print lat,lon,lat,lon
            return lat,lon
            
        
def openexcel(win,filex):
    init2(win,0,1,0,0)
    aomlogot2=Text(Point(600,80+(25*int(1))), '')
    aomlogot2.draw(win)

    aomlogot4=Text(Point(600,80+(25*int(1))), '')
    aomlogot4.draw(win)

    book = xlrd.open_workbook(filex)
    #print "The number of worksheets is", book.nsheets
    #print "Worksheet name(s):", book.sheet_names()
    sh = book.sheet_by_index(0)
    #print sh.name, sh.nrows, sh.ncols
    #print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
    flag=0
    excellist=[]
    goodlist=[]
    #raw_input('...')
    listy=['Map Number','Station Name','Address1','State','Zip']
    for rx in range(0,1):
        
        aa= sh.row(rx)
        #print
        for cx in range(sh.ncols):
            
            idd= sh.cell_value(rx,cx)
            #idd= str(cx)+'='+sh.cell_value(rx,cx)
            excellist.append(idd)
            if cx%2==1:
                background = Rectangle(Point(200,67+(25*int(cx))), Point(aomw-200,93+(25*int(cx))))
                background.setFill(color_rgb(250,230,230))
                background.draw(win)
                
            aomlogot = Text(Point(aomw/3,80+(25*int(cx))), idd)
            aomlogot.draw(win)
        flag=0
        for ly in range(len(listy)):
            
            idd= listy[ly]
            try:
                aomlogot.undraw()
            except:
                'not'
            #aomlogot = Text(Point(aomw/3+200,80+(25*int(ly))), "Pick: "+idd)
            aomlogot = Text(Point(aomw/3+200,50), "Pick:\n "+idd)
            aomlogot.setStyle('bold')

            aomlogot.draw(win)

            #z=getKey(win)
            
            z=win.getMouse()
            x=z.getX()
            y=z.getY()
            print x,y
            #print ord(z)
            #z=win.getMouse()
            #found=int(z)
            
            #aomlogot2.undraw()
            found= int((y-75)/25)
            #print [found]

            aomlogot2 = Text(Point(aomw/3+400,80+(25*int(ly))), "Picked: "+excellist[found])
            try:
                goodlist.append(found)
            except:
                print found,type(found)
            
            aomlogot2.draw(win)
            if y>600 and found>-1:
                ''




    #print goodlist
        
    #default=raw_input('default?...')
    mn=goodlist[0]
    sn=goodlist[1]
    ad=goodlist[2]
    
    st=goodlist[3]
    zi=goodlist[4]
    if 1==2:


        mn=raw_input('Map Number==')
        sn=raw_input('Station Name==')
        #br=raw_input('Brand==')
        ad=raw_input('Address 1==')
        st=raw_input('State==')
        zi=raw_input('Zip==')
        mn=int(mn)
        sn=int(sn)
        br=int(br)
        ad=int(ad)
        zi=int(zi)
        st=int(st)

    ttt=open('te.bro','w')
    ttt.write('manager;1.1\n')
    ttt.write('route;SUPER;0\n')
    
    for rx in range(1,sh.nrows):
        
        aa= sh.row(rx)
        #print
        for cx in range(sh.ncols):
            #print cx,'=',sh.cell_value(rx,cx)
            mnv=sh.cell_value(rx,mn)
            snv=sh.cell_value(rx,sn)
            #brv=sh.cell_value(rx,br)
            adv=sh.cell_value(rx,ad)
            ziv=sh.cell_value(rx,zi)
            stv=sh.cell_value(rx,st)
        #print mnv,snv,brv,adv,ziv
        ziv=str(ziv)
        adv=str(adv)
        #print ziv
        ziv,junk=split(ziv,'.0')
        mnv=str(mnv)
        mnv,junk=split(mnv,'.0')
        fulladd=adv+', '+stv+', ' +ziv
        aomlogot3 = Text(Point(aomw/2+000,500+(25)), "Downloading: "+fulladd)
        
        aomlogot3.draw(win)
        rxp=rx*1.0
        #print rxp%sh.nrows
        a33= rxp/sh.nrows
        a33=format(a33, '.2f')
        a33=str(a33)
        #print a33
        a33=float(a33)
        a34=(a33)*100
        #print 
        if a34%5==0:
            aomlogot4.undraw()
            aomlogot4 = Text(Point(aomw/2+000,500+(-25)), "Percent Done: "+str(a34))
        
            aomlogot4.draw(win)
            
        lat,lon=getcord(fulladd,mnv)
        what='location;#'+mnv+' '+fulladd+';'+lat+';'+lon+';'+adv+';'+ziv+';;;;0000FF\n'
        ttt.write(what)
        
        #raw_input('...')
        aomlogot3.undraw()
        
            
    init2(win,0,0,1,0)
            
def findexcel(win):
    excel=Image(Point(50,70), 'ui/excel.gif')
    excel.draw(win)

    aomw=500
    aomh=720
    opener = GraphWin("open file", aomw, aomh)

    background = Rectangle(Point(0,aomh+2), Point(aomw+2,0))
    background.setFill('white')
    background.draw(opener)


    
    cwd = os.getcwd()
    listx=fnmatch.filter(os.listdir('.'), '*.xls')
    #print listx

    for a in range(13):
        try:
            temp= listx[a]
            if a%2==0:

                background = Rectangle(Point(0,70+(25*int(a))), Point(aomw,95+(25*int(a))))
                background.setFill(color_rgb(250,230,230))
                background.draw(opener)

            
            
            aomlogot = Text(Point(aomw/2,80+(25*int(a))), temp)
            aomlogot.draw(opener)
        except:
            print 'oops'
    flag=0
    found=99
    while flag==0:
        

        z=opener.getMouse()
        x=z.getX()
        y=z.getY()
        print x,y
        if y>400:
            try:
                opener.close()
                return listx[found]
            except:
                ''
        found= int(((y-80)/25))
        aomlogot = Text(Point(aomw/2,500), '...')
        background = Rectangle(Point(50,400), Point(aomw-50,550))
        background.setFill(color_rgb(230,230,230))
        background.draw(opener)
        listx[found]

        aomlogot = Text(Point(aomw/2,450), 'Open')
        aomlogot.draw(opener)
        
        aomlogot = Text(Point(aomw/2,500), listx[found])
        aomlogot.draw(opener)
        #flag=1
        
        if x>0 and x<85 and y >35 and y<135:
            
            print 'goal'
                   
    
    aomlogot = Text(Point(40,025), "Open...")
    aomlogot.draw(opener)

    aomlogot = Text(Point(aomw/2,50), cwd)
    aomlogot.draw(opener)
    
def init():


    win = GraphWin("ui test", aomw, aomh)
    #win.setFill('white')
    print 'poop'




    #ent5=Entry(Point(1100,50),70)
    #ent5.draw(win)
    #entt5 = Text(Point(770,50), "2=")
    #entt5.draw(win)
    return(win)
def helps(win):
    #background = Rectangle(Point(0,aomh+2), Point(aomw+2,0))
    #background.setFill('white')
    #background.draw(win)
    bottomimage=Image(Point(aomw/2,aomh/2), 'ui/help.gif')
    bottomimage.draw(win)
    z=win.getMouse()
    bottomimage.undraw()
    
    



def credit(win):
    background = Rectangle(Point(0,aomh+2), Point(aomw+2,0))
    background.setFill('blue')
    background.draw(win)
    bottomimage=Image(Point(aomw/2,aomh/2), 'ui/quit.gif')
    bottomimage.draw(win)
    z=win.getMouse()
    win.close()

def init2(win,ex,fi,gp,he):
    background = Rectangle(Point(0,aomh+2), Point(aomw+2,0))
    background.setFill('white')
    background.draw(win)
    
    bottomimage=Image(Point(aomw/2,aomh-50), 'ui/bottom2.gif')
    bottomimage.draw(win)

    if ex==1:
        excel=Image(Point(50,70), 'ui/excel.gif')
    else:
        excel=Image(Point(50,70), 'ui/excel20.gif')
    excel.draw(win)

    
    if fi==1:
        filler=Image(Point(50,220), 'ui/filter.gif')
    else:
        filler=Image(Point(50,220), 'ui/filter20.gif')
    filler.draw(win)

    if gp==1:
        
        gps=Image(Point(50,370), 'ui/gps.gif')
    else:
        gps=Image(Point(50,370), 'ui/gps20.gif')
    gps.draw(win)


    if he==1:
        hh=Image(Point(50,520), 'ui/helplogo.gif')
    else:
        hh=Image(Point(50,520), 'ui/helplogo20.gif')
    hh.draw(win)




    aomlogo = Rectangle(Point(0,aomh-100), Point(aomw+1,aomh+1))
    #aomlogo.draw(win)
    aomlogo.setFill('red')

    return win

def editexcel(win,filex,lo,la):


    aomlogot2=Text(Point(600,80+(25*int(1))), '')
    aomlogot2.draw(win)

    aomlogot4=Text(Point(600,80+(25*int(1))), '')
    aomlogot4.draw(win)

    book = xlrd.open_workbook(filex)

    sh = book.sheet_by_index(0)
    #print sh.name, sh.nrows, sh.ncols
    #print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
    flag=0
    excellist=[]
    goodlist=[]
    #raw_input('...')
    listy=['Map Number','Station Name','Address1','State','Zip']

    print sh.ncols
    #book = xlwt.Workbook(filex)
    
    file_path = filex+'.edit.xls'
    rb = open_workbook(filex,formatting_info=True)
    r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
    wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
    w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy
    w_sheet.write(0, sh.ncols, 'longitude')
    w_sheet.write(0, sh.ncols+1, 'latitude')
    for bb in range(1,sh.nrows,1):
        w_sheet.write(bb, sh.ncols, (lo[bb]))
        w_sheet.write(bb, sh.ncols+1, (la[bb]))
    
        
    #longitude and latitude
    wb.save(file_path)

    #workbook.save()
    
    #win.getmouse()

def convert2gif(i):
    

    image = Image2.open(i)


    #image=Image.open(os.path.join(path, fileName))
    for orientation in ExifTags.TAGS.keys() : 
        if ExifTags.TAGS[orientation]=='Orientation' : break 
    exif=dict(image._getexif().items())

    if   exif[orientation] == 3 : 
        image=image.rotate(180, expand=True)
    elif exif[orientation] == 6 : 
        image=image.rotate(270, expand=True)
    elif exif[orientation] == 8 : 
        image=image.rotate(90, expand=True)
    basewidth = aomw/3
    basewidth=int(basewidth)
    
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
        



    
    image = image.resize((basewidth,hsize), Image2.ANTIALIAS)
    image.save('temp/'+i+'.gif','PPM')
def main(win):

    aomlogot = Text(Point(40,125), "Load...")
    aomlogot.draw(win)


    go=1
    print 'ok'
    while go==1:
        z=win.getMouse()
       # print z
        x=z.getX()
        y=z.getY()
        print x,y

        if x>0 and x<85 and y >35 and y<135:
            
            print 'goal'
            #win.close()
            filex=findexcel(win)
            print filex
            aomlogot.undraw()
            aomlogot = Text(Point(40,125), "Loaded")
            #editexcel(win,filex)
            openexcel(win,filex)
            la,lo,add=make_list()
            editexcel(win,filex,la,lo)
            go=findjpg(la,lo,add,win)
        if x>1000 and x<1280 and y >35 and y<135:
            helps(win)
            
            
            
    z=win.getMouse()       
    #credit(win)
def start():

    win=init()
    #size=100,100
    #i= "c:/py/2016/aom/pics/IMG_3397.JPG"




    init2(win,1,0,0,0)
    main(win)






start()











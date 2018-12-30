# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:16:26 2018

@author: slimco
"""


import PyQt5.QtWidgets as wdg
import PyQt5.QtGui as qg
import PyQt5.QtCore as core
from bs4 import BeautifulSoup as bs


import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QLineEdit,QGridLayout)
from PyQt5.QtGui import QFont, QColor  
from PyQt5.QtCore import pyqtSlot
import webbrowser
import urllib3
import urllib.request  

class UTubeObj():
    def __init__(self):
        self.query=''
        self.img_links=[]
        self.title=[]
        self.link=[]
        self.links=[]
    
    
    def Query(self,keyword):
        http=urllib3.PoolManager()
        data=http.request('GET','https://www.youtube.com/results?search_query={}'.format(keyword))
        soup=bs(data.data,'lxml')
        for img in soup.find_all('img'):
            self.link=(img['src'])
            if 'https' in self.link:
                self.img_links.append((img['src'].split('?')[0]))
        for a in soup.find_all('a',dir='ltr'):
            if 'title' in a.attrs and 'http' not in a['title']:
                self.title.append(a['title'])
        
        for link in soup.find_all('a', href=True):
            self.links.append(link['href'])
        

####################################################################################################################################
class UI(QWidget):
    
    def __init__(self,l):
        super().__init__()
        
        self.initUI(l)
        
    
    
    #Button Functions####################################################################    
    @pyqtSlot()
    def onclick(self):
        url='www.youtube.com{}'.format(vids.links[0])
        webbrowser.open(url)
        print('it works')
    
    @pyqtSlot()
    def Search(self):
        
        textboxValue = self.textbox.text()
        global vids
        vids=UTubeObj()
        vids.Query(textboxValue)
        vids.query=textboxValue
        layout=QGridLayout(self)
        
        
        
        for i in range(5):
                                   
            urllib.request.urlretrieve(vids.img_links[i], '{}.jpg'.format(i))
            btn = QPushButton('', self)
            btn.setToolTip('{}'.format(vids.title[i]))
            btn.clicked.connect(self.onclick)
            btn.resize(100,100)
            icon=qg.QIcon('{}.jpg'.format(i))
            btn.setIcon(icon)
            btn.setIconSize(core.QSize(150,150))
            #btn.resize(btn.sizeHint())
            
            layout.addWidget(btn,0,i)
            
    
        
        
        
             
    
        
		
    
   
    
    
        
    #Interface Initialization########################################################################     
    def initUI(self,l):
        
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(750, 750)
        
        search = QPushButton('Search', self)
        search.clicked.connect(self.Search)
        icon=qg.QIcon('C:\\Users\\slimc\\Downloads\\icon.png')
        search.setIcon(icon)
        search.resize(qbtn.sizeHint())
        search.move(60, 50)
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 20)
        self.textbox.resize(200,30)
        self.textbox.setFont(QFont('SansSerif', 15))
        
        #self.setToolTip('This is a <b>QWidget</b> widget')
        
            
        
        self.setGeometry(200, 300, 900  , 900)
        #self.setStyleSheet('background-image: C:\\Users\\slimc\\OneDrive\\Pictures\\4k-Ultra-HD-Wallpapers2.jpg')
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(53,53,53))
        self.setPalette(p)
        self.setWindowTitle('MyYouTube')    
        self.show()
    
    
        
        
        
  

app=wdg.QApplication(sys.argv)
ex=UI(1)          
app.exec_()







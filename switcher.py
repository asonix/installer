#!/usr/bin/env python3
from subprocess import call

def determine_hex(value):
    allowed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    value = value[1:]
    for i in value:
        if i not in allowed:
            return(False)
    return(True)

def find_and_replace_hex(document,values,iterator):
    for i in range(len(document)):
        if document[i].find('#') != -1:
            if determine_hex(document[i][document[i].find('#'):document[i].find('#')+7]):
                index = document[i].find('#')
                begin = document[i][:index]
                rec_doc = [document[i][index+7:]]
                temp = begin + values[iterator]
                result = find_and_replace_hex(rec_doc,values,iterator+1)
                document[i] = temp + str(result[0][0])
                iterator = result[1]
    return([document,iterator])

class ColorsObj(object):
    def __init__(self,choose):
        #creates list of colors to choose from
        colors = ["#2d2d2d","#dedede","#f9f9f9","#aaaaaa",
                  "#d64937","#c09853","#b94a48","#f9f9f9",
                  "#777777","#859d00","#3a87ad","#b57cdd",
                  "#a897cc","#a0b0de","#268bd2","#c7c7c7",
                  "#cccccc","#333333","#f57900","#577382",
                  "#929eb0","#a6a6a6","#000000","#00ff00",
                  "#ff0000","#555555","#24507c","#e5e5e5"]
        
        i3Light =  [ 4, 4, 0, 4, 1,25, 0, 1, 1,25, 0, 1, 4, 1, 2, 1, 1, 0, 1, 4, 4, 1, 4, 1, 4, 1, 1,17, 4, 1,17]
        i3Dark =   [ 4, 4, 1, 4, 0,25, 1, 0, 0,25, 1, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 4, 0, 0, 1, 4, 0, 1]
        i3Matrix = [23,23,22,23,23,23,22,23,23,23,22,23,23,23,22,23,22,23,22,23,22,23,23,22,23,23,22,23,23,22,23]
        i3Hacker = [24,24,22,24,24,24,22,24,24,24,22,24,24,24,22,24,22,24,22,24,22,24,24,22,24,24,22,24,24,22,24]
        
        termTrans =  [ 7, 1, 7, 1, 7, 1, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 3, 1]
        termLight =  [ 0,27, 0, 1, 0, 1, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 0,27]
        termDark =   [ 1, 0, 1, 0, 1, 0, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 2, 0]
        termMatrix = [23,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,22]
        termHacker = [24,22,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,22]
        
        lightbg  = "/home/riley/Pictures/furfaggotry/flora.png"
        darkbg   = "/home/riley/Pictures/furfaggotry/katia_managan.jpg"
        matrixbg = "/home/riley/Pictures/black.png"
        
        self.trans = ""
        
        self.bg = ""
        self.ischeme = []
        self.tscheme = []
        self.tempi = []
        self.tempt = []
        self.border = 2
        self.fading = 0

        if choose[0].lower() == 'l':
            self.trans = "100"
            self.bg = lightbg
            self.tempi = i3Light
            self.tempt = termLight
        elif choose[0].lower() == 'm':
            self.trans = "100"
            self.bg = matrixbg
            self.tempi = i3Matrix
            self.tempt = termMatrix
        elif choose[0].lower() == 'h':
            self.trans = "100"
            self.bg = matrixbg
            self.tempi = i3Hacker
            self.tempt = termHacker
        elif choose[0].lower() == 'd':
            self.trans = "100"
            self.bg = darkbg
            self.tempi = i3Dark
            self.tempt = termDark
        elif choose[0].lower() == 't':
            c2 = input("Light or Dark?\n")
            if c2[0].lower() == 'l':
                self.trans = "0"
                self.bg = lightbg
                self.tempi = i3Light
                self.tempt = termTrans
                self.border = 0
                self.fading = 5
            else:
                self.trans = "0"
                self.bg = darkbg
                self.tempi = i3Dark
                self.tempt = termTrans
                self.border = 0
                self.fading = 5

            
        for i in range(len(self.tempi)):
            self.ischeme.append(colors[self.tempi[i]])
        for i in range(len(self.tempt)):
            self.tscheme.append(colors[self.tempt[i]])

decide = input('What theme would you like to use?\n\
\n\
Options:\n\
>Light Numix\n\
>Dark Numix\n\
>Hacker\n\
>Matrix\n\
>Transparent\n\
\n')

fi3 = open('.i3/config','r')
fterm = open('.Xresources','r')
freread = open('.reread.sh','r')

i3 = fi3.readlines()
term = fterm.readlines()
reread = freread.readlines()

fi3.close()
fterm.close()
freread.close()

colors = ColorsObj(decide)

i3 = find_and_replace_hex(i3,colors.ischeme,0)[0]

term = find_and_replace_hex(term,colors.tscheme,0)[0]

for i in range(len(i3)):
    if i3[i].find('pixel') != -1:
        i3[i] = i3[i].split(' ')
        for j in range(len(i3[i])):
            if i3[i][j] != "new_window" and i3[i][j] != "pixel" and i3[i][j] != "\n" and i3[i][j] != "Window" and i3[i][j] != "#" and i3[i][j] != "" and i3[i][j] != "pixels" and i3[i][j] != "new_float":
                i3[i][j] = str(colors.border)
        if type(i3[i]) != "string":
            i3[i] = ' '.join(i3[i])+'\n'

for i in range(len(term)):
    if term[i].find('fading') != -1:
        term[i] = term[i].split(' ')
        for j in range(len(term[i])):
            if term[i][j] != "*fading:" and term[i][j] != "\n":
                term[i][j] = str(colors.fading)
        if type(term[i]) != "string":
            term[i] = ' '.join(term[i])+'\n'

for i in range(len(term)):
    if term[i].find(']#') != -1:
        term[i] = term[i][:term[i].find('[')]+'['+colors.trans+term[i][term[i].find(']'):]

for j in range(len(reread)):
    if reread[j].find('gsettings') != -1:
        reread[j] = 'gsettings set org.gnome.desktop.background picture-uri "file:///'+colors.bg+'"\n'

fi3 = open('.i3/config','w')
fterm = open('.Xresources','w')
freread = open('.reread.sh','w')

fi3.truncate()
fterm.truncate()
freread.truncate()

fi3.writelines(i3)
fterm.writelines(term)
freread.writelines(reread)

fi3.close()
fterm.close()
freread.close()

call('./.reread.sh',shell=True)

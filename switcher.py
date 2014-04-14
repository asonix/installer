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
                print(document[i])
                result = find_and_replace_hex(rec_doc,values,iterator+1)
                print(document[i])
                document[i] = temp + str(result[0][0])
                iterator = result[1]
    return([document,iterator])

class ColorsObj(object):
    def __init__(self,choose):
        #creates list of colors to choose from
        colors = ["#2d2d2d","#dedede","#f9f9f9","#aaaaaa",
                  "#d64937","#cf7c73","#c6301c","#4c884e",
                  "#777777","#e5a29f","#78b5fe","#b57cdd",
                  "#a897cc","#a0b0de","#9cabdd","#c7c7c7",
                  "#cccccc","#333333","#999999","#577382",
                  "#929eb0","#a6a6a6","#000000","#00ff00",
                  "#ff0000","#444444","#24507c"]
        
        i3Light =  [ 4, 4, 0, 4, 1,25, 0, 1, 1,25, 0, 1, 4, 1, 2, 1, 1, 0, 1, 4, 4, 1, 4, 1, 4, 1, 1,17, 4, 1,17]
        i3Dark =   [ 4, 4, 1, 4, 0,25, 1, 0, 0,25, 1, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 4, 0, 0, 1, 4, 0, 1]
        i3Matrix = [23,23,22,23,23,23,22,23,23,23,22,23,23,23,22,23,22,23,22,23,22,23,23,22,23,23,22,23,23,22,23]
        i3Hacker = [24,24,22,24,24,24,22,24,24,24,22,24,24,24,22,24,22,24,22,24,22,24,24,22,24,24,22,24,24,22,24]
        
        termLight =  [ 0, 1, 0, 1, 0, 1, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 0, 1]
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
        
        for i in range(len(self.tempi)):
            self.ischeme.append(colors[self.tempi[i]])
        for i in range(len(self.tempt)):
            self.tscheme.append(colors[self.tempt[i]])

decide = input('What theme would you like to use?\n\nOptions:\n>Light Numix\n>Dark Numix\n>Hacker\n>Matrix\n\n')

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

for i in range(len(term)):
    if term[i].find(']#') != -1:
        term[i] = term[i][:term[i].find('[')]+'['+colors.trans+term[i][term[i].find(']'):]

for j in range(len(reread)):
    print(reread[j])
    if reread[j].find('gsettings') != -1:
        print('gsettings found')
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

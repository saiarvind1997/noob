with open('text/color.txt','r+') as f :
    with open('text/color_code.txt','w+') as f2:
        for l in f:
            l=(l.strip()).split(",")#used for splitting text into seperate list elements 
            print l
            color_code=['#9400D3','#4B0082','#0000FF','#00FF00','#FFFF00','#FF7F00','#FF0000']
            str=" "
            text=str.join(l)#used for joining list back into a string
            print text
            if l[1]=='Violet':
                f2.write('%s %s\n' % (text,color_code[0]))
            elif l[1]=='Indigo':
                f2.write('%s %s\n' % (text,color_code[1]))
            elif l[1]=='Blue':
                f2.write('%s %s\n' % (text,color_code[2]))
            elif l[1]=='Green':
                f2.write('%s %s\n' % (text,color_code[3]))
            elif l[1]=='Orange':
                f2.write('%s %s\n' % (text,color_code[4]))
            elif l[1]=='Yellow':
                f2.write('%s %s\n' % (text,color_code[5]))
            elif l[1]=='Red':
                f2.write('%s %s\n' % (text,color_code[6]))
        f2.close()
    f.close()
    

         
        




    #myNames = [line.strip() for line in f]
    #for i in myNames:
    # print i

   
   
   
   
   
   



"""
Violet	=	['Violet','#9400D3']	
Indigo	=	['Indigo','#4B0082']	
Blue	=	['Blue','#0000FF']	
Green	=	['Green','#00FF00']	
Yellow	=	['Yellow','#FFFF00']	
Orange	=	['Orange','#FF7F00']	
Red	=	['Red','#FF0000']
color=[Violet,Indigo,Blue,Green,Yellow,Red]
color_code=['#9400D3','#0000FF','#00FF00','#FFFF00','#FF7F00','#FF0000']
"""


import os

dirPath = os.path.dirname(__file__)
f= open(r"{}\try.txt".format(dirPath),"r")
search = []
for each in f:
    search.append(each.strip("\n"))
# print(search)

logs =os.listdir(r"{}\input".format(dirPath))
fo= open(r"{}\output.html".format(dirPath),"w+")
tcount = 0
def matchSearch():
    global tcount
    global x
    for i in logs:
        fi = open(r"{0}\input\{1}".format(dirPath,i), "r")
        fo.write(f"-----{i}----- \n")
        
        matches ={}
        
        for word in search:
            wcount = 0
            
            
            lc = 0
            for line in fi:
                lc+=1
                if line.count(word)!=0:
                    wcount+=1
                    #matches.append(i+ " -> Line no: " + str(lc) + "->" + line.strip("\n"))
                    matches[str(lc)] = "->" + line.strip("\n")
                    #print ("Occurences: "+ str(wcount))
                    tcount= tcount+ wcount
            fi.seek(0)
            
            if(wcount !=0):
                fo.write ((word.strip("\n") + " : "+ str(wcount) +"\n"))
            
        fo.write("\n")  
        for each in matches:
            fo.write(each + matches[each]+ "\n")
            x= (each + "\n")
        fo.write("********************************"+"\n")
  
matchSearch()
fo.write(f"Total Matches: {tcount}")  

            

        
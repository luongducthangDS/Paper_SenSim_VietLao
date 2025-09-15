import io
import glob, os
f_in   = '';
f_out  = ''
f_dict = 'F:\\WORDS_WordNet_And_VCL_ALL_sorted.txt';
f_log  = '';

files =[]
os.chdir("F:\\data")
for file in glob.glob("*.txt"):
    files.append(file)
    



dic = dict({})
f = open(f_dict, 'r',encoding="utf-8")
i=0
for line in f:
    dic.update({line.strip():i})
    i=i+1
f.close()

print("bat dau")

for j in range(len(files)):
    f_in   = 'F:\\data\\'+files[j];
    f_out  = 'F:\\data\\ChuanHoaTheoWordNet\\'+files[j]+'_WordNet_And_VCL.txt'
    f_log  = 'F:\\data\\ChuanHoaTheoWordNet\\ThayThe\\'+files[j]+'_WordNet_And_VCL.txt'

    print(f_in)
    l=[]
    f = open(f_in, 'r',encoding="utf-8")
    for cc in f:
        for c in cc.split(' . '):
            if (c.strip()!=''):
                l.append(c)
    f.close()

    
    f = open(f_out, 'w',encoding="utf-8")

    result =[]
    replated =[]
    num_senten = len(l)
    for i in range(num_senten):
        #if (i%1000==0):
            #print(i, ' of ',num_senten)
        ws=[]    
        s = l[i].lower()
        ws1 = s.split()
        for xy in range(len(ws1)):
            if (len(ws1[xy])>1):
                ws.append(ws1[xy])

        d=""
        t=0
        n=len(ws)
        while (t<n):
            k=1;
            tem=ws[t]
            if(t<n-4):
                if ((ws[t]+"_"+ws[t+1]+"_"+ws[t+2]+"_"+ws[t+3]+"_"+ws[t+4]) in dic):
                    k=5
                    tem=ws[t]+"_"+ws[t+1]+"_"+ws[t+2]+"_"+ws[t+3]+"_"+ws[t+4]
                else:
                    if(t<n-3):
                        if ( (ws[t]+"_"+ws[t+1]+"_"+ws[t+2]+"_"+ws[t+3]) in dic):
                            k=4
                            tem=ws[t]+"_"+ws[t+1]+"_"+ws[t+2]+"_"+ws[t+3] 
                        else:
                            if(t<n-2):
                                if ( (ws[t]+"_"+ws[t+1]+"_"+ws[t+2]) in dic):
                                    k=3
                                    tem=ws[t]+"_"+ws[t+1]+"_"+ws[t+2]
                                else:
                                    if(t<n-1):
                                        if ( (ws[t]+"_"+ws[t+1]) in dic):
                                            k=2
                                            tem=ws[t]+"_"+ws[t+1]   
               
#luu cac tu da thay the
            if (tem!=ws[t]):
                try:
                    vt = replated.index(tem)
                except ValueError:
                    replated.append(tem)
            
            t=t+k
            if (d!=""):
                d=d+" "+ tem;
            else:
                d=tem;
                
        if (d.strip()!=''):
            result.append(d)


    for i in range(len(result)):
        f.write(result[i]+'\n')   
    f.close()

#luu da thay the
    f = open(f_log, 'w',encoding="utf-8")
    for i in range(len(replated)):
        f.write(replated[i]+'\n')   
    f.close()

print('done')

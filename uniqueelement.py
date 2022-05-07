def list(samplelist):
   i=0
   a=[]
   while i<len(samplelist):
      if samplelist[i] not in a:
         a.append(samplelist[i])
      i=i+1
   print(a)
list([1,2,3,3,3,3,4,5])




filepath = 'Prometheus_Unbound_first100_lines.txt'
words = set()
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       current_line=line.strip().lower()
       #https://stackoverflow.com/questions/29418281/attributeerror-object-has-no-attribute-split
       words=[i.split(" ") for i in current_line]
       print words 
       #print current_line.spilt()
       print ("Line {}: {} (words {})".format(cnt, current_line,words)) 
       line = fp.readline()
       cnt += 1
##for w in words:
##   print str(w)

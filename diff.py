# import os
#
# pointer
# 
#
#
print('-|Lets do this!')

mfile_name = raw_input('-|put file name (main): ')
cfile_name = raw_input('-|put file name (compared): ')

#main
mfile = open(str(mfile_name), "r")
#compared
cfile = open(str(cfile_name), "r")
#difference
ufile = open('uniqlist.txt', "w")

#magic
diff_list = list(set(mfile)-set(cfile))  

#show me what you get
print('-|')
print diff_list  
print('-|')

#loopik zalypik
for i in diff_list: 
	ufile.write(str(i))
print('-|finish');

#turn off the light
mfile.close()
cfile.close()
ufile.close()
#
#
#
#
#

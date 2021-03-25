! pip install filesplit

from fsplit.filesplit import Filesplit

fs = Filesplit()
filedir=input("Enter the complete file path")
outdir=input("Enter the complete path of the directory where you want to store the output files")
choice=int(input("Do you want to split the file in \n 1.KB's \n 2.MB's \n 3.GB's \n"))
if(choice == 1):
    x=int(input("Enter the split size for KB split"))
    x=x*1024
elif(choice == 2):
    x=int(input("Enter the split size for MB split"))
    x=x*1024*1024
elif(choice == 3):
    x=int(input("Enter the split size for GB split"))
    x=x*1024*1024*1024
else:
    print("Wrong Input") 
f_size=x
print(f_size)
def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))
    
fs.split(file=filedir, split_size=f_size, output_dir=outdir,  callback=split_cb)

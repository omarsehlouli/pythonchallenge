from PIL import Image
im = Image.open("level7.png")
center=im.size[1]/2 # half-width value
p = im.load()  # list of (R,G,B,A), which can be accessed by p[x,y]
res = [chr(p[4,center][1])] + [chr(p[5+7*i,center][1]) for i in range(90)] # RGB colors from white to black does have the same RGB values , that means R=G=B for every block. Please note that the first block is only 5 pixels, whereas the other 
print(''.join(res)) 

#the commented part below is the actual solution
#print(chr(105)+chr(110)+chr(116)+chr(101)+chr(103)+chr(114)+chr(105)+chr(116)+chr(121)) 


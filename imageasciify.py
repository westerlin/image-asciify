from PIL import Image, ImageFilter
import getopt, sys

defaulttones = [' ','.',':','!','c','o','C','O','8','@']

def createAsciiArt(im_name,cellsW=50,cellsH=30,tones=defaulttones,method=1,reverse=False,contrast=True,filename="print"):
    #Read image
    im = Image.open(im_name)
    bwim = im.convert("L")

    if reverse:
        tones.reverse()

    if method==1:
        cells,qmax,qmin = averageMethod(bwim,cellsW,cellsH)
    else:
        cells,qmax,qmin = scaleMethod(bwim,cellsW,cellsH)

    outputAscii(cells,qmax,qmin,contrast,filename,tones)

def getCellValue(img,cellX,cellY,pixelsPerCellW,pixelsPerCellH):
    cellTone = 0
    for x in range(cellX*pixelsPerCellW,cellX*pixelsPerCellW+pixelsPerCellW-1):
        for y in range(cellY*pixelsPerCellH,cellY*pixelsPerCellH+pixelsPerCellH-1):
            pixel = img.getpixel((x,y))
            cellTone += pixel/256
    return cellTone/(pixelsPerCellH*pixelsPerCellW)

def getCharFromTone(tone,tones):
    toneIdx = int(tone*(len(tones)))
    return tones[toneIdx]

def averageMethod(img, cellsW=50,cellsH=30):
    cells = [[0.0 for x in range(0,cellsH)] for y in range(0,cellsW)]
    qmax = 0
    qmin = 1
    pixelsPerCellW = int((img.width) / cellsW)
    pixelsPerCellH = int((img.height) / cellsH)
    for y in range(0,cellsH):
        for x in range(0,cellsW):
            cells[x][y] = getCellValue(img,x,y, pixelsPerCellW,pixelsPerCellH)
            #if cells[x][y]>=.8:cells[x][y]=0
            if qmax < cells[x][y]: qmax = cells[x][y]
            if qmin > cells[x][y]: qmin = cells[x][y]
    return cells,qmax,qmin

def scaleMethod(qimg,cellsW=50,cellsH=30):
    img = qimg.resize((cellsW,cellsH),Image.ANTIALIAS)
    cells = [[0.0 for x in range(0,cellsH)] for y in range(0,cellsW)]
    qmax = 0
    qmin = 1
    for y in range(0,cellsH):
        for x in range(0,cellsW):
            cells[x][y] = img.getpixel((x,y))/256
            #if cells[x][y]>=.8:cells[x][y]=0
            if qmax < cells[x][y]: qmax = cells[x][y]
            if qmin > cells[x][y]: qmin = cells[x][y]
    return cells,qmax,qmin


def outputAscii(cells,qmax,qmin,contrast=True,filename="print",tones=defaulttones):
    if filename!="print": f = open(filename,"w")
    for y in range(0,len(cells[0])):
        fileline=""
        for x in range(0,len(cells)):
            if contrast: cells[x][y] = (cells[x][y] - qmin) /(qmax-qmin+0.00001)
            fileline += getCharFromTone(cells[x][y],tones)
        if filename=="print":
            print (fileline)
        else:
            f.write(fileline+"\n")
    if filename!="print":
        f.close()

def doTones():
    for tone in range(0,100):
        print(tone,getCharFromTone(tone/100,tones))

def usage():
    print("Ascii Art Creator")
    print("You need to supply one argument for image til ASCII'fied")
    print()
    print(" -c            (Maximizes contrast)")
    print(" -o <filename> (Output file, if omitted it will print)")
    print(" -m            (Use average method, default is scale method)")
    print(" -t <tone>     (Set your own tones a char string from char representing lightest tone to char representing darkest tone)")
    print(" -r            (tones reversed)")
    print(" -x <number>   (width in chars of char image)")
    print(" -y <number>   (height in chars of char image)")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:cmt:rx:y:", ["help","output=","contrast","method","tones=","reverse","width=","height="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    output="print"
    reverse=False
    contrast=False
    tones=defaulttones
    method=2
    width=60
    height=30

    for o, a in opts:
        if  len(args)==0 or o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            if o in ("-o", "--output"):output = a
            if o in ("-r", "--reverse"):reverse = True
            if o in ("-c", "--contrast"):contrast = True
            if o in ("-t", "--tones"):
                for letter in a:
                    tones.append(letter)
            if o in ("-m", "--method"):method = 1
            if o in ("-x", "--width"):width = int(a)
            if o in ("-y", "--height"):height = int(a)

    createAsciiArt(args[0],cellsW=width,cellsH=height,tones=tones,method=method,reverse=reverse,contrast=contrast,filename=output)

main()

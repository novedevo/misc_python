import re, glob, os
lst = []
def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        #title = title[22:]
        #hexa = []
        #hexb = []
        hexa = title[:2]
        hexb = title[2:4]
        #title = title[4:]

        title = (title[4:] + '_' + str(int(hexa,16)) + '_' + str(int(hexb, 16)))
        
        #print(title)
        #lst.append(title)
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % title + ext))

def renamer(files, pattern, replacement):
    for pathname in glob.glob(files):
        basename= os.path.basename(pathname)
        new_filename= re.sub(pattern, replacement, basename)
        if new_filename != basename:
            os.rename(
              pathname,
              os.path.join(os.path.dirname(pathname), new_filename))


rename(r'C:\test', r'*.jpeg', r'%s')
#print(lst)

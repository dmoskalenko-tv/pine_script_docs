import os
import urllib.request
 
def finder():
    names = os.listdir(os.getcwd())
    if ('build' in names):
        fullname = os.path.join(os.getcwd(), 'build/html')
        for root, dirs, files in os.walk(".", topdown = False):
            for name in files:
                if (name.endswith('.html')):
                    print(os.path.join(root, name))
                    f = open(os.path.join(root, name),'r+')
                    my_str = f.read()
                    f.seek(0)
                    my_str = my_str.replace('<a', '<a rel="nofollow" ')
                    f.write(my_str)
            for name in dirs:
                continue
    
            
 
if __name__ == '__main__':
    finder()

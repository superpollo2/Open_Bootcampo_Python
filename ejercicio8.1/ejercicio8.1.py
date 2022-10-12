import os 
def archive(line):
    txt = open('new_archive.txt', 'w')
    for lin in line:
        txt.writelines(f'{lin}\n')
    txt.close()
    
def main():
    line = ['habia', 'una vez', 'una' ,'iguana']
    archive(line)
    
if __name__ == '__main__':
    main() 
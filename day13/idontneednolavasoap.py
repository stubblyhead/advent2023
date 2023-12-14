with open('testcase') as f:
    patterns = f.read().split('\n\n')

def check_horiz(pattern):
    for i in range(len(pattern)-1):
        

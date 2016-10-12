# python main.py 50
import sys
def execute(n):
    a,b = 0,1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()

print('execute...')
sys.path.append(sys.path[0]+"/com/thoughtworks/daimler/otr/leads")
print(sys.path)
if __name__ == "__main__":
    import sys
    print(len(sys.argv))
    print(sys.argv[0])
    if len(sys.argv) > 1 :
        execute(int(sys.argv[1]))

import Lead
Lead.printMySelf()
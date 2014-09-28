#Find the next triangle number that is also pentagonal and hexagonal.
#Answer: 1533776805.0
#author: wubek
    
import datetime

def ntriangle(n):
    return n*(n+1)/2

def npentagonal(n):
    return n*(3*n-1)/2
 
def nhexagonal(n):
    return n*(2*n-1)
    
def solve():
    hex_index = 144
    penta_index = 166
    tr_index = 286
    not_found = True
    
    while not_found:
    
        triangle_number = ntriangle(tr_index)
        tr_index += 1
        penta_number = 0
        hex_number = 0
        
        while triangle_number > penta_number:
            penta_number = npentagonal(penta_index)
            penta_index += 1
        
        while triangle_number > hex_number:
            hex_number = nhexagonal(hex_index)
            hex_index += 1
            
        if triangle_number == penta_number and triangle_number == hex_number:
            print("##Answer:", triangle_number)
            not_found = False
        
        penta_index -= 1
        hex_index -= 1

if __name__ == "__main__":
    timer = datetime.datetime.now()
    solve()
    timer = datetime.datetime.now() - timer
    print("Time:", timer)
   
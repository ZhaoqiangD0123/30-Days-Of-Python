from random import randint

def shuffle_list(lis:list):
    lis_cy = lis.copy()
    lis_random = []
    for i in range(len(lis_cy)):
        lis_random.append(lis_cy.pop(randint(0,len(lis_cy)-1)))
    return lis_random



if __name__ == '__main__':
    lis = ['ad','adf',65,'adfs']
    print(shuffle_list(lis))
    o = []
    o.append(lis.pop(randint(0,len(lis)-1)))
    print(lis)
    print(o)
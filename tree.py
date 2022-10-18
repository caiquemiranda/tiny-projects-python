
# heigth of tree for print
height_tree = int(input('Height of tree : '))


for i in range(1, height_tree + 1):
    
    tree_lentgh = height_tree - i

    print( (tree_lentgh//2) * '-' + i * '*' + (tree_lentgh//2) * '-' )


'''

primeiro -> todos os prints tem que ter o mesmo espaço
segundo  -> os espaços tem que ser divididos com a folha no meio

'''
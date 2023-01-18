def busqueda_binaria (target):
    epsilon = 0.01
    base = 0.0
    top = max(1.0, target)
    answ = (top + base)/2

    while abs(answ**2 - target) >= epsilon:
        print(f'base= {base}, top = {top}, answ= {answ}')
        if answ**2 < target:
            base = answ
        else:
            top = answ
    
        answ = (top + base)/2

    print(f'the square root of {target} is {answ}')
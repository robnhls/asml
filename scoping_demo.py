
top = 100 # global.top


def change_things():

    global top
    func_variable = 500

    def can_i_build_a_function_here():
        nonlocal func_variable = 1000
        pass

    top = 200 # global.top
    print("Top in func", top)






print("First Top", top) # 100
change_things()
print("Second Top", top) # 200


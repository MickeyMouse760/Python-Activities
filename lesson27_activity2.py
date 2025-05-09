class employee():
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Object destructed")
def create_obj():
    obj = employee()
    print("Function is ending")
    return obj
obj = create_obj()
print("Program is ending")
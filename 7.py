class old_eight_grocery:
    def __init__(self):
       self.__information={"数量":8,"商品名称":"mizhi_small_hunberger","price_for_one":8,"amount":88,"amount_left":8} 
    def display(self):
        return self.__information
    def income(self):
        add=(self.__information["amount"]-self.__information["amount_left"])*self.__information["price_for_one"]
        return add
    def setdata(self):
        self.__information["amount_left"]=int(input("剩多少小汉堡"))
hanbao=old_eight_grocery()
hanbao.setdata()
print("\n")
print(hanbao.display())
print("\n")
print("已经卖了",hanbao.income(),"元")
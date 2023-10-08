class laptop:
    price = ""
    processor = ""
    ram = ""
    def hp_laptop(self):
        print ("Comes in budget")
    def lenovo_laptop(self):
        print ("little bit expensive")
    def dell_laptops(self):
        print ("flagship")
hp = laptop()
dell = laptop()
lenovo = laptop()
hp.price = "45K"
dell.price = "75K"
lenovo.price = "1L"
hp.processor = "i3 processer"
dell.processor = "i5 processer"
lenovo.processor = "i7 processer"
hp.ram = "4GB"
dell.ram = "8GB"
lenovo.ram = "16GB"
print ("")
print ("Price of the laptop: ", hp.price)
print ("processor: ", hp.processor)
print ("Size for ram: ", hp.ram)
hp.hp_laptop()
print ("")
print ("Price of the laptop: ", dell.price)
print ("processor: ", dell.processor)
print ("Size for ram: ", dell.ram)
dell.dell_laptops()
print ("")
print ("Price of the laptop: ", lenovo.price)
print ("processor: ", lenovo.processor)
print ("Size for ram: ", lenovo.ram)
lenovo.lenovo_laptop()
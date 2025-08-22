class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model) 
        self.os = os
        self.storage = storage
        
    def phone_details(self):
        return f"Smartphone: {self.device_info()}, OS: {self.os}, Storage: {self.storage}GB"
    
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()}...")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, os, storage, gpu):
        super().__init__(brand, model, os, storage)
        self.gpu = gpu
    
    def phone_details(self):
        return f"Gaming Smartphone: {self.device_info()}, OS: {self.os}, Storage: {self.storage}GB, GPU: {self.gpu}"
    
    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.device_info()} with {self.gpu} GPU!")

#testing the classes
phone1 = Smartphone("Samsung", "Galaxy S24", "Android", 256)
print(phone1.phone_details())
phone1.install_app("WhatsApp")

gaming_phone = GamingSmartphone("Asus", "ROG Phone 8", "Android", 512, "Adreno 750")
print(gaming_phone.phone_details())
gaming_phone.play_game("Call of Duty")

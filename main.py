import customtkinter as tk
import CTkListbox as ltk
import CTkMessagebox as mtk
from PIL import *
import random, time

tk.set_appearance_mode("system")
tk.set_default_color_theme("green")
root = tk.CTk()
root.title("Re-Sourceable")
root.geometry("325x600")
root.resizable(False, False)

#functions

def save():
    if pricebought.get() == "Free":
        priceoffer=100
    else:
        priceoffer=30*int(pricebought.get())/100
        qualitychoice=random.choice(qualitychoose)
        if qualitychoice == "Good Condition":
            priceoffer-=40
        elif qualitychoice == "Fair Condition":
            priceoffer-=80
    with open("save.txt", "a") as file:
        if "@" in selleremail.get() and "." in selleremail.get() and len(sellerphone.get()) == 12 or len(sellerphone.get()) == 10 or len(sellerphone.get()) == 16 or len(sellerphone.get()) == 15 or len(sellerphone.get()) == 17 and "+" in sellerphone.get() and oksell.get()=="Yes":
            done1=mtk.CTkMessagebox(title="Done!",message="Thank you for your service to the Re-Sourceable Community.\nWe will check your product for it's quality after you accept our offer.",icon="check",option_1="Ok")
            if done1.get()=="Ok":
                done2=mtk.CTkMessagebox(title="Offer",message=f"Are you ok with upto ${priceoffer}?",icon="question",option_1="Accept",option_2="Decline")
            if done2.get()=="Accept":
                done3=mtk.CTkMessagebox(title="Sent",message="We have sent a box for you to mail us your product in.",icon="info",option_1="Ok")
            if done3.get() == "Ok":
                done4=mtk.CTkMessagebox(title="Reviewed",message=f"We have reviewed your product. Your product is in {qualitychoice}, therefore you will be getting ${priceoffer}.",icon="info",option_1="Ok")
            if done4.get()=="Ok":
                file.write("\n"+typesell.get()+" "+brandsell.get()+" "+yearsell.get()+" "+oksell.get()+" "+modelsell.get()+" "+pricebought.get()+" "+sellername.get()+" "+selleremail.get()+" "+sellerphone.get())
        else:
            warn = mtk.CTkMessagebox(title="Error!",message="Phone not working or Email or Phone format not correct.",icon="cancel",option_1="Retry")
def load():
    try:
        with open("save.txt", "r") as file:
            products = file.readlines()
            print(products)
            product,brand,year,working,model,name,email,phone=products.split(" ")
            pname=brand+" "+product
            print(pname)
            
            shoplist.insert(tk.END,pname)
                
    except FileNotFoundError:
        pass  # Ignore if the file does not exist

def selltype(selection):
    global typesellget
    typesellget=selection
    if typesellget == "Phone":
        oksell.set("Is the phone working?")
        brandsell.configure(values=["Acer","Amazon","Apple","Blackberry","Blu","Dell","Google","HP","Lenovo","LG","Microsoft","Nokia","Nothing","Oppo","Samsung","Sony","Toshiba","Vodafone","Xiaomi","Other"])
    elif typesellget == "Tablet":
        oksell.set("Is the tablet working?")
        brandsell.configure(values=["Acer","Amazon","Apple","Blackberry","Blu","Dell","Google","HP","Lenovo","LG","Microsoft","Nokia","Oppo","Samsung","Sony","Toshiba","Vodafone","Xiaomi","Other"])
    elif typesellget == "Computer":
        oksell.set("Is the computer working?")
        brandsell.configure(values=["Acer","Alienware","Apple","Asus","Dell","Google","HP","Huawei","LG","Lenovo","Microsoft","Razer","Samsung","Xiaomi","Other"])
    elif typesellget == "SmartWatch":
        oksell.set("Is the watch working?")
        brandsell.configure(values=['Amazfit', 'Apple', 'Casio', 'Diesel', 'Fossil', 'Garmin', 'Garmin Venu', 'Honor', 'Huawei', 'imoo', 'Michael Kors', 'Polar', 'Razer', 'Samsung', 'Skagen', 'Suunto', 'Tag Heuer', 'TicWatch (Mobvoi)', 'Withings', 'Xiaomi',"Other"])
    elif typesellget == "Television":
        oksell.set("Is the TV working?")
        brandsell.configure(values=['LG', 'TCL', 'Samsung', 'Sony', 'Hisense', 'Vizio', 'Panasonic', 'Sharp', 'Philips', 'Toshiba', 'Sanyo', 'Element', 'Westinghouse', 'JVC', 'RCA', 'Insignia', 'Magnavox', 'Pioneer', 'Hitachi', 'Dynex',"Other"])
    elif typesellget == "Home Automation":
        oksell.set("Is the Home Automation product working?")
        brandsell.configure(values=['Amazon Echo', 'Apple HomeKit', 'Ecobee', 'Google Nest', 'Honeywell', 'iRobot Roomba', 'Lutron', 'Nanoleaf', 'Philips Hue', 'Ring', 'Samsung SmartThings', 'Sonos', 'TP-Link Kasa', 'Wink', 'Xiaomi Mi Home',"Other"])
    elif typesellget == "Camera":
        oksell.set("Is the camera working?")
        brandsell.configure(values=['Canon', 'Fujifilm', 'Leica', 'Nikon', 'Olympus', 'Panasonic', 'Pentax', 'Ricoh', 'Samsung', 'Sigma', 'Sony',"Other"])
    elif typesellget == "Kitchen Applinces":
        oksell.set("Is the kitchen applince working?")
        brandsell.configure(values=['Breville', 'Cuisinart', 'Hamilton Beach', 'KitchenAid', 'LG', 'Ninja', 'Panasonic', 'Samsung', 'Smeg', 'Vitamix', 'Whirlpool', 'Black & Decker', "De'Longhi", 'Electrolux', 'GE', 'Instant Pot', 'Kenwood', 'Miele', 'NutriBullet', 'Oster', 'Rowenta', 'SMEG', 'T-fal', 'Viking', 'Zojirushi',"Other"])
    elif typesellget == "Other":
        oksell.set("Is the product working?")
        brandsell.configure(values=["Category is set to ''Other'', Type Category, Brand then Model"])
        modelsell.configure(placeholder_text="Type Category, Brand then Model")

def sellbrand(selection):
    global brandsellget
    brandsellget=selection
    if brandsellget == "Other":
        modelsell.configure(placeholder_text="Type Brand then Model")
        
        
#variables
qualitychoose=["Mint Condition","Good Condition","Fair Condition"]

##topbar
topimg = tk.CTkImage(light_image=Image.open("imgs/topbar.png"),dark_image=Image.open("imgs/topbar.png"),size=(325,76))
toplabel=tk.CTkLabel(root,text="",image=topimg)
toplabel.pack()

#image
iconimg = tk.CTkImage(light_image=Image.open("imgs/icon.png"),dark_image=Image.open("imgs/icon.png"),size=(45,45))
iconlabel=tk.CTkLabel(root,text="",image=iconimg,bg_color="#2FA472")
iconlabel.place(x=30,y=20)

#title
titlelabel = tk.CTkLabel(root, text="Re-Sourceable",font=("freesans",30,"bold"), bg_color="#2FA472")
titlelabel.place(x=100, y=20)

##tabs
tabs=tk.CTkTabview(root,height=500)
tabs.pack(pady=5)

shop=tabs.add("Shop")
sell=tabs.add("Sell")

#shop
typeshop=tk.CTkOptionMenu(shop)
typeshop.set("Select Category")
typeshop.configure(values=["All","Phone","Tablet","Computer","SmartWatch","Television","Home Automation","Camera","Kitchen Applinces","Other"])
typeshop.pack()

shoplist = ltk.CTkListbox(shop,width=250,height=400)
shoplist.pack(pady=5)



#sell
###type
typesell=tk.CTkOptionMenu(sell,command=selltype)
typesell.set("Select Category")
typesell.configure(values=["Phone","Tablet","Computer","SmartWatch","Television","Home Automation","Camera","Kitchen Applinces","Other"])
typesell.pack()

###brand
brandsell=tk.CTkOptionMenu(sell)
brandsell.set("Select Brand")
brandsell.configure(values=["Select Category First!"],command=sellbrand)
brandsell.pack(pady=5)

###year
yearsell=tk.CTkOptionMenu(sell)
yearsell.set("Select Year Bought")
yearsell.configure(values=['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])
yearsell.pack(pady=5)

###ok?
oksell=tk.CTkOptionMenu(sell)
oksell.set("Is the product working?")
oksell.configure(values=["Yes","No"])
oksell.pack(pady=5)

###model
modelsell=tk.CTkEntry(sell,placeholder_text="Model",width=250)
modelsell.pack(pady=5)

###price
pricebought=tk.CTkEntry(sell,placeholder_text="Enter Price Bought (''Free'' if $0)",width=250)
pricebought.pack(pady=5)

###seller info
sellername=tk.CTkEntry(sell,placeholder_text="Enter Seller Name")
selleremail=tk.CTkEntry(sell,placeholder_text="Enter Seller Email")
sellerphone=tk.CTkEntry(sell,placeholder_text="Enter Seller Phone")
sellername.pack(pady=5)
selleremail.pack(pady=5)
sellerphone.pack(pady=5)

###submit
submitbutton=tk.CTkButton(sell,text="Submit to \n Shop",command=save)

submitbutton.pack(pady=20)

# load()
root.mainloop()
def main():
    fruits=[{"name":"Apple","Calories":130},
            {"name":"Avocado","Calories":50},
            {"name":"Banana","Calories":110},
            {"name":"Cantaloupe","Calories":50},
            {"name":"Grapefruit","Calories":60},
            {"name":"Grapes","Calories":90},
            {"name":"Honeydew Melon","Calories":50},
            {"name":"Kiwifruit","Calories":90},
            {"name":"Lemon","Calories":15},
            {"name":"Lime","Calories":20},
            {"name":"Nectarine","Calories":60},
            {"name":"Orange","Calories":80},
            {"name":"Peach","Calories":60},
            {"name":"Pear","Calories":100},
            {"name":"Pineapple","Calories":50},
            {"name":"Plums","Calories":70},
            {"name":'Strawberries',"Calories":50},
            {"name":"Sweet Cherries","Calories":100},
            {"name":"Tangerine","Calories":50},
            {"name":"Watermelon","Calories":80}]  
    fruit=input("Item: ").strip().title()
    x=0
    for next in fruits:
        if fruit==fruits[x]["name"]:
            print("Calories: "+str(fruits[x]["Calories"]))
        x=x+1
    
main()
    
        
        



main()

# Example 1
kenyan = ["smocha","githeri","ugali"]
tanzanian = ["pilau","biryani","viazi"]
ugandan = ["matoke","ngumu","mandizi"]


dish = input("Enter a dish name: ")
if dish in kenyan:
    print("kenyan")
elif dish in tanzanian:
    print("tanzanian")
elif dish in ugandan:
    print("ugandan")
else:
    print("Based on my current knowledge i do not know which dish is",dish)


Example 2
    
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter the city belongs to: ")

if city in india:
    print(f"{city} in india")
elif city in pakistan:
    print(f"{city} in pakistan")
elif city in bangladesh:
    print(f"{city} in bangladesh")

else:
    print("I can't tell which {city} sorry")


city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

if city1 in india and city2 in india:
    print("Both cities are in india")

elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan ")

elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities in bangladesh")

else:
    print("They don't belong to same country")

# Example 3

1. Ask user to enter his fasting sugar level
2. If it is below 80 to 100 range then print that sugar is low
3. If it is above 100 then print that it is high otherwise print that it is norma
sugar = input("Enter fasting sugar level: ")
sugar = float (sugar)

if sugar < 80 :
    print("low sugar level")
elif sugar > 100:
    print("high level sugar")
else: 
    print("normal sugar level")
    




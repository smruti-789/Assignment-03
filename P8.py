total_classes=int(input("Enter no. of classes held:"))
class_attend=int(input("Enter no. of classes attended:"))
percentage=(class_attend/total_classes)*100

if percentage>75:
    print(percentage,"Allowed")
elif percentage<75:
    medical=input("Is medical available:")
    if medical=='Yes' or 'yes' or'YES':
        print(f"{percentage:.2f}Allowed under medical")
    else:
        print(f"{percentage:.2f}Not Allowed")
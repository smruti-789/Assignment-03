total_classes=int(input("Enter no. of classes held:"))
class_attend=int(input("Enter no. of classes attended:"))
percentage=(class_attend/total_classes)*100
if percentage>75:
    print(percentage,"Allowed")
else:
    print(percentage,"Not Allowed")
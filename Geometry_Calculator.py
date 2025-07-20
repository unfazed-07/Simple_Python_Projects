import math

def ap_of_circle(rad):
    area=math.pi*rad**2
    perimeter=2*math.pi*rad
    return area, perimeter

def ap_of_square(side):
    area=side**2
    return area

def ap_of_sphere(rad):
    area=4*math.pi*rad**2
    surface_area=4*math.pi*(rad**2)
    return area, surface_area

def ap_of_cylinder(rad,height):
    area=(math.pi*rad**2)*height
    surface_area=2*math.pi*rad*height
    return area, surface_area

def ap_of_cuboid(l, b, h):
    volume=l*b*h
    surface_area=2*((l*b)+(b*h)+(h*l))
    return volume, surface_area

def ap_of_cone(r,h,l):
    volume=(1/3)*math.pi*(r**2)*h
    slant_height=math.sqrt((r**2)+(h**2))
    lateral_surface_area=math.pi*r*h
    total_surface_area=math.pi*r*l
    base_circumference=2*math.pi*r
    return volume, slant_height, lateral_surface_area, total_surface_area, base_circumference

def handle_circle():
    rad=float(input('Enter radius:'))
    area, peri= ap_of_circle(rad)
    print(f"""Area of Circle is: {area:.2f}
    Perimeter of Circle is: {peri:.2f}""")

def handle_square():
    side=float(input('Enter the side length'))
    area=ap_of_square(side)
    print(f"Area of square is: {area:.2f}")

def handle_sphere():
    rad=float(input('Enter the radius'))
    volume, surface_area=ap_of_sphere(rad)
    print(f"""Area of sphere is: {volume:.2f}
    Surface area of Sphere is: {surface_area:.2f}""")

def handle_cylinder():
    rad=float(input('ENter the radius'))
    height=float(input("ENter the height of cylinder"))
    area, surface_area=ap_of_cylinder(rad, height)
    print(f"""Area of cylinder is: {area:.2f}
    Surface area of Cylinder is: {surface_area:.2f}""")
    
def handle_cuboid():
    l=float(input("Enter Cuboid's length:"))
    b=float(input("Enter cuboid's breadth:"))
    h=float(input("Enter Cuboid's height"))
    vol, surf = ap_of_cuboid(l, b, h)
    print(f"""Volume of Cuboid is: {vol}
    Surface Area of Cuboid is: {surf}""")

def handle_cone():
    r=float(input("Enter the radius of Cone:"))
    h=float(input("Enter the height of Cone:"))
    l=float(input("Enter the length of Cone:"))
    vol, slant_height, lateral_surface_area, total_surface_area, base_circumerence = ap_of_cone(r,h,l)
    print(f"""
    Volume: {round(vol, 2)}
    Slant Height: {round(slant_height, 2)}
    Lateral Surface Area: {round(lateral_surface_area, 2)}
    Total Surface Area: {round(total_surface_area, 2)}
    Base Circumference: {round(base_circumerence, 2)}
    """)
    


def main():
    while True:
        print("Choose any shape whose Area/Volume and Surface Area/Perimeter you want to find.")
        print("1. Circle")
        print("2. Sqaure")
        print("3. Sphere")
        print("4. Cylinder")
        print("5. Cuboid")
        print("6. Cone")
        print("7. Exit")

        try:
            choice=input(" Enter you choice(1-6)")

            if choice=="1":
                handle_circle()
            elif choice=="2":
                handle_square()
            elif choice=="3":
                handle_sphere()
            elif choice=="4":
                handle_cylinder()
            elif choice=="5":
                handle_cuboid()
            elif choice=='6':
                handle_cone()
            elif choice=="7":
                break
        except ValueError:
            print("Invali Input! Enter something valid")

        
main()
from GRAPHICS.GRAPHICS3D import cuboid_module as c
print("\n__To find Area and Perimeter of a rectangle__\n")
l=int(input("Enter the length:"))
b=int(input("\nEnter the breadth:"))
h=int(input("\nEnter the height:"))
print("\nSurface Area:",c.surface_area(l,b,h))
print("\nPerimeter:",c.perimeter(l,b,h))
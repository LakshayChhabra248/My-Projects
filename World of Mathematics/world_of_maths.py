import math

PI = math.pi

MENU_OPTIONS = {
    "1": "basic_operations",
    "2": "square_and_root",
    "3": "shape_calculations",
    "4": "percentage_calculator",
    "5": "quadratic_roots",
    "6": "statistics_natural_numbers",
    "7": "prime_numbers_in_range",
    "8": "result_calculator",
    "9": "unit_conversions",
    "10": "multiplication_table",
    "11": "trigonometric_table",
    "12": "hcf_lcm",
    "13": "classwise_result",
    "0": "quit_program",
}

def basic_operations():
    while True:
        action = input("Press 'S' to start, 'Q' for main menu: ").strip().lower()
        if action == 's':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operator = input("Enter operator (+, -, *, /): ")
                match operator:
                    case '+': print(num1 + num2)
                    case '-': print(num1 - num2)
                    case '*': print(num1 * num2)
                    case '/': print(num1 / num2); print("The Quotient Is ",num1 // num2)
                    case _: print("INVALID OPERATOR!!")
            except ValueError:
                print("Invalid number input. Please enter a number.")
        elif action == 'q':
            break
        else:
            print("Invalid input.")

def square_and_root():
    while True:
        choice = input("For square press 1, for square root press 2, 0 for main menu: ").strip()
        match choice:
            case '1':
                try:
                    num = float(input("Enter the number: "))
                    print(f"The square of {num} is {num**2}")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case '2':
                try:
                    num = float(input("Enter the number: "))
                    print(f"The square root of {num} is {math.sqrt(num)}")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            case '0':
                break
            case _:
                print("Invalid choice.")

def shape_calculations():
        dimension = input("Enter 1 for 2D, 2 for 3D, 0 for main menu : ").strip()
        while dimension != '0':
            match dimension:
                case '1':
                    _2d_shapes()
                    break
                case '2':
                    _3d_shapes()
                    break
                case '0':
                    break
                case _:
                    print("Invalid input.")
                
def _2d_shapes():
    print("2D Shapes: Square, Rectangle, Circle, Parallelogram, Rhombus (h), Triangle")
    shape = input("Enter the first letter of the shape (or 'h' for rhombus): ").strip().lower()
    match shape:
        case 's':
            try:
                side = float(input("Enter side of square: "))
                calc = input("Area or perimeter? ").strip().lower()
                if calc == 'area': print(f"Area of square is {side**2}")
                elif calc == 'perimeter': print(f"Perimeter of square is {4 * side}")
                else: print("Invalid calculation type.")
            except ValueError:
               print("Invalid input")
        case 'r':
            try:
                length = float(input("Enter the length of rectangle: "))
                breadth = float(input("Enter the breadth of rectangle: "))
                calc = input("Area or perimeter? ").strip().lower()
                if calc == 'area': print(f"Area of rectangle is {length * breadth}")
                elif calc == 'perimeter': print(f"Perimeter of rectangle is {2 * (length + breadth)}")
                else: print("Invalid calculation type.")
            except ValueError:
                print("Invalid Input")
        case 'c':
             try:
                radius = float(input("Enter the radius of the circle: "))
                calc = input("Area or circumference? ").strip().lower()
                if calc == 'area': print(f"Area of circle is {PI * radius**2}")
                elif calc == 'circumference': print(f"Circumference of circle is {2 * PI * radius}")
                else: print("Invalid calculation type.")
             except ValueError:
                 print("Invalid input")
        case 'p':
            try:
                height = float(input("Enter the perpendicular length of parallelogram: "))
                length = float(input("Enter the length of parallelogram: "))
                base = float(input("Enter the base of parallelogram: "))
                calc = input("Area or perimeter? ").strip().lower()
                if calc == 'area': print(f"Area of parallelogram is {height * base}")
                elif calc == 'perimeter': print(f"Perimeter of parallelogram is {2 * (length + base)}")
                else: print("Invalid calculation type.")
            except ValueError:
                print("Invalid input.")
        case 'h':
           try:
               calc = input("Area or perimeter? ").strip().lower()
               if calc == 'area':
                   diag1 = float(input("Enter first diagonal: "))
                   diag2 = float(input("Enter second diagonal: "))
                   print(f"Area of rhombus is {0.5 * diag1 * diag2}")
               elif calc == 'perimeter':
                   side = float(input("Enter side of rhombus: "))
                   print(f"Perimeter of rhombus is {4 * side}")
               else:
                   print("Invalid calculation type.")
           except ValueError:
               print("Invalid input")
        case 't':
            try:
                side1 = float(input("Enter side 1 of triangle: "))
                side2 = float(input("Enter side 2 of triangle: "))
                side3 = float(input("Enter side 3 of triangle: "))
                calc = input("Area or perimeter? ").strip().lower()
                if calc == 'area':
                    s = (side1 + side2 + side3) / 2
                    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
                    print(f"Area of triangle is {area}")
                elif calc == 'perimeter':
                    print(f"Perimeter of triangle is {side1 + side2 + side3}")
                else:
                    print("Invalid calculation type.")
            except ValueError:
                print("Invalid Input")
        case _:
            print("Invalid shape.")
            

def _3d_shapes():
    print("3D Shapes: Cube (cu), Cuboid (cd), Cone (cn), Cylinder (cr), Sphere (sr), Hemisphere (hr)")
    shape_code = input("Enter the shape code: ").strip().lower()
    match shape_code:
        case 'cu':
            try:
                side = float(input("Enter the side of the cube: "))
                calc = input("Surface area or volume? ").strip().lower()
                if calc == 'volume': print(f"Volume of cube is {side**3}")
                elif calc == 'surface area':
                   sa_type=input("Lateral or Complete?").strip().lower()
                   if sa_type=='lateral': print(f"Lateral Surface area of cube is {4 * side**2}")
                   elif sa_type=='complete': print(f"Complete Surface area of cube is {6 * side**2}")
                   else :print("Invalid surface area type")
                else: print("Invalid calculation type.")
            except ValueError:
                 print("Invalid input")
        case 'cd':
            try:
                length = float(input("Enter the length of cuboid: "))
                breadth = float(input("Enter the breadth of cuboid: "))
                height = float(input("Enter the height of cuboid: "))
                calc = input("Surface area or volume? ").strip().lower()
                if calc == 'volume': print(f"Volume of cuboid is {length * breadth * height}")
                elif calc == 'surface area':
                    sa_type = input("Lateral or Complete?").strip().lower()
                    if sa_type == 'complete':
                         sa = 2 * ((length * breadth) + (breadth * height) + (length * height))
                         print(f"Complete Surface Area of cuboid is {sa}")
                    elif sa_type == 'lateral':
                         sa=2*height*(length+breadth)
                         print(f"Lateral Surface Area of cuboid is {sa}")
                    else:
                        print("Invalid surface area type")
                else: print("Invalid calculation type.")
            except ValueError:
                 print("Invalid Input")

        case 'cn':
            try:
                radius = float(input("Enter the radius of cone: "))
                height = float(input("Enter the height of cone: "))
                calc = input("Surface area or volume? ").strip().lower()
                if calc == 'volume':
                    volume = PI * radius**2 * (height / 3)
                    print(f"Volume of cone is {volume}")
                elif calc == 'surface area':
                    sa_type = input("Lateral or Complete?").strip().lower()
                    slant_height = math.sqrt(height**2 + radius**2)
                    if sa_type == 'lateral':
                        print(f"Lateral surface area of cone is {PI * radius * slant_height}")
                    elif sa_type == 'complete':
                        print(f"Complete surface area of cone is {PI * radius * (radius + slant_height)}")
                    else:
                        print("Invalid surface area type.")
                else: print("Invalid calculation type.")
            except ValueError:
                print("Invalid Input")
        case 'cr':
            try:
                radius = float(input("Enter the radius of cylinder: "))
                height = float(input("Enter the height of cylinder: "))
                calc = input("Surface area or volume? ").strip().lower()
                if calc == 'volume':
                    volume = PI * radius**2 * height
                    print(f"Volume of cylinder is {volume}")
                elif calc == 'surface area':
                    sa_type = input("Lateral or Complete?").strip().lower()
                    if sa_type == 'lateral':
                        print(f"Lateral surface area of cylinder is {2 * PI * radius * height}")
                    elif sa_type == 'complete':
                        print(f"Complete surface area of cylinder is {2 * PI * radius * (radius + height)}")
                    else:
                        print("Invalid surface area type.")
                else: print("Invalid calculation type.")
            except ValueError:
                print("Invalid input")
        case 'sr':
            try:
                radius = float(input("Enter the radius of sphere: "))
                calc = input("Surface area or volume? ").strip().lower()
                if calc == 'surface area':
                    print(f"Surface area of sphere is {4 * PI * radius**2}")
                elif calc == 'volume':
                    volume = (4/3) * PI * radius**3
                    print(f"Volume of sphere is {volume}")
                else: print("Invalid calculation type.")
            except ValueError:
                print("Invalid Input")
        case 'hr':
           try:
               radius = float(input("Enter the radius of hemisphere: "))
               calc = input("Surface area or volume? ").strip().lower()
               if calc == 'volume':
                   volume = (2 / 3) * PI * radius**3
                   print(f"Volume of hemisphere is {volume}")
               elif calc == 'surface area':
                   sa_type = input("Lateral or Complete? ").strip().lower()
                   if sa_type == 'lateral':
                       print(f"Lateral surface area of hemisphere is {2 * PI * radius**2}")
                   elif sa_type == 'complete':
                       print(f"Complete surface area of hemisphere is {3 * PI * radius**2}")
                   else:
                       print("Invalid surface area type.")
               else:
                   print("Invalid calculation type.")
           except ValueError:
               print("Invalid input.")
        case _:
             print("Invalid code.")

def percentage_calculator():
     while True:
        action = input("Press 'S' to start, 'Q' for main menu: ").strip().lower()
        if action == 's':
            try:
              total=float(input("Enter Total :"))
              obtained=float(input("Enter Obtained : "))
              percentage=(obtained/total)*100
              print(f"Percentage of {obtained} over {total} is {percentage:.2f}%")
            except ValueError:
              print("Invalid Input")
        elif action=='q':
            break
        else:
            print("Invalid Input")

def quadratic_roots():
    while True:
      action = input("Press 'S' to start, 'Q' for main menu: ").strip().lower()
      if action == 's':
          try:
              a = float(input("Enter value of a in ax^2 + bx + c : "))
              b = float(input("Enter value of b in ax^2 + bx + c : "))
              c = float(input("Enter value of c in ax^2 + bx + c : "))

              discriminant = b**2 - 4*a*c
              print(f"Discriminant = {discriminant}")
              if discriminant<0:
                  print("Roots are Imaginary")
              elif discriminant>0:
                print("Roots are Real")
              else:
                  print("Roots are Real and Equal")

              root1 = (-b - math.sqrt(discriminant)) / (2*a)
              root2 = (-b + math.sqrt(discriminant)) / (2*a)
              print(f"Roots of quadratic equation are : \n Root1 = {root1} \n Root2 = {root2}")
          except ValueError:
              print("Invalid input")
      elif action == 'q':
          break
      else:
        print("Invalid input.")

def statistics_natural_numbers():
    while True:
        try:
            limit = int(input("Enter the limit (0 for main menu): "))
            if limit == 0:
                break
            else:
                print(f"1. Find the mean of first {limit} natural numbers")
                print(f"2. Find the variance of first {limit} natural numbers")
                print(f"3. Find the sum of squares of first {limit} natural numbers")
                print(f"4. Find the standard deviation of first {limit} natural numbers")

                choice = int(input("Enter your choice (1, 2, 3, 4): "))
                mean = (limit * (limit + 1)) / 2
                sum_squares = (limit * (limit + 1) * (2 * limit + 1)) / 6
                variance = (sum_squares/limit)-((mean/limit)**2)
                std_dev = math.sqrt(variance)
                match choice:
                    case 1: print(f"Mean is: {mean/limit}")
                    case 2: print(f"Variance is: {variance}")
                    case 3: print(f"Sum of squares is: {sum_squares}")
                    case 4: print(f"Standard deviation is: {std_dev}")
                    case _: print("Invalid Input!!!")
        except ValueError:
            print("Invalid Input")
                
def prime_numbers_in_range():
    while True:
       action = input("Press 'S' to start, 'Q' for main menu: ").strip().lower()
       if action=='s':
           try:
              lower_limit = int(input("Enter lower limit of range: "))
              upper_limit = int(input("Enter upper limit of range: "))
              for num in range(lower_limit,upper_limit+1):
                   if num>1:
                       for i in range(2,int(math.sqrt(num))+1):
                            if(num % i) == 0:
                                break
                       else:
                            print(f"{num} is a Prime No.")
           except ValueError:
               print("Invalid Input")
       elif action=='q':
            break
       else:
           print("Invalid input")


def result_calculator():
    try:
        name = input("Enter your name: ")
        maths = float(input("Enter maths marks: "))
        science = float(input("Enter science marks: "))
        english = float(input("Enter english marks: "))
        hindi = float(input("Enter hindi marks: "))
        social_science = float(input("Enter social science marks: "))

        total = 500
        obtained = maths + science + english + hindi + social_science
        percentage = (obtained / total) * 100

        print(f"{name} got a total of {obtained} marks.")
        print(f"{name} got {percentage:.2f}%")
        _check_performance(percentage)
    except ValueError:
        print("Invalid Input")

def _check_performance(percentage):
    if percentage > 85:
        print("Very Nice")
    else:
        print("Do More Hardwork")
        
def unit_conversions():
    while True:
       print("Unit Conversion for:",
              "\n1. Length (meter)",
              "\n2. Mass (gram)",
              "\n3. Volume (litre)",
              "\n4. Internet units (Bytes)",
              "\n0. for main menu" )
       choice = input("Enter (1, 2, 3, 4, 0): ").strip()
       match choice:
            case '1': _length_conversion()
            case '2': _mass_conversion()
            case '3': _volume_conversion()
            case '4': _data_conversion()
            case '0': break
            case _: print("Invalid choice.")

def _length_conversion():
        print("Converter for length units: ",
              "\nKilometer (Km)",
              "\nHectometer (Hm)",
              "\nDecameter (Dm)",
              "\nmeter (m)",
              "\nDecimeter (dm)",
              "\nCentimeter (Cm)",
              "\nMillimeter (Mm)")
        from_unit = input("Enter the unit you want to convert from : ").strip()
        to_unit= input("Enter the unit you want to convert to : ").strip()
        try:
            value= float(input("Enter the value you want to convert: "))
            conversion_factors = {
            ('Km', 'Hm'): 10, ('Km', 'Dm'): 100, ('Km', 'm'): 1000, ('Km', 'dm'): 10000, ('Km', 'Cm'): 100000, ('Km', 'Mm'): 1000000,
            ('Hm', 'Km'): 0.1, ('Hm', 'Dm'): 10, ('Hm', 'm'): 100, ('Hm', 'dm'): 1000, ('Hm', 'Cm'): 10000, ('Hm', 'Mm'): 100000,
            ('Dm', 'Km'): 0.01, ('Dm', 'Hm'): 0.1, ('Dm', 'm'): 10, ('Dm', 'dm'): 100, ('Dm', 'Cm'): 1000, ('Dm', 'Mm'): 10000,
            ('m', 'Km'): 0.001, ('m', 'Hm'): 0.01, ('m', 'Dm'): 0.1, ('m', 'dm'): 10, ('m', 'Cm'): 100, ('m', 'Mm'): 1000,
            ('dm', 'Km'): 0.0001, ('dm', 'Hm'): 0.001, ('dm', 'Dm'): 0.01, ('dm', 'm'): 0.1, ('dm', 'Cm'): 10, ('dm', 'Mm'): 100,
            ('Cm', 'Km'): 0.00001, ('Cm', 'Hm'): 0.0001, ('Cm', 'Dm'): 0.001, ('Cm', 'm'): 0.01, ('Cm', 'dm'): 0.1, ('Cm', 'Mm'): 10,
            ('Mm', 'Km'): 0.000001, ('Mm', 'Hm'): 0.00001, ('Mm', 'Dm'): 0.0001, ('Mm', 'm'): 0.001, ('Mm', 'dm'): 0.01, ('Mm', 'Cm'): 0.1,
            }
            if (from_unit,to_unit) in conversion_factors:
                converted_value=value* conversion_factors[(from_unit,to_unit)]
                print(f"{value} {from_unit} is {converted_value} {to_unit}")
            else:
                 print("Invalid input. Please check the input.")
        except ValueError:
            print("Invalid Input")
        
def _mass_conversion():
    print("Converter for mass units: ",
      "\nKilogram (Kg)",
      "\nHectogram (Hg)",
      "\nDecagram (Dg)",
      "\nGram (g)",
      "\nDecigram (dg)",
      "\nCentigram (Cg)",
      "\nMilligram (Mg)")
    from_unit=input("Enter the unit you want to convert from :").strip()
    to_unit=input("Enter the unit you want to convert to :").strip()
    try:
        value= float(input("Enter the value you want to convert: "))
        conversion_factors = {
            ('Kg', 'Hg'): 10, ('Kg', 'Dg'): 100, ('Kg', 'g'): 1000, ('Kg', 'dg'): 10000, ('Kg', 'Cg'): 100000, ('Kg', 'Mg'): 1000000,
            ('Hg', 'Kg'): 0.1, ('Hg', 'Dg'): 10, ('Hg', 'g'): 100, ('Hg', 'dg'): 1000, ('Hg', 'Cg'): 10000, ('Hg', 'Mg'): 100000,
            ('Dg', 'Kg'): 0.01, ('Dg', 'Hg'): 0.1, ('Dg', 'g'): 10, ('Dg', 'dg'): 100, ('Dg', 'Cg'): 1000, ('Dg', 'Mg'): 10000,
            ('g', 'Kg'): 0.001, ('g', 'Hg'): 0.01, ('g', 'Dg'): 0.1, ('g', 'dg'): 10, ('g', 'Cg'): 100, ('g', 'Mg'): 1000,
            ('dg', 'Kg'): 0.0001, ('dg', 'Hg'): 0.001, ('dg', 'Dg'): 0.01, ('dg', 'g'): 0.1, ('dg', 'Cg'): 10, ('dg', 'Mg'): 100,
            ('Cg', 'Kg'): 0.00001, ('Cg', 'Hg'): 0.0001, ('Cg', 'Dg'): 0.001, ('Cg', 'g'): 0.01, ('Cg', 'dg'): 0.1, ('Cg', 'Mg'): 10,
            ('Mg', 'Kg'): 0.000001, ('Mg', 'Hg'): 0.00001, ('Mg', 'Dg'): 0.0001, ('Mg', 'g'): 0.001, ('Mg', 'dg'): 0.01, ('Mg', 'Cg'): 0.1,
            }
        if (from_unit,to_unit) in conversion_factors:
             converted_value=value* conversion_factors[(from_unit,to_unit)]
             print(f"{value} {from_unit} is {converted_value} {to_unit}")
        else:
            print("Invalid input. Please check the input.")
    except ValueError:
        print("Invalid Input")
        
def _volume_conversion():
    print("Converter for volume units: ",
      "\nKilolitre (Kl)",
      "\nHectolitre (Hl)",
      "\nDecalitre (Dl)",
      "\nlitre (l)",
      "\nDecilitre (dl)",
      "\nCentilitre (Cl)",
      "\nMillilitre (Ml)")
    from_unit=input("Enter the unit you want to convert from :").strip()
    to_unit=input("Enter the unit you want to convert to :").strip()
    try:
        value= float(input("Enter the value you want to convert: "))
        conversion_factors = {
            ('Kl', 'Hl'): 10, ('Kl', 'Dl'): 100, ('Kl', 'l'): 1000, ('Kl', 'dl'): 10000, ('Kl', 'Cl'): 100000, ('Kl', 'Ml'): 1000000,
            ('Hl', 'Kl'): 0.1, ('Hl', 'Dl'): 10, ('Hl', 'l'): 100, ('Hl', 'dl'): 1000, ('Hl', 'Cl'): 10000, ('Hl', 'Ml'): 100000,
            ('Dl', 'Kl'): 0.01, ('Dl', 'Hl'): 0.1, ('Dl', 'l'): 10, ('Dl', 'dl'): 100, ('Dl', 'Cl'): 1000, ('Dl', 'Ml'): 10000,
            ('l', 'Kl'): 0.001, ('l', 'Hl'): 0.01, ('l', 'Dl'): 0.1, ('l', 'dl'): 10, ('l', 'Cl'): 100, ('l', 'Ml'): 1000,
            ('dl', 'Kl'): 0.0001, ('dl', 'Hl'): 0.001, ('dl', 'Dl'): 0.01, ('dl', 'l'): 0.1, ('dl', 'Cl'): 10, ('dl', 'Ml'): 100,
            ('Cl', 'Kl'): 0.00001, ('Cl', 'Hl'): 0.0001, ('Cl', 'Dl'): 0.001, ('Cl', 'l'): 0.01, ('Cl', 'dl'): 0.1, ('Cl', 'Ml'): 10,
            ('Ml', 'Kl'): 0.000001, ('Ml', 'Hl'): 0.00001, ('Ml', 'Dl'): 0.0001, ('Ml', 'l'): 0.001, ('Ml', 'dl'): 0.01, ('Ml', 'Cl'): 0.1,
            }
        if (from_unit,to_unit) in conversion_factors:
            converted_value=value* conversion_factors[(from_unit,to_unit)]
            print(f"{value} {from_unit} is {converted_value} {to_unit}")
        else:
            print("Invalid input. Please check the input.")
    except ValueError:
        print("Invalid Input")

def _data_conversion():
    while True:
        unit = input("Enter the unit (MB, KB, GB, TB, PB, EB, ZB, YB, or 0 to quit): ").strip()
        if unit == '0':
                break
        try:
            value = float(input("Enter data: "))
            to_unit= input("Enter the unit in which you want to convert the data into : ").strip()
            if unit==to_unit:
                print("Entered the same format.Rewrite.")
            conversion_factors = {
                ('MB', 'KB'): 1024, ('MB', 'GB'): 1/1024, ('MB', 'TB'): 1/(1024**2), ('MB', 'PB'): 1/(1024**3), ('MB', 'EB'): 1/(1024**4), ('MB', 'ZB'): 1/(1024**5), ('MB', 'YB'): 1/(1024**6),
                ('KB', 'MB'): 1/1024, ('KB', 'GB'): 1/(1024**2), ('KB', 'TB'): 1/(1024**3), ('KB', 'PB'): 1/(1024**4), ('KB', 'EB'): 1/(1024**5), ('KB', 'ZB'): 1/(1024**6), ('KB', 'YB'): 1/(1024**7),
                ('GB', 'MB'): 1024, ('GB', 'KB'): 1024**2, ('GB', 'TB'): 1/1024, ('GB', 'PB'): 1/(1024**2), ('GB', 'EB'): 1/(1024**3), ('GB', 'ZB'): 1/(1024**4), ('GB', 'YB'): 1/(1024**5),
                ('TB', 'KB'): 1024**3, ('TB', 'MB'): 1024**2, ('TB', 'GB'): 1024, ('TB', 'PB'): 1/1024, ('TB', 'EB'): 1/(1024**2), ('TB', 'ZB'): 1/(1024**3), ('TB', 'YB'): 1/(1024**4),
                ('PB', 'TB'): 1024, ('PB', 'GB'): 1024**2, ('PB', 'MB'): 1024**3, ('PB', 'KB'): 1024**4, ('PB', 'EB'): 1/1024, ('PB', 'ZB'): 1/(1024**2), ('PB', 'YB'): 1/(1024**3),
                ('EB', 'PB'): 1024, ('EB', 'TB'): 1024**2, ('EB', 'GB'): 1024**3, ('EB', 'MB'): 1024**4, ('EB', 'KB'): 1024**5, ('EB', 'ZB'): 1/1024, ('EB', 'YB'): 1/(1024**2),
                ('ZB', 'EB'): 1024, ('ZB', 'PB'): 1024**2, ('ZB', 'TB'): 1024**3, ('ZB', 'GB'): 1024**4, ('ZB', 'MB'): 1024**5, ('ZB', 'KB'): 1024**6, ('ZB', 'YB'): 1/1024,
                ('YB', 'ZB'): 1024, ('YB', 'EB'): 1024**2, ('YB', 'PB'): 1024**3, ('YB', 'TB'): 1024**4, ('YB', 'GB'): 1024**5, ('YB', 'MB'): 1024**6, ('YB', 'KB'): 1024**7,
            }
            if (unit,to_unit) in conversion_factors:
                converted_value=value* conversion_factors[(unit,to_unit)]
                print(f"{value} {unit} is {converted_value} {to_unit}")
            else:
                 print("Invalid input. Please check the input.")
        except ValueError:
             print("Invalid input")
def multiplication_table():
    while True:
       try:
          num = int(input("Enter the number(0 for main menu): "))
          if num == 0:
              break
          else:
              for i in range(1, 11):
                print(f"{num} X {i} = {num*i}")
       except ValueError:
          print("Invalid input")

def trigonometric_table():
    while True:
        action = input("Press 'S' to start, 'Q' for main menu: ").strip().lower()
        if action == 's':
            func = input("Choose function (sin, cos, tan, cot, sec, cosec): ").strip().lower()
            try:
                degree = int(input("Choose the degree (0, 30, 45, 60, 90): "))
                match (func,degree):
                    case ('sin', 0): print(0)
                    case ('sin', 30): print("1/2")
                    case ('sin', 45): print("1/√2")
                    case ('sin', 60): print("√3/2")
                    case ('sin', 90): print(1)
                    case ('cos', 0): print(1)
                    case ('cos', 30): print("√3/2")
                    case ('cos', 45): print("1/√2")
                    case ('cos', 60): print("1/2")
                    case ('cos', 90): print(-1)
                    case ('cot', 45): print(1)
                    case ('cot', 60): print("1/√3")
                    case ('cot', 90): print(0)
                    case ('sec', 0): print(1)
                    case ('sec', 30): print("2/√3")
                    case ('sec', 45): print("√2")
                    case ('sec', 60): print(2)
                    case ('sec', 90): print("Not defined")
                    case ('cosec', 0): print("Not defined")
                    case ('cosec', 30): print(2)
                    case ('cosec', 45): print("√2")
                    case ('cosec', 60): print("2/√3")
                    case ('cosec', 90): print(1)
                    case _: print("Invalid degree.")

            except ValueError:
                print("Invalid Input")
        elif action == 'q':
           break
        else:
          print("Invalid input.")
def hcf_lcm():
    while True:
        action = input("LCM and HCF of two numbers. 'S' to start, 'E' to exit: ").strip().lower()
        if action == 's':
            choice = input("Enter 1 for LCM, 2 for HCF: ").strip()
            try:
              num1 = int(input("Enter the first number: "))
              num2 = int(input("Enter the second number: "))
              if choice == '1':
                  lcm = max(num1,num2)
                  while True:
                      if lcm % num1 == 0 and lcm % num2 == 0:
                          break
                      else:
                          lcm += 1
                  print(f"LCM = {lcm}")
              elif choice == '2':
                    hcf=min(num1,num2)
                    while True:
                         if num1 % hcf == 0 and num2 % hcf == 0:
                            break
                         else:
                            hcf -=1
                    print(f"HCF = {hcf}")
              else:
                    print("Invalid input")
            except ValueError:
                print("Invalid Input.")
        elif action=='e':
            break
        else:
            print("Invalid input.")
def classwise_result():
    while True:
        action = input("Enter 'S' to Start or 'E' to Exit: ").strip().lower()
        if action == 's':
             name=input("Enter your name : ").strip()
             try:
                 std=int(input("Enter your class : ").strip())
                 if std <=10 and std >1:
                       def result():
                           if percentage>85:
                               print("Very Nice")
                           else:
                               print("Do More Hardwork")
                       print("Enter Subjectwise Marks")
                       maths=int(input("Enter Maths Marks : "))
                       science=int(input("Enter Science Marks : "))
                       english=int(input("Enter English Marks : "))
                       hindi=int(input("Enter Hindi Marks : "))
                       social=int(input("Enter Social science Marks : "))
                       total=500
                       obtained=maths+science+english+hindi+social
                       percentage=(obtained/total)*100
                       print(f"{name} Get Total of {obtained} marks")
                       print(f"{name} Get {percentage:.2f}%")
                       result()
                 elif std >10:
                     stream=input("Enter Your Stream\n1.Science\n2.Commerce\n3.Humanities(arts)\n")
                     if stream == '1':
                        group = input("Enter 1 for PCB (Medical), 2 for PCM (Non-Medical): ").strip()
                        if group == '1':
                           physics=int(input("Enter Physics Marks : "))
                           chemistry=int(input("Enter Chemistry marks : "))
                           biology=int(input("Enter Biology marks : "))
                           english=int(input("Enter English marks : "))
                           additional=int(input("Enter Additional subject Marks :"))
                           total=500
                           obtained=physics+chemistry+biology+english+additional
                           percentage = (obtained/total)*100
                           print(f"{name} got a total of {obtained} marks out of 500")
                           print(f"Percentage is {percentage:.2f}%")
                           if percentage==100:
                               print("You are a brilliant Student")
                           elif percentage>90:
                               print("Very Nice")
                           elif percentage>80:
                               print("Well Done")
                           elif percentage<80:
                               print("Do More Hard work")
                           else:
                               pass
                        elif group == '2':
                            physics=int(input("Enter Physics Marks : "))
                            chemistry=int(input("Enter Chemistry marks : "))
                            maths=int(input("Enter Maths marks : "))
                            english=int(input("Enter English marks : "))
                            additional=int(input("Enter Additional subject Marks :"))
                            total = 500
                            obtained=physics+chemistry+maths+english+additional
                            percentage = (obtained/total)*100
                            print(f"{name} got a total of {obtained} marks out of 500")
                            print(f"Percentage is {percentage:.2f}%")
                            if percentage==100:
                                print("You are a brilliant Student")
                            elif percentage>90:
                                print("Very Nice")
                            elif percentage>80:
                                print("Well Done")
                            elif percentage<80:
                                print("Do More Hard work")
                            else:
                                pass
                        else :
                             print("Invalid Input")
                     elif stream == '2':
                          business = int(input("Enter Business Marks : "))
                          economics = int(input("Enter Economics Marks : "))
                          accounts=int(input("Enter Accounts Marks : "))
                          english = int(input("Enter English Marks : "))
                          additional = int(input("Enter Additional subject Marks : "))
                          total=500
                          obtained = business + economics + accounts + english + additional
                          percentage= (obtained/total)*100
                          print(f"{name} got a total of {obtained} marks out of 500")
                          print(f"Percentage is {percentage:.2f}%")
                          if percentage == 100:
                             print("You are a brilliant Student")
                          elif percentage > 90:
                             print("Very Nice")
                          elif percentage > 80:
                             print("Well Done")
                          elif percentage < 80:
                             print("Do More Hard work")
                          else:
                             pass
                     elif stream == '3':
                          political = int(input("Enter Political Science Marks : "))
                          history = int(input("Enter History Marks: "))
                          english=int(input("Enter English marks : "))
                          hindi=int(input("Enter Hindi Marks : "))
                          additional = int(input("Enter Additional Subject marks : "))
                          total=500
                          obtained = political + history + english + hindi + additional
                          percentage= (obtained/total)*100
                          print(f"{name} got a total of {obtained} marks out of 500")
                          print(f"Percentage is {percentage:.2f}%")
                          if percentage == 100:
                                print("You are a brilliant Student")
                          elif percentage > 90:
                                print("Very Nice")
                          elif percentage > 80:
                                print("Well Done")
                          elif percentage < 80:
                                print("Do More Hard work")
                          else:
                                pass

                     else:
                         print("Invalid Input")
                 else:
                     print("Write Correctly")
             except ValueError:
                 print("Invalid Input")
        elif action == 'e':
             break
        else :
              print("Rewrite Please")


def quit_program():
    print("Thanks for using this program!")


def main():
    print("\tWELCOME TO THE WHOLE MATHEMATICS CALCULATOR")
    name = input("Enter Your name : ")
    while True:
        print("****************************************************************************************************************************************************************")
        print("1.Basic Mathematics Operations(+,-,*,/)")
        print("2.Square And Square Root")
        print("3.Surface Area, Volume , Perimeter, Area Of Every 2D And 3D Shapes")
        print("4.Percentage")
        print("5.Roots Of Quadratic Equations")
        print("6.Statstics Of First n natural Numbers")
        print("7.Prime Numbers Between Given Range")
        print("8.Result Calculator")
        print("9.Units Conversions")
        print("10.Table of any number")
        print("11.Trignometric Table(0,30,45,60,90)")
        print("12. H.C.F And L.C.M Of Any Two Numbers")
        print("13.Classwise result calculator")
        print("0.Quit")
        print("################################################################################")
        choice = input("ENTER YOUR Choice(1,2,3,4,5,6,7,8,9,10,11,12,13,0) : ").strip()
        print("****************************************************************************************************************************************************************")

        if choice in MENU_OPTIONS:
            selected_function = MENU_OPTIONS[choice]
            match selected_function:
                case 'basic_operations': basic_operations()
                case 'square_and_root': square_and_root()
                case 'shape_calculations': shape_calculations()
                case 'percentage_calculator': percentage_calculator()
                case 'quadratic_roots': quadratic_roots()
                case 'statistics_natural_numbers': statistics_natural_numbers()
                case 'prime_numbers_in_range': prime_numbers_in_range()
                case 'result_calculator': result_calculator()
                case 'unit_conversions': unit_conversions()
                case 'multiplication_table': multiplication_table()
                case 'trigonometric_table': trigonometric_table()
                case 'hcf_lcm': hcf_lcm()
                case 'classwise_result': classwise_result()
                case 'quit_program':
                    quit_program()
                    break

        else:
            print("REWRITE PLEASE")
            print("***************************************************************************************************************************************************************")


if __name__ == "__main__":
    main()
                    

# We Are Here To create "THE WHOLE MATHS CALCULATOR
#I hope This Program Will Help you A Lot
import math
print("\tWELCOME TO THE WHOLE MATHEMATICS CALCULATOR")
aq=input("Enter Your name : ")
laksh=0
while laksh<1:
    #Here are The Whole Topics Covered in This Calculator
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
    vb=(input("ENTER YOUR Choice(1,2,3,4,5,6,7,8,9,10,11,12,13,0) : "))
    print("****************************************************************************************************************************************************************")
    if vb=='1':
        #Simple Calculations
        q=0
        while q<1:
             w=input("Press:\n'S'to start\n'q' for main menu\n")
             if w=='s' or w=='S':
                  a=int(input("Enter First No. : "))
                  b=int(input("Enter Second No. : "))
                  c=input("Enter Operator [+,-,*,/] : ")
                  if c=='+':	
                            print(a+b)
                  elif c=='-':
                              print(a-b)
                  elif c=='*':
                              print(a*b)
                  elif c=='/':
                              print(a/b)
                              print("The Quotient Is ",a//b)
                  else :
                        print("INVALID OPERATOR!!")
             elif w=='q' or w=='Q':
                break
             else:
                print("REWRITE PLEASE")
    elif vb=='13':
        st=(input("Enter\n'S' To Start \n'E' to exit\n"))
        qw=0
        while qw<2:
            if st=='s'or st=='S':
            
                    print("-----------------------------------------------------------------------")
                    na=input("Enter Your Name : ")
                    d=int(input("Enter Your Class : "))
                    if d<=10 and d>1:
                        def result():
                            if percentage>85:
                                print("Very Nice")
                            else:
                                print("Do More Hardwork")
                            
                        
                        print("Enter Subjectwise Marks")
                        ai=int(input("Enter Maths Marks : "))
                        bo=int(input("Enter Science Marks : "))
                        cp=int(input("Enter English Marks : "))
                        da=int(input("Enter Hindi Marks : "))
                        es=int(input("Enter Social science Marks : "))
                        sum=ai+bo+cp+da+es
                        total=500
                        percentage=(sum/total)*100
                        print(na,"Get Total of",sum,"marks")
                        print(na,"Get ",percentage,"%")
                        result()
                    elif d>10:
                        q=input("Enter Your Stream\n1.Science\n2.Commerce\n3.Humanities(arts)\n")
                        if q=='1':
                            s=input("Enter \n1.PCB(medical)\n2.PCM(non medical)\n")
                            if s=='1':
                                p=int(input("Enter Physics Marks : "))
                                c=int(input("Enter Chemistry marks : "))
                                b=int(input("Enter Biology marks : "))
                                e=int(input("Enter English marks : "))
                                a=int(input("Enter Additional subject Marks :"))
                                t=p+c+b+a+e
                                per=(t/500)*100
                                print(na,"got a total of",t,"marks out of 500")
                                print("Percentage is",per,"%")
                                if per==100:
                                    print("You are a brilliant Student")
                                elif per>90:
                                    print("Very Nice")
                                elif per>80:
                                    print("Well Done")
                                elif per<80:
                                    print("Do More Hard work")
                                else:
                                    pass
                            elif s=='2':
                                p=int(input("Enter Physics Marks : "))
                                c=int(input("Enter Chemistry marks : "))
                                m=int(input("Enter Maths marks : "))
                                e=int(input("Enter English marks : "))
                                a=int(input("Enter Additional subject Marks :"))
                                t=p+c+m+a+e
                                per=(t/500)*100
                                print(na,"got a total of",t,"marks out of 500")
                                print("Percentage is",per,"%")
                                if per==100:
                                    print("You are a brilliant Student")
                                elif per>90:
                                    print("Very Nice")
                                elif per>80:
                                    print("Well Done")
                                elif per<80:
                                    print("Do More Hard work")
                                else:
                                    pass
                            else:
                                print("Invalid Input!!!")
                        if q=='2':
                            bu=int(input("Enter Business Marks : "))
                            ec=int(input("Enter Economics Marks : "))
                            ac=int(input("Enter Accounts Marks : "))
                            en=int(input("Enter English Marks : "))
                            ad=int(input("Enter Additional subject Marks : "))
                            t=bu+ec+ac+en+ad
                            per=(t/500)*100
                            print(na,"got a total of",t,"marks out of 500")
                            print("Percentage is",per,"%")
                            if per==100:
                                print("You are a brilliant Student")
                            elif per>90:
                                print("Very Nice")
                            elif per>80:
                                print("Well Done")
                            elif per<80:
                                print("Do More Hard work")
                            else:
                                pass
                        if q=='3':
                            ps=int(input("Enter Political Science Marks : "))
                            ht=int(input("Enter History Marks: "))
                            eg=int(input("Enter English marks : "))
                            hi=int(input("Enter Hindi Marks : "))
                            ad=int(input("Enter Additional Subject marks : "))
                            t=ps+ht+eg+hi+ad
                            per=(t/500)*100
                            print(na,"got a total of",t,"marks out of 500")
                            print("Percentage is",per,"%")
                            if per==100:
                                print("You are a brilliant Student")
                            elif per>90:
                                print("Very Nice")
                            elif per>80:
                                print("Well Done")
                            elif per<80:
                                print("Do More Hard work")
                            else:
                                pass
                            



                            

                    else:
                        print("Write Correctly")
            elif st=='e'or st=='E':
                break
            else:
                print("Rewrite Please!!")


    elif vb=='12':
            
            a=input("LCM AND HCF OF TWO NUMBERS\n1.enter s for start the program\n2.enter e for exit the program\n")
            if a=="s"or a=='S':
                a=input("Enter\n1.LCM\n2.HCF\n")
                if a=="1":
                    a=int(input("enter the first number: "))
                    b=int(input("enter the second number: "))
                    if a>b:
                        lcm=a
                    else:
                        lcm=b
                    while True:
                        if lcm%a==0 and lcm%b==0:
                            break
                        else:
                            lcm=lcm+1
                    print("\nLCM=",lcm)
                elif a=="2":
                    a=int(input("enter the first number: "))
                    b=int(input("enter the second number: "))
                    if a>b:
                        hcf=a
                    else:
                        hcf=b
                    while True:
                        if a%hcf==0 and b%hcf==0:
                            break
                        else:
                            hcf=hcf-1
                    print("\nHCF=",hcf)
                print("***************************************************************************************************************************************************************")
            elif a=="e" or a=='E':
                    print("***************************************************************************************************************************************************************")
                    break
            else:
                print("REWRITE PLEASE")
    elif vb=='10':
        #Table of Any number
        for i in range(8):
          n=int(input("Enter the Number(0 for main menu) : "))
          if n==0:
                   break
          for a in range(1,11):
              print(n,"X",a,"=",n*a)
    elif vb=='11':
        #All Trignometric Functions
        for re in range(2):
            hi=input("Press\n'S'.To Start\n'Q'.For Main Menu\n")
            if hi=='s' or hi=='S':
                a=str(input("Choose trignometry function [sin,cos,tan,cot,sec,cosec] : "))
    
                if a=='sin':
                    b=int(input("Choose the degree [0,30,45,60,90] : "))
                    if b==0:
                        print("0")
                    if b==30:
                         print("1/2")
                    elif b==45:
                        print("1/√2")
                    elif b==60:
                        print("√3/2")
                    elif b==90:
                        print("1")
                    else:
                         print("Invalid angle!!!!")
                elif a=='cos':
                    b=int(input("Choose the degree [0,30,45,60,90] : "))
                    if b==0:
                        print("1")
                    if b==30:
                        print("√3/2")
                    elif b==45:
                        print("1/√2")
                    elif b==60:
                        print("1/2")
                    elif b==90:
                        print("0")
                    else:
                         print("Invalid angle!!!!")
                elif a=='tan':
                    b=int(input("Choose the degree [0,30,45,60,90] : "))
                    if b==0:
                        print("0")
                    elif b==30:
                        print("1/√3")
                    elif b==45:
                        print("1")
                    elif b==60:
                        print("√3")
                    elif b==90:
                        print("Not defined")
                    else:
                         print("Invalid angle!!!!")
                elif a=='cot':
                    b=int(input("Choose the degree [0,30,45,60,90] : "))
                    if b==0:
                        print("Not defined")
                    elif b==30:
                        print("√3")
                    elif b==45:
                        print("1")
                    elif b==60:
                        print("1/√3")
                    elif b==90:
                        print("0")
                    else:
                         print("Invalid angle!!!!")
                elif a=='sec':
                    b=int(input("Choose the degree [0,30,45,60,90] : "))
                    if b==0:
                        print("1")
                    elif b==30:
                        print("2/√3")
                    elif b==45:
                        print("√2")
                    elif b==60:
                        print("2")
                    elif b==90:
                        print("Not defined")
                    else:
                         print("Invalid angle!!!!")
                elif a=='cosec':
                    b=int(input("Choose the degree [0,30,45,60,90] : "))
                    if b==0:
                        print("Not defined")
                    elif b==30:
                        print("2")
                    elif b==45:
                        print("√2")
                    elif b==60:
                        print("2/√3")
                    elif b==90:
                        print("1")
                    else:
                         print("Invalid angle!!!!")
                else:
                    print("INVALID FUNCTION!!!!")
            elif hi=='q' or hi=='Q':
                break
            else:
                print("REWRITE PLEASE")
                    


        
          
    elif vb=='3':
        a=input("Enter\n1.2D\n2.3D\n")
        print("****************************************************************************************************************************************************************")
        if a=='1':
            print("The 2D Shapes are Square Rectangle Circle Parallelogram Rhombus Triangle : ")
            print("##For Rhombus type 'h'")
            b=input("Enter The First Digit OF Shape (Small Letter) : ")
            print("****************************************************************************************************************************************************************")
            if b=='s':
                d=int(input("Enter the Side Of Square : "))
                print("****************************************************************************************************************************************************************")
                c=input("Area or Perimeter : ")
                if c=='area':
                    print("The Area of square is",d*d)
                elif c=='perimeter':
                    print("THe Perimeter Of Square is",4*d)
                else:
                    print("Correct Your Spelling")
                    print("****************************************************************************************************************************************************************")
            elif b=='c':
                d=int(input("Enter The radius of circle : "))
                e=input("Area or Circumference : ")
                if e=='area':
                    print("The area of Circle is",22/7*d*d)
                elif e=='circumference':
                    print("The circumference of circle is",22/7*2*d)
                else:
                    print("Correct Your Spelling")
            elif b=='t':
                d=int(input("1st Side of Triangle : "))
                e=int(input("2nd Side of Triangle : "))
                f=int(input("3rd Side of Triangle : "))
                g=input("Area Or Perimerter : ")
                if g=='area':
                    h=(d+e+f)/2
                    i=(h*(h-d)*(h-e)*(h-f))**0.5
                    print("The Area Of Triangle is",i)
                elif g=='perimeter':
                    print("The Perimeter of Triangle is",d+e+f)
                else:
                    print("Correct Your Spelling")
            elif b=='r':
                d=int(input("Enter The Length Of Rectangle : "))
                e=int(input("Enter The Breadth Of Rectangle : "))
                f=input("Area or Perimeter : ")
                if f=='area':
                    print("The Area Of Rectangle is",d*e)
                elif f=='perimeter':
                    print("The Perimeter Of Rectangle is",2*(d+e))
                else:
                    print("Correct Your Spelling")
            elif b=='p':
                d=int(input("Enter The Perpendicular length : "))
                g=int(input("Enter Length Of Parallelogram : "))
                e=int(input("Enter The Base lentgh : "))
                f=input("Area or Perimeter : ")
                if f=='area':
                    print("The Area of //gm is",d*e)
                elif f=='perimeter':
                    print("The Perimeter of //gm is",2*(g+e))
                else:
                    print("Correct Your Spelling")
            elif b=='h':
                d=input("Area or Perimeter ; ")
                if d=='area':
                    e=int(input("Enter the 1st Diagonal : "))
                    f=int(input("Enter the 2nd Diagonal : "))
                    print("The Area Of Rhombus is",(1/2)*e*f)
                elif d=='perimeter':
                    e=int(input("Enter The Side Of Rhombus : "))
                    print("The Perimeter of Rhombus is",4*e)
                else:
                    print("Correct Your Spelling")
            else:
                print(b,"is not a 2D shape")
        elif a=='2':
            print("THE 3D Shapes Are Cube Cuboid Cone Cylinder Sphere Hemisphere")
            print("Codes For Shapes To Enter : ",
              "\nCube='cu'",
              "\ncuboid='cd'",
              "\nCone='cn'",
              "\nCylinder='cr'",
              "\nSphere='sr'",
              "\nHemisphere='hr'")
            b=input("Enter The Code Of Shape : ")
            if b=='cu':
                c=int(input("Enter The Side OF Cube : "))
                d=input("Surface Area Or Volume : ")
                if d=='volume':
                    print("Volume OF Cube is",c**3)
                elif d=='surface area':
                    e=input("Lateral or Complete : ")
                    if e=='lateral':
                        print("The Latreal Surface of Cube is",4*c*c)
                    elif e=='complete':
                        print("The Complete Surface Area Of cube is",6*c*c)
                    else:
                        print("Correct Your Spelling")
                else:
                    print("Correct Your Spelling")
            elif b=='cd':
                c=int(input("Enter The Length Of Cuboid : "))
                d=int(input("Enter The Breadth Of Cuboid : "))
                e=int(input("Enter The Height of Cuboid : "))
                f=input("Surface Area or Volume : ")
                if f=='volume':
                    print("The Volume Of Cuboid is",c*d*e)
                elif f=='surface area':
                    g=input("Lateral Or Complete : ")
                    if g=='complete':
                        h=2*((c*d)+(d*e)+(c*d))
                        print("The Lateral Surface Area Of Cuboid Is",h)
                    elif g=='lateral':
                        h=2*e*(c+d)
                        print("The Complete Surface Area is",h)
                    else:
                        print("Correct Your Spelling")
                else:
                    print("Correct Your Spelling")
            elif b=='cn':
                d=int(input("Enter The Radius of Base Of cone : "))
                e=int(input("Enter The Height Of Cone : "))
                f=input("Surface area or Volume : ")
                if f=='volume':
                    g=(22/7)*d*d*(e/3)
                    print("The Volume Of Cone Is",g)
                elif f=='surface area':
                    g=input("lateral or Complete : ")
                    if g=='lateral':
                        h=(22/7)*d*((e*e)+(d*d))**0.5
                        print("The Lateral Surface Of Cone is",h)
                    elif g=='complete':
                        h=(22/7)*d*(d+((e*e)+(d*d))**0.5)
                        print("The Complete Surface Area Of Cone is",h)
                    else:
                        print("Correct Your Spelling")
                else:
                    print("Correct Your Speling")
            elif b=='cr':
                d=int(input("Enter The Radius Of Cylinder : "))
                e=int(input("Enter The Height Of cylinder : "))
                f=input("Surface Area Or Volume : ")
                if f=='volume':
                    h=(22/7)*d*d*e
                    print("The Volume OF Cylinder is",h)
                elif f=='surface area':
                    g=input("Lateral Or Complete : ")
                    if g=='lateral':
                        h=2*(22/7)*d*e
                        print("The Lateral Surface Area Of Cylinder is",h)
                    elif g=='complete':
                        h=2*(22/7)*d*(d+e)
                        print("The Complete Surface Area Of Cylinder is",h)
                    else:
                        print("Correct Your Spelling")
                else:
                    print("Correct Your Spelling")
            elif b=='sr':
                d=int(input("Enter The Radius of Sphere : "))
                e=input("Surface area or Volume : ")
                if e=='surface area':
                    print("The Surface Area Of sphere is",4*(22/7)*d*d)
                elif e=='volume' or 'Volume':
                    f=(4/3)*(22/7)*d*d*d
                    print("The Volume Of Sphere is",f)
                else:
                    print("Correct Your Spelling")
            elif b=='hr':
                d=int(input("Enter The Radius Of Hemisphere : "))
                e=input("Surface Area Or Volume : ")
                if e=='volume' or 'Volume':
                    f=(2/3)*(22/7)*d*d*d
                    print("The Volume of Hemisphere is",f)
                elif e=='surface area':
                    f=input("Lateral or Complete : ")
                    if f=='lateral':
                        g=2*(22/7)*d*d
                        print("The Lateral Surface Area OF hemispher is",g)
                    elif f=='complete':
                        g=3*(22/7)*d*d
                        print("The complete Surface Area of Hemisphere is",g)
                    else:
                        print("Correct Your Spelling")
                else:
                    print("Correct Your Speling")
            else:
                print("Check Your Code")
    elif vb=='5':
        dl=0
        while dl<1:
            ee=input("PRESS\n's'To Start\n'q'For Main Menu\n")
            if ee=='s' or ee=='S':
                def Roots():
                    print("Have A Nice Day. \n Time To Say Good Bye")
                print("Hello Friends \nLet's Find the Root Of Quadratic Equation")
                print("Enter The Value Of a,b,c In ax2+bx+c")
                a=int(input("Enter the value Of a : "))
                b=int(input("Enter the value Of b : "))
                c=int(input("Enter the value Of c : "))
                d=(b**2)-(4*a*c)
                print("Discriminant = ",d)
                if d<0:
                    print("Roots Are Imaginary")
                elif d>0:
                    print("Roots Are Real")
                else :
                    print("Roots Are Real And Equal")
                Root1=(-b-(d**0.5))/(2*a)
                Root2=(-b+(d**0.5))/(2*a)
                print("Root Of The Quadratic Equations are: \n Root1=",Root1,"\n Root2=",Root2)
                Roots()
            elif ee=='q' or ee=='Q':
                break
            else:
                print("REWRITE PLEASE")
    elif vb=='7':
        e=0
        while e<1:
            d=(input("'s' To Start\n'q' For Main menu\n"))
            if d=='s' or d=='S':
                x=int(input("Enter Lower Limit Of range : "))
                y=int(input("Enter higher Limit Of range : "))
                o=[]
                for a in range(x,y):
                    for b in range(2,a):
                        v=a%b
                        if v==0:
                            j=a/b
                            o.append(a)
                            
                            break
                        
                            
                    else:
                            print(a,"is a Prime No.")
            elif d=='q'or d=='Q':
                break
            else:
                print("REWRITE PLEASE")

            
    elif vb=='6':
        for dd in range(10):
            n=int(input("Enter The Limit(0 For Main Menu) : "))
            if n==0:
                break
            else:
                print("1. Find the Mean Of First",n,"natural numbers")
                print("2. Find The Varience of First",n,"natural numbers")
                print("3. Find The Sum Of Square of First",n,"natural numbers")
                print("4. Find The Standard Deviation of",n,"natural numbers")
                c=int(input("ENTER YOUR CHOICE (1,2,3,4): "))
                mean=(n*(n+1))/2
                square=(n*(n+1)*((2*n)-1))/6
                variance=(n*(mean)*(square))/n
                sd=(variance)**0.5
                if c==1:
                    print("Your Mean is",mean)
                elif c==3:
                    print("Your Sum of Square of",n,"natural Numbers is",square)
                elif c==2:
                    print("Varinace of First",n,"Natural Numbers is",variance)
                elif c==4:
                    print("Standard Deviation of first",n,"natural Numbers is",sd)
                else:
                    print("INVALID INPUT!!!!")

                pass
    elif vb=='8':
        def result():
            if percentage>85:
                print("Very Nice")
            else:
                print("Do More Hardwork")
        
        name=str(input("Enter Your Name : "))
        print("Enter Subjectwise Marks")
        ai=int(input("Enter Maths Marks : "))
        bo=int(input("Enter Science Marks : "))
        cp=int(input("Enter English Marks : "))
        da=int(input("Enter Hindi Marks : "))
        es=int(input("Enter Social science Marks : "))
        sum=ai+bo+cp+da+es
        total=500
        percentage=(sum/total)*100
        print(name,"Get Total of",sum,"marks")
        print(name,"Get ",percentage,"%")
        result()
    elif vb=='4':
        for fh in range(4):
            zx=input("Press\n'S'To Start\n'Q'.For Main Menu\n")
            if zx=='s' or zx=='S':
                
                ss=int(input("Enter Total :"))
                sd=int(input("Enter Obtained : "))
                p=(sd/ss)*100
                print("Percentage of",sd,"over",ss,"is",p,"%")
            elif zx=='q' or zx=='Q':
                break
            else:
                print("REWRITE PLEASE")
    elif vb=='9':
        print("Unit Conversion for :",
              "\n1.Length(meter)",
              "\n2.Mass(gram)",
              "\n3.Volume(litre)",
              "\n4.Internet units(Bytes)")
        cv=input("Enter (1,2,3,4) : ")
        if cv=='1':
            print("Converter For Length Units :-",
                  "\nKilometer = Km",
                  "\nHectometer = Hm",
                  "\nDecameter = Dm",
                  "\nmeter = m",
                  "\nDecimeter = dm",
                  "\nCentimeter = Cm",
                  "\nMilimeter = Mm")
            a=input("Enter The  Unit AS mentioned Above : ")
            if a=='Km':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='Hm':
                    d=c*10
                    print(c,"Km is",d,"Hm")
                elif b=='Dm':
                        d=c*100
                        print(c,"Km is",d,"Dm")
                elif b=='m':
                            d=c*1000
                            print(c,"Km is",d,"m")
                elif b=='dm':
                                d=c*10000
                                print(c,"Km is",d,"dm")
                elif  b=='Cm':
                                    d=c*100000
                                    print(c,"Km is",d,"Cm")
                elif b=='Mm':
                                        d=c*1000000
                                        print(c,"Km is",d,"Mm")
                else:
                    print("CHECK YOUR CODE AND WRITE AGAIN!!!!!")
            elif a=='Hm':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='Dm':
                    d=c*10
                    print(c,"Hm is",d,"Dm")
                elif b=='m':
                    d=c*100
                    print(c,"Hm is",d,"m")
                elif b=='dm':
                    d=c*1000
                    print(c,"Hm is",d,"dm")
                elif b=='Cm':
                    d=c*10000
                    print(c,"Hm is",d,"Cm")
                elif b=='Mm':
                    d=c*100000
                    print(c,"Hm is",d,"Mm")
                elif b=='Km':
                    d=c/10
                    print(c,"Hm is",d,"Km")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AmAIN!!!!!!")
            elif a=='Dm':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='m':
                    d=c*10
                    print(c,"Dm is",d,"m")
                elif b=='dm':
                    d=c*100
                    print(c,"Dm is",d,"dm")
                elif b=='Cm':
                    d=c*1000
                    print(c,"Dm is",d,"Cm")
                elif b=='Mm':
                    d=c*10000
                    print(c,"Dm is",d,"Mm")
                elif b=='Km':
                    d=c/100
                    print(c,"Dm is",d,"Km")
                elif b=='Hm':
                    d=c/10
                    print(c,"Dm is",d,"Hm")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='m':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='dm':
                     d=c*10
                     print(c,"m is",d,"dm")
                elif b=='Cm':
                    d=c*100
                    print(c,"m is",d,"Cm")
                elif b=='Mm':
                    d=c*1000
                    print(c,"m is",d,"Mm")
                elif b=='Km':
                    d=c/1000
                    print(c,"m is",d,"Km")
                elif b=='Hm':
                    d=c/100
                    print(c,"m is",d,"Hm")
                elif b=='Dm':
                    d=c/10
                    print(c,"m is",d,"Dm")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
       
    


    
            elif a=='dm':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='Cm':
                    d=c*10
                    print(c,"dm is",d,"Cm")
                elif b=='Mm':
                    d=c*100
                    print(c,"dm is",d,"Mm")
                elif b=='Km':
                    d=c/10000
                    print(c,"dm is",d,"Km")
                elif b=='Hm':
                    d=c/1000
                    print(c,"dm is",d,"Hm")
                elif b=='Dm':
                    d=c/100
                    print(c,"dm is",d,"Dm")
                elif b=='m':
                    d=c/10
                    print(c,"dm is",d,"m")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AmAIN!!!!!!")
            elif a=='Cm':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='Mm':
                    d=c*10
                    print(c,"Cm is",d,"Mm")
                elif b=='Km':
                    d=c/100000
                    print(c,"Cm is",d,"Km")
                elif b=='Hm':
                    d=c/10000
                    print(c,"Cm is",d,"Hm")
                elif b=='Dm':
                    d=c/1000
                    print(c,"Cm is",d,"Dm")
                elif b=='m':
                    d=c/100
                    print(c,"Cm is",d,"m")
                elif b=='dm':
                    d=c/10
                    print(c,"Cm is",d,"dm")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='Mm':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The length   : "))
                if b=='Km':
                    d=c/1000000
                    print(c,"Mm is",d,"Km")
                elif b=='Hm':
                    d=c/100000
                    print(c,"Mm is",d,"Hm")
                elif b=='Dm':
                    d=c/10000
                    print(c,"Mm is",d,"Dm")
                elif b=='m':
                    d=c/1000
                    print(c,"Mm is",d,"m")
                elif b=='dm':
                    d=c/100
                    print(c,"Mm is",d,"dm")
                elif b=='Cm':
                    print(c,"Mm is",d,"Cm")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")

            else:
                 print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
        elif cv=='2':
            print("Converter For Mass Units :-",
      "\nKilogram = Kg",
      "\nHectogram = Hg",
      "\nDecagram = Dg",
      "\nGram = g",
      "\nDecigram = dg",
      "\nCentigram = Cg",
      "\nMiligram = Mg")
      
            a=input("Enter The Mass Unit AS mentioned Above : ")
            if a=='Kg':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='Hg':
                    d=c*10
                    print(c,"Kg is",d,"Hg")
                elif b=='Dg':
                    d=c*100
                    print(c,"Kg is",d,"Dg")
                elif b=='g':
                    d=c*1000
                    print(c,"Kg is",d,"g")
                elif b=='dg':
                    d=c*10000
                    print(c,"Kg is",d,"dg")
                elif  b=='Cg':
                    d=c*100000
                    print(c,"Kg is",d,"Cg")
                elif b=='Mg':
                    d=c*1000000
                    print(c,"Kg is",d,"Mg")

                else:
                    print("CHECK YOUR CODE AND WRITE AGAIN!!!!!")
            elif a=='Hg':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='Dg':
                    d=c*10
                    print(c,"Hg is",d,"Dg")
                elif b=='g':
                    d=c*100
                    print(c,"Hg is",d,"g")
                elif b=='dg':
                    d=c*1000
                    print(c,"Hg is",d,"dg")
                elif b=='Cg':
                    d=c*10000
                    print(c,"Hg is",d,"Cg")
                elif b=='Mg':
                    d=c*100000
                    print(c,"Hg is",d,"Mg")
                elif b=='Kg':
                    d=c/10
                    print(c,"Hg is",d,"Kg")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='Dg':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='g':
                    d=c*10
                    print(c,"Dg is",d,"g")
                elif b=='dg':
                    d=c*100
                    print(c,"Dg is",d,"dg")
                elif b=='Cg':
                    d=c*1000
                    print(c,"Dg is",d,"Cg")
                elif b=='Mg':
                    d=c*10000
                    print(c,"Dg is",d,"Mg")
                elif b=='Kg':
                    d=c/100
                    print(c,"Dg is",d,"Kg")
                elif b=='Hg':
                    d=c/10
                    print(c,"Dg is",d,"Hg")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='g':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='dg':
                    d=c*10
                    print(c,"g is",d,"dg")
                elif b=='Cg':
                    d=c*100
                    print(c,"g is",d,"Cg")
                elif b=='Mg':
                    d=c*1000
                    print(c,"g is",d,"Mg")
                elif b=='Kg':
                    d=c/1000
                    print(c,"g is",d,"Kg")
                elif b=='Hg':
                    d=c/100
                    print(c,"g is",d,"Hg")
                elif b=='Dg':
                    d=c/10
                    print(c,"g is",d,"Dg")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='dg':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='Cg':
                    d=c*10
                    print(c,"dg is",d,"Cg")
                elif b=='Mg':
                    d=c*100
                    print(c,"dg is",d,"Mg")
                elif b=='Kg':
                    d=c/10000
                    print(c,"dg is",d,"Kg")
                elif b=='Hg':
                    d=c/1000
                    print(c,"dg is",d,"Hg")
                elif b=='Dg':
                    d=c/100
                    print(c,"dg is",d,"Dg")
                elif b=='g':
                    d=c/10
                    print(c,"dg is",d,"g")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='Cg':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='Mg':
                    d=c*10
                    print(c,"Cg is",d,"Mg")
                elif b=='Kg':
                    d=c/100000
                    print(c,"Cg is",d,"Kg")
                elif b=='Hg':
                    d=c/10000
                    print(c,"Cg is",d,"Hg")
                elif b=='Dg':
                    d=c/1000
                    print(c,"Cg is",d,"Dg")
                elif b=='g':
                    d=c/100
                    print(c,"Cg is",d,"g")
                elif b=='dg':
                    d=c/10
                    print(c,"Cg is",d,"dg")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='Mg':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The mass Amount : "))
                if b=='Kg':
                    d=c/1000000
                    print(c,"Mg is",d,"Kg")
                elif b=='Hg':
                    d=c/100000
                    print(c,"Mg is",d,"Hg")
                elif b=='Dg':
                    d=c/10000
                    print(c,"Mg is",d,"Dg")
                elif b=='g':
                    d=c/1000
                    print(c,"Mg is",d,"g")
                elif b=='dg':
                    d=c/100
                    print(c,"Mg is",d,"dg")
                elif b=='Cg':
                    print(c,"Mg is",d,"Cg")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")

            else:
                 print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
        elif cv=='3':
            print("Converter For volume Units :-",
      "\nKilolitre = Kl",
      "\nHectolitre = Hl",
      "\nDecalitre = Dl",
      "\nlitre = l",
      "\nDecilitre = dl",
      "\nCentilitre = Cl",
      "\nMililitre = Ml")
      
            a=input("Enter The  Unit AS mentioned Above : ")
            if a=='Kl':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='Hl':
                    d=c*10
                    print(c,"Km is",d,"Hl")
                elif b=='Dl':
                    d=c*100
                    print(c,"Kl is",d,"Dl")
                elif b=='l':
                    d=c*1000
                    print(c,"Kl is",d,"l")
                elif b=='dl':
                    d=c*10000
                    print(c,"Kl is",d,"dl")
                elif  b=='Cl':
                    d=c*100000
                    print(c,"Kl is",d,"Cl")
                elif b=='Ml':
                    d=c*1000000
                    print(c,"Kl is",d,"Ml")

                else:
                    print("CHECK YOUR CODE AND WRITE AGAIN!!!!!")
            elif a=='Hl':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='Dl':
                    d=c*10
                    print(c,"Hl is",d,"Dl")
                elif b=='l':
                    d=c*100
                    print(c,"Hl is",d,"l")
                elif b=='dl':
                    d=c*1000
                    print(c,"Hl is",d,"dl")
                elif b=='Cl':
                    d=c*10000
                    print(c,"Hl is",d,"Cl")
                elif b=='Ml':
                    d=c*100000
                    print(c,"Hl is",d,"Ml")
                elif b=='Kl':
                    d=c/10
                    print(c,"Hl is",d,"Kl")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AgAIN!!!!!!")
            elif a=='Dl':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='m':
                    d=c*10
                    print(c,"Dl is",d,"l")
                elif b=='dl':
                    d=c*100
                    print(c,"Dl is",d,"dl")
                elif b=='Cl':
                    d=c*1000
                    print(c,"Dl is",d,"Cl")
                elif b=='Ml':
                    d=c*10000
                    print(c,"Dl is",d,"Ml")
                elif b=='Kl':
                    d=c/100
                    print(c,"Dl is",d,"Kl")
                elif b=='Hl':
                    d=c/10
                    print(c,"Dl is",d,"Hl")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='l':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='dl':
                    d=c*10
                    print(c,"l is",d,"dl")
                elif b=='Cl':
                    d=c*100
                    print(c,"l is",d,"Cl")
                elif b=='Ml':
                    d=c*1000
                    print(c,"l is",d,"Ml")
                elif b=='Kl':
                    d=c/1000
                    print(c,"l is",d,"Kl")
                elif b=='Hl':
                    d=c/100
                    print(c,"l is",d,"Hl")
                elif b=='Dl':
                    d=c/10
                    print(c,"l is",d,"Dl")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='dl':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='Cl':
                    d=c*10
                    print(c,"dl is",d,"Cl")
                elif b=='Ml':
                    d=c*100
                    print(c,"dl is",d,"ll")
                elif b=='Kl':
                    d=c/10000
                    print(c,"dl is",d,"Kl")
                elif b=='Hl':
                    d=c/1000
                    print(c,"dl is",d,"Hl")
                elif b=='Dl':
                    d=c/100
                    print(c,"dl is",d,"Dl")
                elif b=='l':
                    d=c/10
                    print(c,"dl is",d,"l")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AgAIN!!!!!!")
            elif a=='Cl':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='Ml':
                    d=c*10
                    print(c,"Cl is",d,"Ml")
                elif b=='Kl':
                    d=c/100000
                    print(c,"Cl is",d,"Kl")
                elif b=='Hl':
                    d=c/10000
                    print(c,"Cl is",d,"Hl")
                elif b=='Dl':
                    d=c/1000
                    print(c,"Cl is",d,"Dl")
                elif b=='l':
                    d=c/100
                    print(c,"Cl is",d,"l")
                elif b=='dl':
                    d=c/10
                    print(c,"Cl is",d,"dl")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
            elif a=='Ml':
                b=input("Enter The Format In Which You Want To Convert : ")
                c=int(input("Enter The volume   : "))
                if b=='Kl':
                    d=c/1000000
                    print(c,"Ml is",d,"Kl")
                elif b=='Hl':
                    d=c/100000
                    print(c,"Ml is",d,"Hl")
                elif b=='Dl':
                    d=c/10000
                    print(c,"Ml is",d,"Dl")
                elif b=='l':
                    d=c/1000
                    print(c,"Ml is",d,"l")
                elif b=='dl':
                    d=c/100
                    print(c,"Ml is",d,"dl")
                elif b=='Cl':
                    print(c,"Ml is",d,"Cl")
                else:
                    print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")

            else:
                 print("CHECK YOUR CODE AND WRITE IT AGAIN!!!!!!")
        elif cv=='4':
                u=input("Enter The Format i.e MB, KB, GB, TB, PB, EB, ZB, YB(Block Letter)\n0 to quit : ")
    
                if u=='MB':
                     a=float(input("Enter Data : "))
                     b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")
                     if b=='KB':
                        kb=a*1024
                        print(a,"MB is",kb,"KB")
                     elif b=='GB':
                        gb=a/1024
                        print(a,"MB is",gb,"GB")
                     elif b=='TB':
                        tb=a/(1024*1024)
                        print(a,"MB is",tb,"TB")
                     elif b=='PB':
                        pb=a/(1024**3)
                        print(a,"MB is",pb,"PB")
                     elif b=='EB':
                        eb=a/(1024**4)
                        print(a,"MB is",eb,"EB")
                     elif b=='ZB':
                        zb=a/(1024**5)
                        print(a,"MB is",zb,"ZB")
                     elif b=='YB':
                        yb=a/(1024**6)
                        print(a,"MB is",yb,"YB")
                     elif b=='MB':
                        print("YOU ENTERED THE SAME FORMAT.REWRITE")
                     else:
                        print("WRITE CORRECTLY IN BLOCK LETTER")
                elif u=='KB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")

                    if b=='MB':
                        mb=a/1024
                        print(a,"KB is",mb,"MB")
                    elif b=='GB':
                        gb=a/(1024*1024)
                        print(a,"KB is",gb,"GB")
                    elif b=='TB':
                        tb=a/(1024**3)
                        print(a,"KB is",tb,"TB")
                    elif b=='PB':
                        pb=a/(1024**4)
                        print(a,"KB is",pb,"PB")
                    elif b=='EB':
                        eb=a/(1024**5)
                        print(a,"KB is",eb,"EB")
                    elif b=='ZB':
                        zb=a/(1024**6)
                        print(a,"KB is",zb,"ZB")
                    elif b=='YB':
                        yb=a/(1024**7)
                        print(a,"KB is",yb,"YB")
                    elif b=='KB':
                        print("YOU ENTERED THE SAME FORMAT.REWRITE")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTER")
            
                elif u=='GB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")

                    if b=='MB':
                        mb=a*1024
                        print(a,"GB is",mb,"MB")
                    elif b=='KB':
                        kb=a*1024*1024
                        print(a,"GB is",kb,"KB")
                    elif b=='TB':
                        tb=a/1024
                        print(a,"GB is",tb,"TB")
                    elif b=='PB':
                        pb=a/(1024**2)
                        print(a,"GB is",pb,"PB")
                    elif b=='EB':
                        eb=a/(1024**3)
                        print(a,"GB is",eb,"EB")
                    elif b=='ZB':
                        zb=a/(1024**4)
                        print(a,"GB is",zb,"ZB")
                    elif b=='YB':
                        yb=a/(1024**5)
                        print(a,"GB is",yb,"ZB")
                    elif b=='GB':
                        print("YOU ENTERED THE SAME FORMAT.REWRITE")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTER")
                elif u=='TB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")

                    if b=='KB':
                        kb=a*1024*1024*1024
                        print(a,"TB is",kb,"KB")
                    elif b=='GB':
                        gb=a*1024
                        print(a,"TB is",gb,"GB")
                    elif b=='MB':
                        mb=a*1024*1024
                        print(a,"TB is",mb,"MB")
                    elif b=='PB':
                        pb=a/(1024)
                        print(a,"TB is",pb,"PB")
                    elif b=='EB':
                        eb=a/(1024**2)
                        print(a,"TB is",eb,"EB")
                    elif b=='ZB':
                        zb=a/(1024**3)
                        print(a,"TB is",zb,"ZB")
                    elif b=='YB':
                        yb=a/(1024**4)
                        print(a,"TB is",yb,"YB")
                    elif b=='TB':
                        print("YOU ENTERED THE SAME FORMAT.REWRITE")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTER")
                elif u=='PB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")

                    if b=='TB':
                        tb=a*1024
                        print(a,'PB is',tb,"TB")
                    elif b=='GB':
                        gb=a*1024*1024
                        print(a,'PB is',gb,"GB")
                    elif b=='MB':
                        tb=a*1024*1024*1024
                        print(a,'PB is',tb,"MB")
                    elif b=='KB':
                        tb=a*1024*1024*1024*1024
                        print(a,'PB is',tb,"KB")
                    elif b=='EB':
                        tb=a/1024
                        print(a,'PB is',tb,"EB")
                    elif b=='ZB':
                        tb=a/(1024*1024)
                        print(a,'PB is',tb,"ZB")
                    elif b=='YB':
                        tb=a/(1024*1024*1024)
                        print(a,'PB is',tb,"YB")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTERS!!!")
                elif u=='EB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")

                    if b=='PB':
                        h=a*1024
                        print(a,"EB is",h,"PB")
                    elif b=='TB':
                        h=a*1024*1024
                        print(a,"EB is",h,"TB")
                    elif b=='GB':
                        h=a*1024*1024*1024
                        print(a,"EB is",h,"GB")
                    elif b=='MB':
                        h=a*1024*1024*1024*1024
                        print(a,"EB is",h,"MB")
                    elif b=='KB':
                        h=a*1024*1024*1024*1024*1024
                        print(a,"EB is",h,"KB")
                    elif b=='ZB':
                        h=a/1024
                        print(a,"EB is",h,"ZB")
                    elif b=='YB':
                        h=a/(1024*1024)
                        print(a,"EB is",h,"YB")
                    elif b=='ZB':
                        print("You Entered The Same Format")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTERS!!!")
                elif u=='ZB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")
                    if b=='EB':
                        h=a*1024
                        print(a,"ZB is",h,"EB")
                    elif b=='PB':
                        h=a*(1024**2)
                        print(a,"ZB is",h,"PB")
                    elif b=='TB':
                        h=a*(1024**3)
                        print(a,"ZB is",h,"TB")
                    elif b=='GB':
                        h=a*(1024**4)
                        print(a,"ZB is",h,"GB")
                    elif b=='MB':
                        h=a*(1024**5)
                        print(a,"ZB is",h,"MB")
                    elif b=='KB':
                        h=a*(1024**6)
                        print(a,"ZB is",h,"KB")
                    elif b=='YB':
                        h=a/1024
                        print(a,"ZB is",h,"YB")
                    elif b=='EB':
                        print("You Entered The Same Format")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTERS!!!")
                elif u=='YB':
                    a=float(input("Enter Data : "))
                    b=input("Enter The Format In which You Want To Convert Data In(Block Letter) : ")
                    if b=='ZB':
                        h=a*1024
                        print(a,"YB is",h,"ZB")
                    elif b=='EB':
                        h=a*(1024**2)
                        print(a,"YB is",h,"EB")
                    elif b=='PB':
                        h=a*(1024**3)
                        print(a,"YB is",h,"PB")
                    elif b=='TB':
                        h=a*(1024**4)
                        print(a,"YB is",h,"TB")
                    elif b=='GB':
                        h=a*(1024**5)
                        print(a,"YB is",h,"GB")
                    elif b=='MB':
                        h=a*(1024**6)
                        print(a,"YB is",h,"MB")
                    elif b=='KB':
                        h=a*(1024**7)
                        print(a,"YB is",h,"KB")
                    elif b=='YB':
                        print("YOU Entered The Same Format")
                    else:
                        print("WRITE CORRECTLY IN BLOCK LETTERS!!!")
                elif u=='0':
                    print("Thanks for Your Valueable time\nTime To say GoodBye")
                    break
                else:
                    print("WRITE CORRECTLY IN BLOCK LETTERS")
    elif vb=='2':
        er=0
        while er<1:
            print("What Do you want Square or Squre Root(1,2)")
            af=input("For sq press 1\nFor square root press 2\n0.for MAin Menu\n")
            print("****************************************************************************************************************************************************************")
            if af=='1':
                aj=int(input("Enter The Number : "))
                print("The Square of",aj,"is",aj**2)
            elif af=='2':
                aj=int(input("Enter The Square : "))
                ak=math.sqrt(aj)
                print("The Square root of",aj,"is",ak)
            elif af=='0':
                break
            else:
                print("Write again please")
            

    elif vb=='0':
        print(aq,"Thanks For using This program")

        break
        quit()

    else:
        print("REWRITE PLEASE")
        print("***************************************************************************************************************************************************************")

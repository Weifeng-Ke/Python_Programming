#Lab 2 (part2)
#student name: Weifeng Ke   
#student number: 18879288

from tkinter import *
#do not import any more modules

#do not change the skeleton of the program. Only add code where it is requested.
class Complex:
    """ this class implements the complex number type 
        it stores the complex number in from
        two data fields: 
            real and complex
        Operation: 
            add, subtract, multiply and divide
            toString
    """
    def __init__(self,real: float,complex: float) -> None:
        """initizer stores the complex number in the original form""" 
        self._real=real
        self._complex=complex
        
    
    def add(self, secondComplex: "Complex") -> "Complex":
        """adds 'this' Complex to secondComplex
           returns the result as a Complex number (type Complex)
        """
        if secondComplex._real == "" or secondComplex._complex == "" :
            return Complex("","")
        num1= self._real+secondComplex._real
        num2=self._complex+secondComplex._complex
        return Complex(num1,num2)
    
    def subtract(self, secondComplex: "Complex") -> "Complex":
        """subtract 'this' Complex to secondComplex
           returns the result as a complex number (type Complex)
        """
        if secondComplex._real == "" or secondComplex._complex == "" :
            return Complex("","")
        num1= self._real-secondComplex._real
        num2=self._complex-secondComplex._complex
        return Complex(num1,num2)    
    
    def multiply(self, secondComplex: "Complex") -> "Complex":
        """multiply 'this' complex to secondComplex
           returns the result as a Complex number (type Complex)
        """
        if secondComplex._real == "" or secondComplex._complex == "" :
            return Complex("","")
        num1= (self._real*secondComplex._real)-(self._complex*secondComplex._complex)       
        num2=(self._real*secondComplex._complex)+(self._complex*secondComplex._real)
        return Complex(num1,num2)
    
    def divide(self, secondComplex: "Complex") -> "Complex":
        """divide 'this' complex to secondComplex
           returns the result as a complex number (type Complex)
        """
        #This is to ensure every parameter has been entered
        if secondComplex._real == "" or secondComplex._complex == "" :
            return Complex("","")
        num_real=(self._real*secondComplex._real)+(self._complex*secondComplex._complex)
        num_img=(self._complex*secondComplex._real)-(self._real*secondComplex._complex)
        num_denom=(abs(secondComplex._real) ** 2)+(abs(secondComplex._complex) ** 2)
        if num_denom == 0:
            return Complex("","")
        return Complex(num_real/num_denom,num_img/num_denom)
    
    def toString(self) -> str:
        """ returns a string representation of 'this' complex
            the format is: real + (+- Imaginary) i
            if 'this' complex number is an 0, it must not show both real equals to 0 and imaginary equals to 0 
            if any part of real and imaginary is NULL, it just returns "NaN" (not a number)
        """
        #this is to check to see if all entry has been entered
        if self._real == "" and self._complex == "":
            return f"NaN"
        #this is to check if both real and imaginary part are 0 we return 0
        elif self._real == 0 and self._complex == 0:
            return f"0"
        #this is to check if it's just the real part
        elif self._real != 0 and self._complex == 0:
            return f"{self._real:.1f}"
        #this is to check if it's just the imaginary part
        elif self._real == 0 and self._complex != 0:
            return f"{self._complex:.1f} i"
        #this is to ensure if complex is 1 we display i alone not coefficient of 1
        elif abs(self._complex) == 1:
            #this if and else is to ensure it work for both pos and neg
            if self._complex>0:
                return f"{self._real:.1f} + i"
            else:
                return f"{self._real:.1f} - i"
        #not special condition, display result in a standard format for pos imaginary part and negative imaginary part
        else:
            if self._complex>0:
                return f"{self._real:.1f} + {self._complex:.1f} i"
            else:
                return f"{self._real:.1f} + ({self._complex:.1f}) i"
class GUI:
    """ this class implements the GUI for our program
        use as is.
        The add, subtract, multiply and divide methods invoke the corresponding
        methods from the Rational class to calculate the result to display.
    """
    def __init__(self):
        """ The initializer creates the main window, label and entry widgets,
            and starts the GUI mainloop.
        """
        window = Tk()
        window.title("CN") #Complex Numbers
       
        # Labels and entries for the first complex number
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)
        Label(frame1, text = "Complex 1:").pack(side = LEFT)
        self.complex1Real = StringVar()
        Entry(frame1, width = 5, textvariable = self.complex1Real, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "+").pack(side = LEFT)
        self.complex1Imaginary = StringVar()
        Entry(frame1, width = 5, textvariable = self.complex1Imaginary, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1,text = 'i').pack(side =RIGHT)
        
        # Labels and entries for the second complex number
        frame2 = Frame(window)
        frame2.grid(row = 3, column = 1, pady = 10)
        Label(frame2, text = "Complex 2:").pack(side = LEFT)
        self.complex2Real = StringVar()
        Entry(frame2, width = 5, textvariable = self.complex2Real, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "+").pack(side = LEFT)
        self.complex2Imaginary = StringVar()
        Entry(frame2, width = 5, textvariable = self.complex2Imaginary, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2,text = 'i').pack(side =RIGHT)
        
        # Labels and entries for the result rational number
        # an entry widget is used as the output here
        frame3 = Frame(window)
        frame3.grid(row = 4, column = 1, pady = 10)
        Label(frame3, text = "Result:     ").pack(side = LEFT)
        self.result = StringVar()
        Entry(frame3, width = 12, textvariable = self.result, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)

        # Buttons for add, subtract, multiply and divide
        frame4 = Frame(window) # Create and add a frame to window
        frame4.grid(row = 5, column = 1, pady = 5, sticky = E)
        Button(frame4, text = "Add", command = self.add).pack(
            side = LEFT)
        Button(frame4, text = "Subtract", 
               command = self.subtract).pack(side = LEFT)
        Button(frame4, text = "Multiply", 
               command = self.multiply).pack(side = LEFT)
        Button(frame4, text = "Divide", 
               command = self.divide).pack(side = LEFT)
               
        mainloop()
        
    def add(self): 
        (cnum1, cnum2) = self.getbothComplex()
        result = cnum1.add(cnum2)
        self.result.set(result.toString())
    
    def subtract(self):
        (cnum1, cnum2) = self.getbothComplex()
        result = cnum1.subtract(cnum2)
        self.result.set(result.toString())
    
    def multiply(self):
        (cnum1, cnum2) = self.getbothComplex()
        result = cnum1.multiply(cnum2)
        self.result.set(result.toString())
    
    def divide(self):
        (cnum1, cnum2) = self.getbothComplex()
        result = cnum1.divide(cnum2)
        self.result.set(result.toString())

    def getbothComplex(self):
        """ Helper method used by add, subtract, multiply and divide methods"""
        try:
            real1 = eval(self.complex1Real.get())
            complex1 = eval(self.complex1Imaginary.get())
            cnum1 = Complex(real1, complex1)

            real2 = eval(self.complex2Real.get())
            complex2 = eval(self.complex2Imaginary.get())
            cnum2 = Complex(real2, complex2)
            return (cnum1, cnum2)
        except:
            return(Complex("",""), Complex("","")) #if an entry value is missing, cause NaN

if __name__ == "__main__": GUI() 
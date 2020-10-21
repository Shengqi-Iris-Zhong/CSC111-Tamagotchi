# Group 28
# Meihui Chen, Hana Hirano, Shengqi (Iris) Zhong

# Tamagotchi

from mygraphics import *


class Button:

    '''A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it.'''

    def __init__(self, win, xcent, ycent, width2, height2, color, slabel):
        '''Creates a rectangular button.
        width2 & height2 are half of the full width & height''' 
        
        self.rect = MyRectangle(xcent, ycent, width2, height2)
        self.rect.setFill( color )
        self.rect.draw(win)

        p = Point( xcent, ycent )
        self.slabel = slabel # To make the string accessible to methods
        self.label = Text(p, slabel)
        self.label.setSize( 10 )
        self.label.draw(win)
        self.verbose = False
        self.activate()

    def clicked(self, p):
        '''Returns True if button active and p is inside'''
        if PtInRect( p, self.rect ):
            if self.verbose:
                print( 'Button clicked:',self.slabel )
            return True
        else:
            return False

    def activate(self):
        '''Sets this button to active.'''
        self.label.setFill('DarkRed')
        self.rect.setWidth(3)
        self.active = True

    def undraw(self):
        '''Undraw the button'''
        self.rect.undraw()
        self.label.undraw()

    def deactivate(self):
        '''Sets this button to inactive.'''
        self.label.setFill('DarkGrey')
        self.rect.setWidth(1)
        self.active = False

    def setVerboseOn(self):
        '''Turns on printing for each method call'''
        self.verbose = True

    def setVerboseOff(self):
        '''Turns off printing for each method call'''
        self.verbose = False

class Dog:
    '''create a class to draw and undraw the dog figure by putting dog body parts
        into a list. Create dog face in three mood: happy, flat, and sad.
        The size and positon of the dog character displayed can be changed
        by changing the size and x,y input.''' 

    def __init__( self, win, x, y,size ):
        '''creates different parts of dog. x and y are the position inputs of
            the dog, and size is the size input of dog'''

        #initiate the local variable self.mood
        self.mood = ' '
        
        #dog face
        dogface = Circle( Point( x, y ), 3*size )
        dogface.setFill( 'tan' )
        dogface.setOutline( 'tan' )

        #two dog ears
        dog_R_ear = Polygon( Point( x-3.5*size, y+size ), Point( x-1.7*size, y+2.4*size ), Point( x-2.5*size, y-0.5*size ) )
        dog_R_ear.setFill( 'maroon' )
        dog_R_ear.setOutline( 'maroon' )
        self.dog_R_ear = dog_R_ear

        dog_L_ear = Polygon( Point( x+3.5*size, y+size ), Point( x+1.7*size, y+2.4*size ), Point( x+2.5*size, y-0.5*size ) ) 
        dog_L_ear.setFill( 'maroon' )
        dog_L_ear.setOutline( 'maroon' )
        self.dog_L_ear = dog_L_ear

        #dog eyes
        dog_R_eyew = Circle( Point( x-1.2*size, y+0.5*size ), 0.6*size )
        dog_R_eyew.setFill( 'white' )
        dog_R_eyew.setOutline( 'white' )
        self.dog_R_eyew = dog_R_eyew

        dog_L_eyew = Circle( Point( x+1.2*size, y+0.5*size ), 0.6*size )
        dog_L_eyew.setFill( 'white' )
        dog_L_eyew.setOutline( 'white' )
        self.dog_L_eyew = dog_L_eyew
        
        dog_f_w1 = Point( x-1.3*size, y-0.3*size )
        dog_f_w2 = Point( x+1.3*size, y-2.5*size )
        dog_face_white = Oval( dog_f_w1, dog_f_w2 )
        dog_face_white.setFill( 'white' )
        dog_face_white.setOutline( 'white' )
        self.dog_face_white = dog_face_white

        #dog nose
        dog_nose1 = Point( x-0.8*size, y-1*size )
        dog_nose2 = Point( x+0.8*size, y-0.5*size)
        dog_nose = Oval( dog_nose1, dog_nose2 )
        dog_nose.setFill( 'black' )
        self.dog_nose = dog_nose

        #dogneck
        dog_neck1 = Point( x-1.8*size, y-1.9*size )
        dog_neck2 = Point( x+1.8*size, y-3.2*size )
        dog_neck = Oval( dog_neck1, dog_neck2 )
        dog_neck.setFill( 'red' )
        dog_neck.setOutline( 'red' )
        self.dog_neck = dog_neck

        #body 
        dog_b1 = Point( x-1.5*size, y-2*size )
        dog_b2 = Point( x+1.5*size, y-2.0*size )
        dog_b3 = Point( x+3.5*size, y-4*size )
        dog_b4 = Point( x+2.5*size, y-4.0*size )
        dog_b5 = Point( x+2.5*size, y-8*size )
        dog_b6 = Point( x+1.5*size, y-7.0 *size)
        dog_b7 = Point( x-1.5*size, y-7*size )
        dog_b8 = Point( x-2.5*size, y-8.0*size )
        dog_b9 = Point( x-2.5*size, y-4 *size)
        dog_b10 = Point( x-3.5*size, y-4.0*size )

        dog_b = Polygon( dog_b1, dog_b2, dog_b3, dog_b4, dog_b5, dog_b6, dog_b7, dog_b8, dog_b9, dog_b10 )
        dog_b.setFill( 'tan' )
        dog_b.setOutline( 'tan' )
        self.dog_b = dog_b

        dog_b_white = Circle( Point( x, y-5.0*size ), 1.5*size )
        dog_b_white.setFill( 'white' )
        dog_b_white.setOutline( 'white' )
        self.dog_b_white = dog_b_white
        
        #put body parts of the bog figure into a list
        L = [dog_b, dog_b_white, dog_neck, dogface, dog_R_ear, dog_L_ear, dog_R_eyew, dog_L_eyew, dog_face_white, dog_nose]
        #store the list as a local variable
        self.L = L

        # Expressions of the dog figure
        #flat
        dog_R_eye = Circle( Point( x-1.2*size, y+size*0.5 ), size*0.3 )
        dog_R_eye.setFill( 'black' )
        
        dog_L_eye = Circle( Point( x+1.2*size, y+size*0.5 ), size*0.3 )
        dog_L_eye.setFill( 'black' )
    
        dog_mouth1 = Point( x-size*0.4, y-1.5*size )
        dog_mouth2 = Point( x+size*0.4, y-1.5*size )
        dog_mouth3 = Point( x, y-2*size )
        dog_mouth = Polygon( dog_mouth1, dog_mouth2, dog_mouth3 )
        dog_mouth.setFill( 'pink' )
        dog_mouth.setOutline( 'pink' )
        
        #store the flat facial expression into a list
        F = [dog_R_eye, dog_L_eye, dog_mouth]
        self.F = F

        # happy face
        dog_happy_Reye = Text( Point( x+1.2*size, y+size*0.5 ), '<' )
        dog_happy_Reye.setSize( 2*size )
        dog_happy_Reye.setTextColor( 'black' )

        dog_happy_Leye = Text( Point( x-1.2*size, y+0.5*size ), '>' )
        dog_happy_Leye.setSize( 2*size )
        dog_happy_Leye.setTextColor( 'black' )

        dog_happy_mouth1 = Point( x-0.8*size, y-1.5*size )
        dog_happy_mouth2 = Point( x+0.8*size, y-1.5*size )
        dog_happy_mouth3 = Point( x, y-2.3*size )
        dog_happy_mouth = Polygon( dog_happy_mouth1, dog_happy_mouth2, dog_happy_mouth3 )
        dog_happy_mouth.setFill( 'pink' )
        dog_happy_mouth.setOutline( 'pink' )

        dog_Rcheek1 = Point( x+2.3*size, y-0.3*size )
        dog_Rcheek2 = Point( x+1.5*size, y-0.8*size )
        dog_Rcheek = Oval( dog_Rcheek1, dog_Rcheek2 )
        dog_Rcheek.setFill( 'salmon' )
        dog_Rcheek.setOutline( 'salmon' )

        dog_Lcheek1 = Point( x-2.3*size, y-0.3*size )
        dog_Lcheek2 = Point( x-1.5*size, y-0.8*size )
        dog_Lcheek = Oval( dog_Lcheek1, dog_Lcheek2 )
        dog_Lcheek.setFill( 'salmon' )
        dog_Lcheek.setOutline( 'salmon' )
        
        #store the happy facial expression into a list
        H = [dog_happy_Reye, dog_happy_Leye, dog_happy_mouth, dog_Rcheek, dog_Lcheek]
        self.H = H

        # sad face
        dog_sad_Reye = Text( Point( x+1.2*size, y+0.5*size ), '.' )
        dog_sad_Reye.setSize( size*3 )
        dog_sad_Reye.setTextColor( 'black' )

        dog_sad_Leye = Text( Point( x-1.2*size, y+0.5*size ), '.' )
        dog_sad_Leye.setSize( size*3 )
        dog_sad_Leye.setTextColor( 'black' )

        dog_sad_mouth1 = Point( x-0.5*size, y-2.3*size )
        dog_sad_mouth2 = Point( x+0.5*size, y-2.3*size )
        dog_sad_mouth3 = Point( x, y-1.5*size )
        dog_sad_mouth = Polygon( dog_sad_mouth1, dog_sad_mouth2, dog_sad_mouth3 )
        dog_sad_mouth.setFill( 'pink' )
        dog_sad_mouth.setOutline( 'pink' )
        
        #store the sad facial expression into a list
        S = [dog_sad_Reye, dog_sad_Leye, dog_sad_mouth]
        self.S = S
        

    def facebody( self, win, expression ):     
        '''run for-loops to draw the dog figure and the
            expressions of dog;
            expression take three values: Flat, sad, happy.
        '''
        for i in self.L:
            i.draw( win )
            
        #update self.mood to the chosen emotion
        #if emo matchs the emotion input, run for loop to draw the corresponding emotion    
        if expression == 'flat':
            for i in self.F:
                i.draw( win )
            self.mood = 'flat'
                
        elif expression == 'happy':
            for i in self.H:
                i.draw( win )
            self.mood = 'happy'
                
        elif expression == 'sad':
            for i in self.S:
                i.draw( win )
            self.mood = 'sad'
                     
    def undraw_dog(self ):     
        '''undraw the whole dog figure by undraw the body parts
            and expressions of the dog
        '''
        for i in self.L:
            i.undraw(  )
        #if the updated self.mood matchs the emotion string, run for loop to draw the corresponding emotion    
        if self.mood == 'happy':
            for i in self.H:
                i.undraw( )
        elif self.mood == 'sad':
            for i in self.S:
                i.undraw( )
        elif self.mood == 'flat':
            for i in self.F:
                i.undraw( ) 
      
class Cat:
    '''create a class to draw and undraw the cat figure by putting cat body
        parts into a list. Create cat face in three mood: happy, flat, and sad.
        The size and positon of the cat character displayed can be changed
        by changing the size and x,y input.
    ''' 
    def __init__ (self,win,xcent,ycent,size,bgcolor):
        '''creates different parts of cat. x and y are the position inputs of
            the cat, and size is the size input of cat
        '''
        #initiated local variable self.mood
        self.mood = ''

        #face and nose of the cat
        self.face=MyOval(xcent,ycent,size*12,size*10)
        self.face.setFill("#66676b")
        self.face.setOutline("#66676b")
        
        self.ear1=Polygon(Point(xcent-size*2,ycent+size*9),Point(xcent-size*11,ycent+size*2),Point(xcent-size*13,ycent+size*11))
        self.ear1.setOutline( "#66676b" )
        self.ear1.setFill( "#66676b" )
        self.ear2=Polygon(Point(xcent+size*2,ycent+size*9),Point(xcent+size*11,ycent+size*2),Point(xcent+size*13,ycent+size*11))
        self.ear2.setOutline( "#66676b" )
        self.ear2.setFill( "#66676b" )
        self.ear3=Polygon(Point(xcent-size*2.5,ycent+size*8),Point(xcent-size*10,ycent+size*1.5),Point(xcent-size*12,ycent+size*10))
        self.ear3.setOutline("#cfa299")
        self.ear3.setFill("#cfa299")
        self.ear4=Polygon(Point(xcent+size*2.5,ycent+size*8),Point(xcent+size*10,ycent+size*1.5),Point(xcent+size*12,ycent+size*10))
        self.ear4.setOutline("#cfa299")
        self.ear4.setFill("#cfa299")

        self.nose1=MyOval(xcent,ycent-size*2.7,size*1.5,size*0.6)
        self.nose2=Polygon(Point(xcent-size*1.5,ycent-size*2.7),Point(xcent+size*1.5,ycent-size*2.7),Point(xcent,ycent-size*4))
        self.nose1.setOutline("#cfa299")
        self.nose1.setFill("#cfa299")
        self.nose2.setOutline("#cfa299")
        self.nose2.setFill("#cfa299")

        # eye in flat
        self.eye1=Circle(Point(xcent-size*5,ycent+size),size*2.7)
        self.eye2=Circle(Point(xcent+size*5,ycent+size),size*2.7)
        self.eye1.setFill("white")
        self.eye1.setOutline("white")
        self.eye2.setFill("white")
        self.eye2.setOutline("white")
        self.eye3=Circle(Point(xcent-size*5,ycent+size),size*2)
        self.eye4=Circle(Point(xcent+size*5,ycent+size),size*2)
        self.eye3.setFill("black")
        self.eye4.setFill("black")
        self.eye5=Circle(Point(xcent-size*4,ycent+1.5*size),size*0.3)
        self.eye5.setFill("white")
        self.eye6=Circle(Point(xcent+size*6,ycent+1.5*size),size*0.3)
        self.eye6.setFill("white")        

        # eye in happy
        self.eye21=Text(Point(xcent-size*5,ycent+size),"^")
        self.eye22=Text(Point(xcent+size*5,ycent+size),"^")
        self.eye21.setSize(25)
        self.eye22.setSize(25)

        # eye in sad
        self.eye31=Text(Point(xcent-size*5,ycent+size),">")
        self.eye32=Text(Point(xcent+size*5,ycent+size),"<")
        self.eye31.setSize(size*10)
        self.eye32.setSize(size*10)

        self.mouth=Line(Point(xcent,ycent-size*4),Point(xcent,ycent-size*6))
        self.mouth.setWidth(size)
        self.mouth.setOutline("#cfa299")
                         
        # mouth in flat
        self.mouth1=Line(Point(xcent-size*2,ycent-size*6),Point(xcent+size*2,ycent-size*6))
        self.mouth1.setWidth(size)
        self.mouth1.setOutline("#cfa299")
        
        # mouth in happy
        self.mouth21=Line(Point(xcent,ycent-size*6),Point(xcent-size*2,ycent-size*4.8))
        self.mouth22=Line(Point(xcent,ycent-size*6),Point(xcent+size*2,ycent-size*4.8))
        self.mouth21.setWidth(size)
        self.mouth21.setOutline("#cfa299")
        self.mouth22.setWidth(size)
        self.mouth22.setOutline("#cfa299")

        # mouth in sad
        self.mouth31=Line(Point(xcent,ycent-size*6),Point(xcent-size*1.5,ycent-size*7.2))
        self.mouth32=Line(Point(xcent,ycent-size*6),Point(xcent+size*1.5,ycent-size*7.2))
        self.mouth31.setWidth(size)
        self.mouth31.setOutline("#cfa299")
        self.mouth32.setWidth(size)
        self.mouth32.setOutline("#cfa299")
       

        self.body1=Polygon(Point((xcent-size*7),(ycent-size*8)),Point((xcent+size*7),(ycent-size*8)),Point((xcent+size*15),(ycent-size*12)),Point((xcent-size*15),(ycent-size*12)))
        self.body1.setOutline( "#66676b" )
        self.body1.setFill( "#66676b" )

        self.paw1=Circle(Point(xcent+size*15,ycent-size*12),size*0.5)
        self.paw2=Circle(Point(xcent-size*15,ycent-size*12),size*0.5)
        self.paw1.setOutline("#cfa299")
        self.paw1.setFill("#cfa299")
        self.paw2.setOutline("#cfa299")
        self.paw2.setFill("#cfa299")

        self.tail1=Circle(Point(xcent+9.5*size,ycent-size*15),size*9)
        self.tail2=Circle(Point(xcent+9.5*size,ycent-size*13),size*9)
        self.tail1.setOutline("#66676b")
        self.tail1.setFill("#66676b")        
        self.tail2.setOutline(bgcolor)
        self.tail2.setFill(bgcolor)
        
        self.body2=MyRectangle(xcent,ycent-size*20,size*9.5,size*8)
        self.body2.setOutline("#66676b")
        self.body2.setFill("#66676b")

        self.tummy=MyOval(xcent,ycent-size*17,size*4,size*6)
        self.tummy.setOutline("#b3aaa3")
        self.tummy.setFill("#b3aaa3")

        self.leg1=Polygon(Point(xcent-size*9.5,ycent-size*28),Point(xcent-size*6.5,ycent-size*28),Point(xcent-size*9.5,ycent-size*33))
        self.leg1.setOutline("#66676b")
        self.leg1.setFill("#66676b")
        self.leg2=Polygon(Point(xcent+size*9.5,ycent-size*28),Point(xcent+size*6.5,ycent-size*28),Point(xcent+size*9.5,ycent-size*33))
        self.leg2.setOutline("#66676b")
        self.leg2.setFill("#66676b")

        self.paw3=Circle(Point(xcent-size*9.5,ycent-size*33),size*0.5)
        self.paw4=Circle(Point(xcent+size*9.5,ycent-size*33),size*0.5)
        self.paw3.setOutline("#cfa299")
        self.paw3.setFill("#cfa299")
        self.paw4.setOutline("#cfa299")
        self.paw4.setFill("#cfa299")

        #store body parts of the cat figure into a list
        self.L = [self.ear1, self.ear2, self.ear3,self.ear4,self.tail1,self.tail2,self.face,self.eye1,self.eye2,self.nose1,self.nose2,\
             self.mouth,self.body1,self.paw1,self.paw2,self.body2,self.tummy,self.leg1,self.leg2,self.paw3,self.paw4]
        #store the expressions of cat figure into seperate lists
        #happy
        self.H = [self.eye21,self.eye22,self.mouth21,self.mouth22]
        #flat
        self.F = [self.eye3,self.eye4,self.eye5,self.eye6,self.mouth1]
        #sad
        self.S = [self.eye31,self.eye32,self.mouth31,self.mouth32]
        
    def facebody(self,win,emo):
        '''run for-loops to draw the cat figure and the
            expressions of cat;
            expression take three values: Flat, sad, happy.
        '''
        
        for i in self.L: #run for loop to draw the body parts stored in the self.L list
            i.draw(win)

        #if emo matchs the emotion input, run for loop to draw the corresponding emotion
        #update self.mood to the chosen emotion    
        if emo=="flat": 
            for i in self.F:
                i.draw(win)
            self.mood = 'flat'
            
        elif emo=="happy":
            for i in self.H:
                i.draw(win)
            self.mood = 'happy'
            
        elif emo=="sad":
            for i in self.S:
                i.draw(win)
            self.mood = 'sad'
            
    def undraw_cat(self):
        '''undraw the whole cat figure by undraw the cat body parts
            and expressions of the dog
        '''
        #undraw the body part
        for i in self.L:
            i.undraw(  )
        #if the updated self.mood matchs the emotion string, run for loop to draw the corresponding emotion    
        if self.mood == 'happy':
            for i in self.H:
                i.undraw( )
                
        elif self.mood == 'sad':
            for i in self.S:
                i.undraw( )
                
        elif self.mood == 'flat':
            for i in self.F:
                i.undraw( )
                             
class squirrel:
    '''create a class to draw and undraw the squirrel figure by putting squirrel body
        parts into a list. Create squirrel face in three mood: happy, flat, and sad.
        The size and positon of the squirrel character displayed can be changed
        by changing the size and x,y input.
    ''' 
    def __init__(self, win, x, y,size):
        '''create a squirrel. creates different parts of squirrel. x and y are the position inputs of
            the squirrel, and size is the size input of squirrel
        '''
        #initiated local variable self.mood
        self.mood = ''
        
        #store color of the face, body, leg, and tail of the squirrel 
        cface = '#f0e68c'
        cbody = '#cd853f'
        cleg = '#8b4513'
        ctail = '#8b4513'
        #store selected colors into local variable
        self.cface = cface
        self.cbody = cbody
        self.cleg = cleg
        self.ctail = ctail
        
        #squirrel in sad emotion
        self.sad1 = Circle(Point(x-size*2,y+size*5),size*0.4)
        self.sad1.setFill('lightblue')
        self.sad1.setOutline('lightblue')

        self.sad2 = Oval(Point(x-size*2.3,y+size*5.2),Point(x-size*1.3,y+size*4.3))
        self.sad2.setFill('lightblue')
        self.sad2.setOutline('lightblue')

        self.sad3 = Circle(Point(x-size*5.5,y+size*5),size*0.4)
        self.sad3.setFill('lightblue')
        self.sad3.setOutline('lightblue')

        self.sad4 = Oval(Point(x-size*6.1,y+size*5.2),Point(x-size*4.9,y+size*4.3))
        self.sad4.setFill('lightblue')
        self.sad4.setOutline('lightblue')

        self.sadmouth = Line(Point(x-size*5,y+size*2.5),Point(x-size*2.5,y+size*2.5))
        self.sadmouth.setOutline('darkred')
    
        #squirrel in happy emotion
        self.hp1 = Circle(Point(x-size*3.8,y+size*2),size*1.2)
        self.hp1.setFill('brown')
        self.hp1.setOutline('brown')
        
        self.hp2 = Oval(Point(x-size*5,y+size*3.5),Point(x-size*2.5,y+size*2))
        self.hp2.setFill(cface)
        self.hp2.setOutline(cface)

        #squirrel in flat emotion
        self.fl = Rectangle(Point(x-size*4.8,y+size*2.5),Point(x-size*2.8,y+size*1.2))
        self.fl.setFill('brown')
        self.fl.setOutline('brown')

        #body part
        #teeth
        self.teeth1 = Rectangle(Point(x-size*4.5,y+size*2.5),Point(x-size*3.9,y+size*1.5))
        self.teeth1.setOutline('white')
        self.teeth1.setFill('white') 
    
        self.teeth2 = Rectangle(Point(x-size*3.7,y+size*2.5),Point(x-size*3.1,y+size*1.5))
        self.teeth2.setOutline('white')
        self.teeth2.setFill('white')

        #tail
        self.tail1 = Oval(Point(x-size*3.5,y+size*9),Point(x+size*5,y-size*5))
        self.tail1.setFill(ctail)
        self.tail1.setOutline(ctail)

        self.tail2 = Oval(Point(x+size*2.3,y-size),Point(x+size*4,y-size*5))
        self.tail2.setFill('white')
        self.tail2.setOutline('white')

        self.tail3 = Oval(Point(x+size*6.2,y+size*4.5),Point(x+size*2,y-size*3))
        self.tail3.setFill('white')
        self.tail3.setOutline('white')
   
        #ear
        self.ear1 = Oval(Point(x-size*6.7,y+size*8.8),Point(x-size*5,y+size*6.2))
        self.ear1.setFill(cbody)
        self.ear1.setOutline(cbody)

        self.ear2 = Oval(Point(x-size*2.8,y+size*8.8),Point(x-size,y+size*6.2))
        self.ear2.setFill(cbody)
        self.ear2.setOutline(cbody)
       
        self.ear3 = Oval(Point(x-size*6.5,y+size*8.5),Point(x-size*5.5,y+size*6.5))
        self.ear3.setFill(cface)
        self.ear3.setOutline(cface)
       
        self.ear4 = Oval(Point(x-size*2.3,y+size*8.5),Point(x-size*1.2,y+size*6.5))
        self.ear4.setFill(cface)
        self.ear4.setOutline(cface)
        
        #legs
        self.leg1 = Oval(Point(x+size*0.8,y-size*5),Point(x-size*1.8,y-size*4.5))
        self.leg1.setFill(cleg)
        self.leg1.setOutline(cleg)
        
        self.leg2 = Oval(Point(x-size*6.5,y-size*0.5),Point(x-size*9.1,y-size*4.5))
        self.leg2.setFill(cleg)
        self.leg2.setOutline(cleg)
      
        #clawsback
        self.claw1 = Oval(Point(x-size*9.5,y-size*5),Point(x-size*6,y-size*4))
        self.claw1.setFill(cleg)
        self.claw1.setOutline(cleg)
        
        self.claw2 = Oval(Point(x+1.2*size,y-5*size),Point(x-1.5*size,y-4*size))
        self.claw2.setFill(cleg)
        self.claw2.setOutline(cleg)
        
        self.line1 = Line(Point(x,y-size*4.5),Point(x+size*0.2,y-size*5))
        self.line2 = Line(Point(x+size*0.4,y-size*4.5),Point(x+size*0.6,y-5*size))
      
        self.line3 = Line(Point(x-size*8.6,y-size*5),Point(x-size*8.4,y-4.5*size))
        self.line4 = Line(Point(x-9*size,y-5*size),Point(x-8.8*size,y-4.5*size))
        
        #body
        self.Body1 = Polygon( Point(x-6.0*size,y+2.0*size),Point(x,y-5.5*size), Point(x-2.0*size,y+2.0*size))
        self.Body1.setFill(cbody)
        self.Body1.setOutline(cbody)
       
        self.Body2 = Polygon( Point(x-6.0*size,y+2.0*size),Point(x,y-5.5*size), Point(x-8.0*size,y-5.5*size))
        self.Body2.setFill(cbody)
        self.Body2.setOutline(cbody)
        
        self.Body3 = Circle(Point(x-4.0*size,y-1.7*size),1.5*size)
        self.Body3.setFill(cface)
        self.Body3.setOutline(cface)

        self.Body4 = Polygon(Point(x-5.4*size,y-1.2*size),Point(x-6.5*size,y-5.0*size),Point(x-1.5*size,y-5.0*size))
        self.Body4.setFill(cface)
        self.Body4.setOutline(cface)
    
        self.Body5 = Polygon(Point(x-2.6*size,y-1.2*size),Point(x-6.5*size,y-5*size),Point(x-1.5*size,y-5.0*size))
        self.Body5.setFill(cface)
        self.Body5.setOutline(cface)
        
        #head
        self.Head = Oval(Point(x-8.0*size,y+7.5*size),Point(x,y+0.5*size))
        self.Head.setFill(cbody)
        self.Head.setOutline(cbody)
        
        #eye
        self.Eye1 = Circle(Point(x-4.9*size,y+5.5*size),size)
        self.Eye1.setFill('white')
        self.Eye1.setOutline('white')
        
        self.pupil1 = Circle(Point(x-4.5*size,y+5.5*size),0.3*size)
        self.pupil1.setFill('black')
    
        self.Eye2 = Circle(Point(x-2.7*size,y+5.5*size),size)
        self.Eye2.setFill('white')
        self.Eye2.setOutline('white')
        
        self.pupil2 = Circle(Point(x-3*size,y+5.5*size),0.3*size)
        self.pupil2.setFill('black')
        
        #mouse
        self.Mouse = Oval(Point(x-6.8*size,y+4.2*size),Point(x-1.2*size,y+0.5*size))
        self.Mouse.setFill(cface)
        self.Mouse.setOutline(cface)
        
        #clawsfornt
        self.claws3 = Oval(Point(x-4.0*size,y-4.5*size),Point(x+0.3*size,y-5.8*size))
        self.claws3.setFill(cbody)
        self.claws3.setOutline(cbody)
       
        self.claws4 = Oval(Point(x-4.3*size,y-4.5*size),Point(x-8.6*size,y-5.8*size))
        self.claws4.setFill(cbody)
        self.claws4.setOutline(cbody)
        
        self.line5 = Line(Point(x-0.6*size,y-5.2*size),Point(x-0.4*size,y-5.7*size))
        self.line6 = Line(Point(x-0.2*size,y-5.2*size),Point(x,y-5.5*size))
        
        self.line7 = Line(Point(x-7.7*size,y-5.6*size),Point(x-7.5*size,y-5.2*size))
        self.line8 = Line(Point(x-7.3*size,y-5.7*size),Point(x-7.1*size,y-5.2*size))
        
        self.Nose = Oval(Point(x-4.6*size,y+4.4*size),Point(x-3.0*size,y+3.5*size))
        self.Nose.setFill('black')

        #store body parts of the squirrel figure into a list in sequence 
        self.L = [self.tail1,self.tail2,self.tail3,self.ear1,self.ear2,self.ear3,self.ear4,self.claw1,self.claw2,self.leg1,self.leg2,\
                  self.line1,self.line2,self.line3,self.line4,self.Body1,self.Body2,self.Body3,self.Body4,self.Body5,self.Head,self.Eye1,self.pupil1,self.Eye2,self.pupil2,\
                  self.Mouse,self.claws3,self.claws4,self.line5,self.line6,self.line7,self.line8]
        #store the expressions of the squirrel figure into seperate lists
        #sad 
        self.S = [self.sad1,self.sad2,self.sad3,self.sad4,self.sadmouth,self.teeth1,self.teeth2,self.Nose]
        #flat
        self.F = [self.fl,self.teeth1,self.teeth2,self.Nose]
        #happy
        self.H = [self.hp1,self.teeth1,self.teeth2,self.hp2,self.Nose]
        
    def facebody(self,win,emo):
        '''run for-loops to draw the squirrel figure and the
            expressions of squirrel;
            expression take three values: Flat, sad, happy.
        '''
        for i in self.L: #run for loop to draw the body parts stored in the self.L list
            i.draw(win)
            
        #if emo matchs the emotion input, run for loop to draw the corresponding emotion
        #update self.mood to the chosen emotion    
        if emo=="flat":
            for i in self.F:
                i.draw(win)
            self.mood = 'flat'
            
        elif emo=="happy":
            for i in self.H:
                i.draw(win)
            self.mood = 'happy'
            
        elif emo=="sad":
            for i in self.S:
                i.draw(win)
            self.mood = 'sad'
            
    def undraw_squi(self):
        '''undraw the whole squirrel figure by undraw the squirrel body parts
            and expressions of the squirrel
        '''
        #undraw the body part
        for i in self.L:
            i.undraw(  )
        #if the updated self.mood matchs the emotion string, run for loop to draw the corresponding emotion     
        if self.mood == 'happy':
            for i in self.H:
                i.undraw( )
        elif self.mood == 'sad':
            for i in self.S:
                i.undraw( )
        elif self.mood == 'flat':
            for i in self.F:
                i.undraw( )

def Chat( voice, bot ):
    '''Takes user input, voice, and according to keywords,
    a comment will be returned as output, bot, and the pet's
    facial expression sometimes changes. '''

    #print( '=> Text analysis begins' )

    if 'good' in voice or 'great' in voice:
        bot.setText( 'I wanna know more!!!' )

    elif 'bad' in voice or 'sad'  in voice or 'cry' in voice:
        bot.setText( 'I want to make my lord happy!' )

    elif 'sure' in voice:
        bot.setText( 'What should we do?' )

    elif 'think' in voice:
        bot.setText( 'I wanna know how you think' )

    elif 'pet' in voice:
        bot.setText( 'I love you tooooo' )

    elif 'yes' in voice:
        bot.setText( 'I can say "yes" better, yesssssss' )

    elif 'love' in voice:
        bot.setText( "'= w ='" )

    else:
        bot.setText( 'PET ME!' )
        
    return bot

def Chat2( win,animal,dog1,cat1,squi1 ):
    '''Draws elements needed for chatting and returns
    replies through Chat()'''

    # Output background
    chatbg = MyRectangle( 0, -20, 60, 10 )
    chatbg.setFill( 'cornsilk' )
    chatbg.draw( win )

    # Output text
    bot = Text( Point( 0, -25 ), 'Welcome home, my lord! How are you?' )
    bot.setSize( 10 )
    bot.draw( win )

    # 'Your comment:' 
    chatlabel = Text( Point( -42, -42 ), 'Your comment:' )
    chatlabel.setSize( 12 )
    chatlabel.draw( win )

    # Textbox for the user
    textbox = Entry( Point( 0, -50 ), 30 )
    textbox.setFill( 'aquamarine' )
    textbox.draw( win )

    # Creating send and quit buttons
    sendbut = Button( win, 0, -60, 7, 4, 'pale green', 'SEND' )
    chatquit = Button( win, 0, -80, 15, 4, 'red', 'QUIT CHAT' )

    while True:
        
        p = win.checkMouse()
        if p: 
            if sendbut.clicked( p ): # When the user clicks 'send' button
                voice = textbox.getText() 
                voice = voice.lower() # The user input becomes lowercased 
                bot.undraw() # Bot output is cleared
                output = Chat( voice, bot ) # Text analysis begins
                bot = output 
                bot.draw( win ) # New output/ bot is written
                textbox.setText( '' ) # The user input is cleared to prepare for next comment
    
            elif chatquit.clicked( p ): # Chat function is finished when quit button is clicked
                chatbg.undraw()
                bot.undraw()
                chatlabel.undraw()
                textbox.undraw()
                sendbut.undraw()
                chatquit.undraw()
                break

                
                
            
def quiz( win, money,animal,dog1,cat1,squi1,n):
    '''win, money, animal, dog1, cat1, squi1,n
    Draws elements needed for taking a quiz.
    A question is selected randomly from a list of
    questions. When answered correctly, the pet smiles
    and when answered wrong, the pet becomes sad.
    '''
    
    # 'Question'
    title = Text( Point( 0, -65 ), 'QUESTION' )
    title.setSize( 15 )
    title.draw( win )

    # List of 10 questions
    LQuestion = [ '111 + 222 + 333?', '832 - 457?', '50 x 5?', \
                   '90 ÷ 10?', '26 + 32 - 12?', '72 x 3?', \
                   '200 - (96 ÷ 4)?', '24 + 4 ÷ 4?', ' 3 + 6 x (5 + 4) ÷ 3 - 7', \
                   '150 ÷ (6 + 3 x 8) - 5' ]

    # List of answers
    LAnswer = [ '666', '375', '250', '9', '46', '216', '176', '25', '14', '0' ]

    #n is randonized back in the main
    #each time n is randomized to a different number between 0 and 9
    n = n
    #question and corresponding selected 
    LQ = LQuestion[n]
    LA = LAnswer[n]
        

    # Creating send and quit buttons
    submitbut = Button( win, -25, -90, 10, 4, 'pale green', 'SUBMIT' )
    quitquiz = Button( win, 30, -90, 15, 4, 'red', 'QUIT QUIZ' )

    # Prints out the question
    question = Text( Point( 0, -72 ), LQ )
    question.setSize( 12 )
    question.draw( win )

    # Creates an answer box
    answerbox = Entry( Point( 0, -80 ), 5 )
    answerbox.setFill( 'cornsilk' )
    answerbox.draw( win )
    
    # Checks if the entered answer is correct or wrong
    while True:
        p = win.checkMouse()
        if p:
            if submitbut.clicked( p ):
                yourAnswer = answerbox.getText()
                
                if yourAnswer != LA:
                    answerbox.setFill( 'pink' )
                    if animal =="dog":
                        dog1.undraw_dog()
                        dog1.facebody(win,"sad")
                    if animal =="cat":
                        cat1.undraw_cat()
                        cat1.facebody(win,"sad")
                    if animal =="squirrel":
                        squi1.undraw_squi()
                        squi1.facebody(win,"sad")

                else:   
                    money.change(win,10)
                    answerbox.undraw()
                    question.undraw()
                    title.undraw()
                    submitbut.undraw()
                    quitquiz.undraw()
                    if animal =="dog":
                        dog1.undraw_dog()
                        dog1.facebody(win,"happy")
                    if animal =="cat":
                        cat1.undraw_cat()
                        cat1.facebody(win,"happy")
                    if animal =="squirrel":
                        squi1.undraw_squi()
                        squi1.facebody(win,"happy")
                    break
                                      
            if quitquiz.clicked( p ): # Quiz function breaks when quitauiz button is clicked
                question.undraw()
                answerbox.undraw()
                title.undraw()
                submitbut.undraw()
                quitquiz.undraw()
                break

class Energy:
    ''' A series of functions related to energy computing and drawing such as adding energy when given food and 
    decreasing energy over time.
    '''

    def __init__(self,win):

        ''' Set initial energy value and meter
        '''

        self.energy=100 # initial energy = 100
        self.energybox=MyRectangle(80,80,10,3) # create energy bar (outside)
        self.energymeter=Rectangle(Point(70,77),Point(90,83)) # create energy bar (inside)
        self.energymeter.setFill("blue")
        self.energymeter.setOutline("blue")
        energylabeltext=Text(Point(50,80),"Energy:") # create the label
        energylabeltext.draw(win)
        self.energytext=Text(Point(65,80),self.energy) # show the actual numeric value of energy
        self.energybox.draw(win)
        self.energymeter.draw(win)

    def decrease(self,win):

        ''' Decrease energy over time
        '''
        
        self.energy=self.energy-1 # when the method is called (in main function), energy decreases by 1

        # if energy < 0: game over
        if self.energy<0:
            self.energy=0
            self.energymeter=Rectangle(Point(70,77),Point(70,77))
            time.sleep(3) # wait for 3 seconds
            win.close() # close the window
            

        self.energymeter.undraw() # undraw the original bar (so that we can draw a new one)
        self.energytext.undraw() # undraw the original number (so that we can draw a new one)
        self.energytext=Text(Point(65,80),self.energy) # new energy value
        self.energymeter=Rectangle(Point(70,77),Point(70+self.energy/100*20,83)) # new energy bar
        self.energymeter.draw(win)
        self.energytext.draw(win)
        self.energymeter.setFill("blue")
        self.energymeter.setOutline("blue")

    def fishadd(self,win,animal):

        ''' Add energy after fish button is clicked
        '''

        # dog and squirrel: add 5; cat: add 10
        if animal=="dog":
            self.energy=self.energy+5
        if animal=="cat":
            self.energy=self.energy+10
        if animal=="squirrel":
            self.energy=self.energy+5

        # maximum level of energy is 100
        if self.energy>100:
            self.energy=100
            
        self.energymeter.undraw() # undraw the original bar (so that we can draw a new one)
        self.energytext.undraw() # undraw the original number (so that we can draw a new one)
        self.energymeter=Rectangle(Point(70,77),Point(70+self.energy/100*20,83)) # nwe energy bar
        self.energytext=Text(Point(65,80),self.energy) # new energy value
        self.energymeter.setFill("blue")
        self.energymeter.setOutline("blue")
        self.energymeter.draw(win)
        self.energytext.draw(win)

    def nutadd(self,win,animal):

        ''' Add energy after nut button is clicked
        '''

        # dog and cat: add 5; squirrel: add 10
        if animal=="dog":
            self.energy=self.energy+5
        if animal=="cat":
            self.energy=self.energy+5
        if animal=="squirrel":
            self.energy=self.energy+10

        # maximum level of energy is 100
        if self.energy>100:
            self.energy=100
            
        self.energymeter.undraw()
        self.energytext.undraw()
        self.energymeter=Rectangle(Point(70,77),Point(70+self.energy/100*20,83))
        self.energytext=Text(Point(65,80),self.energy)
        self.energymeter.setFill("blue")
        self.energymeter.setOutline("blue")
        self.energymeter.draw(win)
        self.energytext.draw(win)
        
    def beefadd(self,win,animal):

        ''' Add energy after beef button is clicked
        '''

        # cat and squirrel: add 5; dog: add 10
        if animal=="dog":
            self.energy=self.energy+10
        if animal=="cat":
            self.energy=self.energy+5
        if animal=="squirrel":
            self.energy=self.energy+5

        # maximum level of energy is 100
        if self.energy>100:
            self.energy=100
            
        self.energymeter.undraw()
        self.energytext.undraw()
        self.energymeter=Rectangle(Point(70,77),Point(70+self.energy/100*20,83))
        self.energytext=Text(Point(65,80),self.energy)
        self.energymeter.setFill("blue")
        self.energymeter.setOutline("blue")
        self.energymeter.draw(win)
        self.energytext.draw(win)

            
class Money:
    ''' a class to purchase decorations and food for pet.
        User starts with $10 and can finish quiz to gain money.
        Food and decorations cost $5 or $10.

    '''
    
    def __init__(self,win):
        '''Start with $10
           the amount of money is printed in the upper left part of the window
        '''
        
        self.money=10 # initial money = 10
        self.label = "Money: $ {}".format(self.money) # create the label that shows the amount of money
        self.moneytext = Text(Point(65, 70), self.label) # create the text object which contains the label above
        self.moneytext.draw(win)

    def isEnough(self,fishbut,nutbut,beefbut,treebut,sockbut):
        '''deactivate buttons when money is less than price'''
        
        # if money < 10: deactivate fish, nut, beef, tree buttons
        if  self.money < 10:
            fishbut.deactivate()
            nutbut.deactivate()
            beefbut.deactivate()
            treebut.deactivate()

        # if money < 5: deactivate sock button
        if self.money<5:
            sockbut.deactivate()
            
    def gain(self,fishbut,nutbut,beefbut,treebut,sockbut,numt,nums):
        '''if money >= 5 after taking quiz, activate sock button;
            if money >= 10,activate other buttons'''
        
        if self.money >= 10:
            fishbut.activate()
            nutbut.activate()
            beefbut.activate()
        if self.money >= 10 and numt==0: # numt is to make sure christmas tree is purchased only once
            treebut.activate()
        if self.money >= 5 and nums==0: # nums is to make sure sock is purchased only once
            sockbut.activate()

    def change(self,win,value):
        ''' change money when buying or winning the quiz
        '''
        self.money=self.money+value # add/subtract money
        self.moneytext.undraw() # undraw the original text (so that we can draw new text)
        self.label = "Money: $ {}".format(self.money) # create new label
        self.moneytext = Text(Point(65, 70), self.label) # create new text
        self.moneytext.draw(win)

   
class Christmasdec:
    '''the class of two Christmas decorations (sock and Christamas tree),
        and the figures for three food options
    '''

    def __init__(self, win, x, y, size):
        '''creates different parts of decorations and store as local variable.
            x and y are the position inputs of images, and size is the size input of images
        '''
    #christmas tree
        x = -50
        y = 74
        self.tree1 = Text(Point(x,y+size*10), '*')
        self.tree1.setSize(35)
        self.tree1.setTextColor('green')
        self.tree2 = Polygon(Point(x+size*2,y),Point(x,y+size*10),Point(x-size*2,y))
        self.tree2.setFill('green')
        self.tree2.setOutline('green')
        self.tree3 = Polygon(Point(x+size*4,y),Point(x,y+size*8),Point(x-size*4,y))
        self.tree3.setFill('green')
        self.tree3.setOutline('green')
        self.tree4 = Polygon(Point(x+size*6,y),Point(x,y+size*6),Point(x-size*6,y))
        self.tree4.setFill('green')
        self.tree4.setOutline('green')
        self.tree5 = Polygon(Point(x+size*8,y),Point(x,y+size*3),Point(x-size*8,y))
        self.tree5.setFill('green')
        self.tree5.setOutline('green')
        self.tree6 = Polygon(Point(x+size*7,y),Point(x,y+size*1),Point(x-size*8,y))
        self.tree6.setFill('green')
        self.tree6.setOutline('green')
        self.tree7 = Polygon(Point(x+size*8,y-size*1.7),Point(x,y+size),Point(x-size*8.5,y-size*2))
        self.tree7.setFill('green')
        self.tree7.setOutline('green')
        self.tree8 = Polygon(Point(x+size*10,y-size*3.5),Point(x,y-size*1.2),Point(x-size*9,y-size*3.4))
        self.tree8.setFill('green')
        self.tree8.setOutline('green')
        self.tree9 = Polygon(Point(x+size*10.8,y-size*5),Point(x,y-size*2),Point(x-size*10.8,y-size*5.2))
        self.tree9.setFill('green')
        self.tree9.setOutline('green')
        self.tree10 = Polygon(Point(x+size,y-size*8),Point(x,y-size*2),Point(x-size,y-size*8))
        self.tree10.setFill('brown')
        self.tree10.setOutline('brown')
        
     #sock
        x = 33
        size = 5
        self.sock1=Circle(Point(x+size*0.2,y),size)
        self.sock1.setFill('#B60043')
        self.sock1.setOutline('#B60043')
        self.sock2= Oval(Point(x-size*3.6, y-size*1.2), Point(x+size*0.7, y+size*0.8))
        self.sock2.setFill('#E93636')
        self.sock2.setOutline('#E93636')
        self.sock3 = Rectangle(Point(x-size*0.8,y-size*0.7),Point(x+size*0.8,y+size*4))
        self.sock3.setFill('pink')
        self.sock3.setOutline('pink')
        self.sock4 = Rectangle(Point(x-size*0.8,y+size*5),Point(x+size*0.8,y+size*4))
        self.sock4.setFill('#F783CD')
        self.sock4.setOutline('#F783CD')
        self.sock5= Oval(Point(x-size*3.5, y-size*1.2), Point(x+size*0.9, y+size*0.8))
        self.sock5.setFill('#E93636')
        self.sock5.setOutline('#E93636')

    #bone
        size = 2
        self.bone1 = Circle(Point(74-2*size,-5+3*size),size)
        self.bone2 = Circle(Point(74-2*size,-5+size),size)
        self.bone3 = Circle(Point(74+4*size,-5+3*size),size)
        self.bone4 = Circle(Point(74+4*size,-5+size),size)
        self.bone5 = Oval(Point(74-2*size,-5+2.8*size),Point(74+4*size,-5+size))
        self.bone1.setFill('SlateGray3')
        self.bone2.setFill('SlateGray3')
        self.bone3.setFill('SlateGray3')
        self.bone4.setFill('SlateGray3')
        self.bone5.setFill('SlateGray3')
        self.bone1.setOutline('SlateGray3')
        self.bone2.setOutline('SlateGray3')
        self.bone3.setOutline('SlateGray3')
        self.bone4.setOutline('SlateGray3')
        self.bone5.setOutline('SlateGray3')
        
        #fish
        self.fish1 = MyOval( 75+5.6, -41, 1, 4)
        self.fish1.setFill('#FF9E2F')
        self.fish1.setOutline('#FF9E2F')
        self.fish2 = MyOval( 75, -41, 6, 3 )
        self.fish2.setFill( '#FC7E2A' )
        self.fish2.setOutline( '#FC7E2A' )
        self.fish3 = Circle( Point(75-2.8,-41+0.8), 1 )
        self.fish3.setFill( 'white' )
        self.fish3.setOutline( 'white' )

        #acorn
        self.acron1= MyOval(74,-21,3.5,3)
        self.acron1.setFill('#97511C')
        self.acron1.setOutline('#97511C')
        self.acron2 = Rectangle(Point(74-0.5,-21+2),Point(74+0.5,-21+4.5))
        self.acron2.setFill('#8E7120')
        self.acron2.setOutline('#8E7120')
        self.acron3 = Polygon(Point(74-2.2,-21-0.8),Point(74+2.2,-21-0.6),Point(74,-21-4))
        self.acron3.setFill('#97511C')
        self.acron3.setOutline('#97511C')
        self.acron4= MyOval(74,-21+2,2.8,1)
        self.acron4.setFill('#A47B0C')
        self.acron4.setOutline('#A47B0C')
        
    def Christmastree(self, win):
        '''draw the parts of Christmas tree in the window'''
        
        self.tree10.draw(win)
        self.tree1.draw(win)
        self.tree2.draw(win)
        self.tree3.draw(win)
        self.tree4.draw(win)
        self.tree5.draw(win)
        self.tree6.draw(win)
        self.tree7.draw(win)
        self.tree8.draw(win)
        self.tree9.draw(win)
        
        
    def Sock(self,win):   
        '''draw sock in the window'''
        self.sock4.draw(win)
        self.sock3.draw(win)
        self.sock2.draw(win)
        self.sock5.draw(win)
        self.sock1.draw(win)

    def bone(self, win):
        '''draw bone in the window'''
        self.bone1.draw(win)
        self.bone2.draw(win)
        self.bone3.draw(win)
        self.bone4.draw(win)
        self.bone5.draw(win)

    def fish(self, win):
        '''draw the image fish in the window'''
        self.fish1.draw(win)
        self.fish2.draw(win)
        self.fish3.draw(win)
        
    def acorn(self,win):
        '''draw acorn in the window'''
        self.acron1.draw(win)
        self.acron2.draw(win)
        self.acron3.draw(win)
        self.acron4.draw(win)

def main():
    '''select one pet from three options (dog,cat,squirrel) by clicking the buttom below the pet figure
        time decrease as game goes on, remaining time is shown by the blue rectangle
        pets start with flat face and change emotions: pets get happy if user feed the pet and turn sad if user failed in quiz
    '''
    #construct the window
    win = GraphWin( "Tamagotchi",500,500,autoflush=False)
    bgcolor="white"
    win.setBackground( bgcolor )
    win.setCoords( -100, -100, 100, 100)

    #buttons to select corresponding pet
    catbut = CreateButton( win,-4, -60,15,8, "#66676b", '' )
    dogbut = CreateButton( win,-68,-60,15,8, 'tan', '' )
    sqbut = CreateButton( win, 56, -60, 15,8, '#f0e68c', '' )

    #draw initial three pet figures with happy face
    cat=Cat(win,-5,16,1.8,"white")
    cat.facebody(win,"happy")

    dog=Dog(win,-68,20,7)
    dog.facebody(win,"happy")

    squi = squirrel( win, 75, -5,5)
    squi.facebody(win,'happy')

    #draw the selected pet figure with flat face once the one pet is selected by user
    cat1=Cat(win,-8,30,3,"white")
    dog1=Dog(win,0,25,12)
    squi1 = squirrel( win, 16,-5,8)



    while True:
        p = win.checkMouse()
        
        if p: # Mouse was clicked
            if PtInRect(p, catbut):
                #if click is inside the button, undraw all three characters,
                #draw the selected character with bigger size and flat emotion in the center of the window
                dog.undraw_dog( )
                squi.undraw_squi( ) 
                cat.undraw_cat( )
                
                dogbut.undraw( )
                catbut.undraw( )
                sqbut.undraw( ) 
                
                cat1.facebody(win,"flat")

                animal = 'cat'

                break

            elif PtInRect(p, dogbut):
                #if click is inside the button, undraw all three characters,
                #draw the selected character with bigger size and flat emotion in the center of the window
                cat.undraw_cat( )
                squi.undraw_squi( )
                dog.undraw_dog( )
                
                dogbut.undraw( )
                catbut.undraw( )
                sqbut.undraw( )
                
                dog1.facebody(win,"flat")

                animal = 'dog'

                break
                
            elif PtInRect(p, sqbut):
                #if click is inside the button, undraw all three characters,
                #draw the selected character with bigger size and flat emotion in the center of the window
                dog.undraw_dog( )
                cat.undraw_cat( )
                squi.undraw_squi( )
                
                dogbut.undraw( )
                catbut.undraw( )
                sqbut.undraw( ) 
                squi1.facebody(win,'flat')

                animal = 'squirrel' 

                break
            
    #construct three food buttons        
    fishbut=Button(win, 75, -50, 15, 3, "white", "Fish:$10")
    nutbut=Button(win, 75, -30, 15, 3, "white", "Nut:$10")
    beefbut=Button(win, 75, -10, 15, 3, "white", "Bone:$10")

    #chat button & quiz button
    ChatButton = Button( win, -80, 50, 7, 4, 'plum', 'Chat' )
    QuizButton = Button( win, -80, 30, 7, 4, 'sky blue', 'Quiz' )
    
    #decoration button
    treebut = Button( win, -80, -30, 18, 4, 'wheat', 'Xmas Tree: $10' )
    sockbut = Button( win, -80, -50, 15, 4, 'wheat', 'Sock: $5' )
    
    #quit button
    quitallbut = Button( win, -90, 90, 10, 10, 'red', 'QUIT' )
    
    #recall enery and money class in main
    energy=Energy(win)
    money=Money(win)

    # For decorations
    xcent,ycent = 0,0
    xrand,yrand = randint(-20,20), randint(-20,20)
    size = 2
    dec = Christmasdec(win, xcent, ycent, size)
    dec.bone( win )
    dec.acorn( win )
    dec.fish( win )  

    #count numbers of treesbutton and socksbutton clicked
    numt,nums = 0,0

    
    starttime=time.time() # record the time when starting the game
    olddiff=0 # used for time calculation in the while loop
    
    while True:
        currenttime=time.time() # current time
        diff=round(currenttime-starttime,3) # the time that the user has played (floating point number, round to 3 digits)
        
        
        if animal=="dog": # dog: most difficult: energy decreases by 1 every 1 second
            if diff-olddiff>=1:
                energy.decrease(win)
                olddiff=diff
                
        if animal=="cat": # cat: moderately difficult: energy decreases by 1 every 2 seconds
            if diff-olddiff>=2:
                energy.decrease(win)
                olddiff=diff
                
        if animal=="squirrel": # squirrel: least difficult: energy decreases by 1 every 3 seconds
            if diff-olddiff>=3:
                energy.decrease(win)
                olddiff=diff

        p = win.checkMouse()  #get the position where the user clicked inside the window
        
        if p:

            # if any food button is clicked : if the button is active, add energy, decrease money, change pet's emotion
            if fishbut.clicked(p):
                if fishbut.active==True:
                    energy.fishadd(win,animal)
                    money.change(win,-10)
                    if animal =="dog":
                        dog1.undraw_dog()
                        dog1.facebody(win,"happy")
                    if animal =="cat":
                        cat1.undraw_cat()
                        cat1.facebody(win,"happy")
                    if animal =="squirrel":
                        squi1.undraw_squi()
                        squi1.facebody(win,"happy")
                    money.isEnough(fishbut,nutbut,beefbut,treebut,sockbut)  # check if any button should be deactivated
                    
                    
            elif nutbut.clicked(p):
                if nutbut.active==True:
                    energy.nutadd(win,animal)
                    money.change(win,-10)
                    if animal =="dog":
                        dog1.undraw_dog()
                        dog1.facebody(win,"happy")
                    if animal =="cat":
                        cat1.undraw_cat()
                        cat1.facebody(win,"happy")
                    if animal =="squirrel":
                        squi1.undraw_squi()
                        squi1.facebody(win,"happy")
                    money.isEnough(fishbut,nutbut,beefbut,treebut,sockbut)

            elif beefbut.clicked(p):
                if beefbut.active==True:
                    energy.beefadd(win,animal)
                    money.change(win,-10)
                    if animal =="dog":
                        dog1.undraw_dog()
                        dog1.facebody(win,"happy")
                    if animal =="cat":
                        cat1.undraw_cat()
                        cat1.facebody(win,"happy")
                    if animal =="squirrel":
                        squi1.undraw_squi()
                        squi1.facebody(win,"happy")
                    money.isEnough(fishbut,nutbut,beefbut,treebut,sockbut)
            
            elif ChatButton.clicked( p ): # Activates Chat function when clicked
                Chat2( win,animal,dog1,cat1,squi1 )

            elif QuizButton.clicked( p ): # Activates Quiz function when clicked
                n = randint(0,9)
                quiz( win, money,animal,dog1,cat1,squi1,n )
                money.gain(fishbut,nutbut,beefbut,treebut,sockbut,numt,nums)
                
                
            elif treebut.clicked( p ): # Draws a christmas tree
                if treebut.active==True:
                    numt += 1 #if the button clicked, number of times tree button is clicked increases by 1
                    if numt == 1:
                        dec.Christmastree(win)
                        money.change( win,-10)
                        money.isEnough(fishbut,nutbut,beefbut,treebut,sockbut) # check if money is enough to buy things
                        treebut.deactivate( )
                    else:
                        #tree decoration can only be selected once
                        #deactivate tree button if the button is clicked more than once
                        treebut.deactivate( )
                        
            elif sockbut.clicked( p ): # Draws a sock
                if sockbut.active==True:
                    nums += 1 #if the button clicked, number of the sock button clicked increases by 1
                    if nums == 1:
                        dec.Sock( win )
                        money.change( win,-5 )
                        money.isEnough(fishbut,nutbut,beefbut,treebut,sockbut) # check if money is enough to buy things
                        sockbut.deactivate()
                        
                    else:
                        #sock decoration can only be selected once
                        #deactivate sock button if the button is clicked more than once
                        sockbut.deactivate()
                
            elif quitallbut.clicked( p ): # close the game if quit button is clicked
                win.close()
                break

main()


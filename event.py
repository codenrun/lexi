import os
import math



KEY_PRESS = 2;
KEY_RELEASE = 3;
MOUSE_PRESS = 4  ;
MOUSE_RELEASE = 5;
MOUSE_MOVE = 5;


QUIT = 7;
MOUSE = 8;
KEYBOARD = 9;


K_a = 'a'    
K_b =  'b' 
K_c =  'c'     
K_d =  'd'     
K_e =  'e'     
K_f   =  'f'    
K_g  =  'g'    
K_h  =  'h'    
K_i   =  'i'    
K_j =  'j'      
K_k =  'k'     
K_l   =  'l'    
K_m  =  'm'   
K_n  =  'n'    
K_o  =  'o'    
K_p  =  'p'    
K_q   =  'q'   
K_r   =  'r'    
K_s   =  's'   
K_t   =  't'   
K_u  =  'u'    
K_v   =  'v'   
K_w  =  'w'   
K_x  =  'x'    
K_y   =  'y'   
K_z  =  'z' 
K_0   =    '0'
K_1   =    '1'
K_2   =    '2'
K_3    =   '3'
K_4    =   '4'
K_5    =   '5'
K_6    =   '6'
K_7    =   '7'
K_8    =   '8'
K_9    =   '9' 
K_UNKN = ''
K_SPACE =' '
K_BACKSPACE ='\b'
K_UP     = 401        
K_DOWN = 402               
K_RIGHT = 403              
K_LEFT  = 404
K_RETURN = '\r'

class Eventing():
	def GetEvents(self):
		pass;
		
class Event():
	def __init__(self,event):
		self.bLeftButtonDown = False;
		self.bLeftButtonUp = False;
		self.bRightButtonDown = False;
		self.bRightButtonUp = False;
		self.bMouseMoved = False;
		self.mousePosition = (-1,-1)
		self.bDragging = False;
		self.dragDelta = (0,0);
		
		self.type = None;
		self.device = None;
		self.keyCode = None;


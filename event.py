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

K_UNKN = -1
K_BACKSPACE ='\b'
K_UP     = 401        
K_DOWN = 402               
K_RIGHT = 403              
K_LEFT  = 404
K_RETURN = '\r'
K_BOLD = 520


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


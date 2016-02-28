import os
import pygame
import math
import gfx 
import event 

from pygame.locals import *
from pygame.color import THECOLORS



class PyGameWindowImpl:
	
	def __init__(self, screen , size ):
		self.screen = screen;
		self.background = pygame.Surface(size)
		self.background = self.background.convert()
		self.background.fill((250, 250, 250))
		self.Font = pygame.font.SysFont(None, 35);
		self.pos = (0,0);
		self.size = size;
		
	def SetTitle(self, title):
		pygame.display.set_caption(title);	
		
	def Render(self)	:
		pygame.draw.rect(self.background, (0,255,10),self.background.get_rect(), 2);
		self.screen.blit(self.background, self.pos);
		
	def SetPosition(self,pos):
		self.pos = pos;
			
	
	def RenderChar( self, ch, pos, col ,bg):
		ch_surface = self.Font.render( ch , 1, col ,bg )
		self.background.blit( ch_surface , pos);       

	def GetCharExtents(self,ch):
		return self.Font.size(ch);
		
	def MakeImage(self, imagePath):
		return pygame.image.load(imagePath);
		
	def RenderImage(self, imageSurface , imageArea):
		imageSurface = pygame.transform.smoothscale(imageSurface, (imageArea[2], imageArea[3]))
		self.background.blit(imageSurface, (imageArea[0], imageArea[1]));
		pygame.draw.rect(self.background, (255,0,0), imageArea, 1);

	def GetImageExtents(self, imageSurface):
		return imageSurface.get_size();
		
	def RenderRect(self, rect ):
		pygame.draw.rect(self.background, (10,10,10),rect, 2);
	
	def ClearRect(self, rect ):
		pygame.draw.rect(self.background, (255,255,255),rect,0);


	

class PyGameGFX(gfx.GFX):
	def __init__(self):
		self.screen = None;
		
	def Init(self):
		pygame.init();
		self.screen = pygame.display.set_mode((1000, 500));
		pygame.mouse.set_visible(1)
		pygame.key.set_repeat (500, 30)


	def Blit(self):
		pygame.display.flip()



	def Context(self):
		return self.screen;
	
	def GetImplemenation(self,type,size):
		if type is  'Window':
			return PyGameWindowImpl(self.screen,size);

		return None;

	def Quit(self):
		pygame.quit();





class PyGameEvent(event.Event):
	def __init__(self, e):
		event.Event.__init__(self,e);
		
		if e.type == KEYDOWN:
			print "KEYDOWN"

			self.device = event.KEYBOARD;
			self.type = event.KEY_PRESS;
			self.keyCode = self.get_key_code(e.key);
		if e.type == KEYUP:			
			self.device = event.KEYBOARD;
			self.type = event.KEY_RELEASE;
			self.keyCode = self.get_key_code(e.key);
		if e.type == MOUSEMOTION:
			(leftDown,middleDown,rightDown) = e.buttons;
			self.bLeftButtonDown = leftDown;
			self.bLeftButtonUp = not leftDown;
			self.bRightButtonDown = rightDown;
			self.bRightButtonUp = not rightDown;
			self.mousePosition = e.pos;
			self.bMouseMoved = True;
			self.device = event.MOUSE;
			self.type = event.MOUSE_MOVE;
			
			
		if self.bLeftButtonDown :			
			self.bDragging = True;
			self.dragDelta = e.rel;
			
		elif e.type == MOUSEBUTTONUP:
			self.bLeftButtonDown = False;
			self.bLeftButtonUp = e.button == 1;
			self.bRightButtonDown = False;
			self.bRightButtonUp = e.button == 3;
			self.mousePosition = e.pos;
			self.bMouseMoved = False;
			self.type = event.MOUSE_RELEASE;
			self.device = event.MOUSE;

		elif e.type == MOUSEBUTTONDOWN:
			self.bLeftButtonUp = False;
			self.bLeftButtonDown = e.button == 1;
			self.bRightButtonUp = False;
			self.bRightButtonDown = e.button == 3;
			self.mousePosition = e.pos;
			self.bMouseMoved = False;
			self.type = event.MOUSE_PRESS;
			self.device = event.MOUSE;
			
		elif  e.type == pygame.QUIT:
			self.type = event.QUIT
	def get_key_code(self, pyKeyCode):
		print "get_key_code", pyKeyCode , pygame.K_LEFT, pyKeyCode == pygame.K_LEFT

		if pyKeyCode is pygame.K_a:
			return event.K_a 
		if pyKeyCode is pygame.K_b:
			return event.K_b 
		if pyKeyCode is pygame.K_c:
			return event.K_c 
		if pyKeyCode is pygame.K_d:
			return event.K_d 
		if pyKeyCode is pygame.K_e:
			return event.K_e 
		if pyKeyCode is pygame.K_f :
			return event.K_f  
		if pyKeyCode is pygame.K_g :
			return event.K_g 
		if pyKeyCode is pygame.K_h :
			return event.K_h 
		if pyKeyCode is pygame.K_i  :
			return event.K_i  
		if pyKeyCode is pygame.K_j :
			return event.K_j 
		if pyKeyCode is pygame.K_k :
			return event.K_k  
		if pyKeyCode is pygame.K_l  :
			return event.K_l  
		if pyKeyCode is pygame.K_m:
			return event.K_m
		if pyKeyCode is pygame.K_n :
			return event.K_n 
		if pyKeyCode is pygame.K_o :
			return event.K_o 
		if pyKeyCode is pygame.K_p :
			return event.K_p 
		if pyKeyCode is pygame.K_q :
			return event.K_q 
		if pyKeyCode is pygame.K_r  :
			return event.K_r  
		if pyKeyCode is pygame.K_s :
			return event.K_s 
		if pyKeyCode is pygame.K_t :
			return event.K_t 
		if pyKeyCode is pygame.K_u :
			return event.K_u 
		if pyKeyCode is pygame.K_v :
			return event.K_v 
		if pyKeyCode is pygame.K_w:
			return event.K_w
		if pyKeyCode is pygame.K_x :
			return event. K_x  
		if pyKeyCode is pygame.K_y :
			return event.K_y 
		if pyKeyCode is pygame.K_z :
			return event. K_z  
		if pyKeyCode is pygame.K_0  :
			return event.K_0 
		if pyKeyCode is pygame.K_1 :
			return event.K_1 
		if pyKeyCode is pygame.K_2 :
			return event.K_2 
		if pyKeyCode is pygame.K_3 :
			return event.K_3  
		if pyKeyCode is pygame.K_4 :
			return event. K_4  
		if pyKeyCode is pygame.K_5 :
			return event.K_5  
		if pyKeyCode is pygame.K_6 :
			return event.K_6  
		if pyKeyCode is pygame.K_7:
			return event.K_7  
		
		if pyKeyCode is pygame.K_8 :
			return event.K_8  
		
		if pyKeyCode is pygame.K_9    :
			return event.K_9  
		
		if pyKeyCode is pygame.K_SPACE:
			return event.K_SPACE  
		
		if pyKeyCode is pygame.K_BACKSPACE:
			return event.K_BACKSPACE  
		
		if pyKeyCode == pygame.K_UP:
			return event.K_UP  
		
		if pyKeyCode == pygame.K_DOWN:
			return event.K_DOWN  
		
		if pyKeyCode == pygame.K_RIGHT:
			return event.K_RIGHT  
		
		if pyKeyCode == pygame.K_LEFT:
			return event.K_LEFT  
		
		if pyKeyCode == pygame.K_RETURN:
			return event.K_RETURN  	

		return event.K_UNKN;
		
		
		
		
		
class PyGameEventing(event.Eventing):
	def GetEvents(self):
		events = [];
		for event in pygame.event.get():
			events.append(PyGameEvent(event));
		return events;















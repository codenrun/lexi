import os
import pygame
import math

from pygame.locals import *
from pygame.color import THECOLORS



	
implType = 'pygame'
screen = None;
background = None;



def PygameInit():
	global screen;
	global background;
	pygame.init()
	screen = pygame.display.set_mode((1000, 500));
	pygame.mouse.set_visible(1)
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	print "PygameInit"

class PyGameWindowImpl:
	screen = None;
	def __init__(self, screen):
		self.screen = screen;
		
	def RenderChar( self, ch, pos, col):
		_font = pygame.font.SysFont(None, 15)
		_ch = _font.render( ch , 1, col )
		textpos = _ch.get_rect(centerx=pos[0], centery=pos[1])
		background.blit( _ch , textpos);       

	

def Init():
	if implType is 'pygame':
		PygameInit();

	
def GetImplemenation(type):
	if type is  'Window':
		if implType is 'pygame':
			return PyGameWindowImpl(screen);

	return None;



class Window():
	def __init__(self):
		self.impl = GetImplemenation('Window') ;
		
	def RenderChar( self, ch, pos, col):
		self.impl.RenderChar(ch, pos,col);
	def RenderImage(self, imagePath , imageArea):
		pass;
	def GetExtents( self, ch):
		pass;
	def GetExtents():
		pass;
		
		

		


		
class Glyph():
	def __init__(self):
		self.pos = (0,0);
	
	def Render(self, window):
		pass;
		
	def Intersects(self, pos ):
		pass;
		
	def Insert( self, glyph , at ):
		pass;
		
	def Bounds():
		pass;
		
	def SetPosition( self, pos):
		self.pos = pos ;


class CharGlyph(Glyph):
	def __init__(self):
		Glyph.__init__(self);
		self.ch='';
		self.color=(10,10,10);
		
	def SetChar(self, ch):
		self.ch = ch;
	def Render(self, window):
		window.RenderChar( self.ch, self.pos, self.color);
	def Bounds():
		pass;
	def SetColor(self, col):
		self.color = col;	
		
class ImageGlyph(Glyph):
	def __init__(self):
		pass;
	def SetImage(self, imagePath ):
		pass;
	def Render(self, window):
		pass;
	def Bounds():
		pass;

		
class RowGlyph(Glyph):
	def __init__(self):
		pass;
	def Render(self, window):
		pass;
		
	def Intersects(self, p):
		pass;
		
	def Insert( self, g , at ):
		pass;
	def Bounds():
		pass;

		
class ColGlyph(Glyph):
	def __init__(self):
		pass;
	def Render(self, window):
		pass;
		
	def Intersects(self, p):
		pass;
		
	def Insert( self, g , at ):
		pass;
	def Bounds():
		pass;


class Compositor():
	def Compose(self):
		pass;
		


Init();		

window = Window();		

ch = CharGlyph();
ch.SetChar('a');
ch.SetPosition( (100,100));
ch.Render(window);
ch = CharGlyph();
ch.SetChar('b');
ch.SetPosition( (105,100));
ch.Render(window);


screen.blit(background, (0, 0))
pygame.display.flip()
screen.blit(background, (0, 0))

while(1):
	pass;	
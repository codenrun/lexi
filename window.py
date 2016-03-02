import os
import math
import event
import compositors

from composition import *
from glyphs import * 

class Window():
	def __init__(self, gc, size, pos):
		self.impl = gc.GetImplemenation('Window' , size ) ;	
		self.composition = Composition(self);
		self.composition.SetSize(size);
		self.composition.SetPosition((10,10));
		 
	def SetCompositor(self, compositor):
		self.compositor = compositor;
		
	def SetPosition(self,pos):
		self.impl.SetPosition(pos);
	
	
	def SetTitle(self, title):
		self.impl.SetTitle(title);		
	 
	def Intersects(self, pos ):
		pos_x , pos_y = pos;
		x,y,w,h = self.Bounds();
		
		##print " mouse-pos" , pos
		##print " rect " , self.Bounds()
		result =  pos_x >= x and pos_x <= x + w and pos_y >= y and pos_y <= y + h;
		return result;
	
	
	def Bounds(self):
		x,y = self.impl.pos;
		w,h = self.impl.size;
		return x,y,w,h;
		
	def Render(self):
		self.composition.Render();
		self.impl.Render();
		
	def HandleInput(self, e):		
		if e.device == event.MOUSE:
			if(self.Intersects(e.mousePosition)):
				rel_mousePosition = e.mousePosition[0] - self.impl.pos[0] , e.mousePosition[1] - self.impl.pos[1] 
				e.mousePosition= rel_mousePosition;
				self.composition.HandleInput(e);
				##print "Window : Got event ";
				self.Render();
				return True;
		if e.device == event.KEYBOARD:
			self.composition.HandleInput(e);
			##print " Window : Got event ";
			self.compositor.Compose(self.composition);
			self.Render();
			return True;	
		return False;
	def RenderChar( self, ch, pos, fgColor, bgColor, bBold):
		self.impl.RenderChar(ch, pos,fgColor , bgColor, bBold);	
	
	def GetCharExtents( self, ch):
		return self.impl.GetCharExtents(ch);

	def MakeImage(self, imagePath):
		return self.impl.MakeImage(imagePath);
		
	def RenderImage(self, image , imageArea):
		self.impl.RenderImage(image, imageArea);
		
	def GetImageExtents(self, image):
		return self.impl.GetImageExtents(image);
		
	def RenderRect(self, rect ):
		self.impl.RenderRect(rect);
		
	def ClearRect(self, rect ):
		self.impl.ClearRect(rect);	




		

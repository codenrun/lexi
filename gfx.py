import os
import pygame
import math
import event



class GFX():
	def __init__(self):
		pass;
		
	def Init(self):
		pass;
		
	def Blit(self):
		pass;
		
	def GetImplemenation(self,type , size ):
		pass;
		
	def Quit(self):
		pass;
	
			

import PygameGfx

def MakeGFX( type ):
	if type is 'pygame':
		return PygameGfx.PyGameGFX();


def MakeEventing( type ):
	if type is 'pygame':
		return PygameGfx.PyGameEventing();


		
		



class Window():
	def __init__(self, gc, size):
		self.impl = gc.GetImplemenation('Window' , size ) ;
		self.body = EditableColGlyph(self);
		self.body.SetSize((size[0], size[1]));
	def SetPosition(self,pos):
		self.impl.SetPosition(pos);
			
	
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
		self.body.Render();
		self.impl.Render();
		
	def HandleInput(self, e):		
		if e.device == event.MOUSE:
			if(self.Intersects(e.mousePosition)):
				rel_mousePosition = e.mousePosition[0] - self.impl.pos[0] , e.mousePosition[1] - self.impl.pos[1] 
				e.mousePosition= rel_mousePosition;
				self.body.GetHitGlyph(rel_mousePosition).HandleInput(e);
				##print "Window : Got event ";
				self.Render();
				return True;
		if e.device == event.KEYBOARD:
			self.body.HandleInput(e);
			##print " Window : Got event ";
			self.Render();
			return True;	
		return False;
	def RenderChar( self, ch, pos, fgColor, bgColor):
		self.impl.RenderChar(ch, pos,fgColor , bgColor);	
	
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




		
		
class Glyph():
	def __init__(self, window):
		self.pos = (0,0);
		self.window = window
		self.size = (0,0);
		self.parent = None;	

	def SetParent(self, parent):
		self.parent = parent;
		
	def Render(self, window):
		pass;
		
	def Intersects(self, pos ):
		pos_x , pos_y = pos;
		x,y,w,h = self.Bounds();
		result =  pos_x >= x and pos_x <= x + w and pos_y >= y and pos_y <= y + h;
		return result;
		
	def Insert( self, glyph , at ):
		pass;
		
	def Bounds(self):
		#print "Glyph::Bounds"
		return (self.pos[0],self.pos[1], self.size[0],self.size[1]);
		
	def SetPosition( self, pos):
		self.pos = pos ;

	def SetSize(self, size):
		self.size = size;

	def HandleInput( self, e ):
		if self.ProcessInput(e) is False:
			if self.parent is not None:
				self.parent.HandleInput(e);
		
	
	def ProcessInput(self,e):
		##print " glyph : got event",self
		return False;
		
	def GetHitGlyph(self, pos):	
		return self;


class CharGlyph(Glyph):
	def __init__(self, window):
		Glyph.__init__(self, window);
		self.ch='';
		self.color=(10,10,10);
		self.bg = (255,255,255);
		self.bSelect = False;
		
	def SetChar(self, ch):
		self.ch = ch;
	def Render(self):
		self.window.RenderChar( self.ch, self.pos, self.color, self.bg);
	def Bounds(self):
		#print "CharGlyph::Bounds"

		x,y =  self.pos[0], self.pos[1], 
		w,h = self.window.GetCharExtents(self.ch);
		return x,y,w,h;
	def SetColor(self, col):
		self.color = col;
	
	
	def ProcessInput(self,e):
		if e.type is event.MOUSE_PRESS:
			#self.bg = (0,255,0);
			pass;
			
		##print " char : got event",self
		return False;
		
	def Select(self , bSelect):
		self.bSelect = bSelect;
	
	def GetChar(self):
		return self.ch;
	
class ImageGlyph(Glyph):
	def __init__(self, window):
		Glyph.__init__(self, window);
		self.image = None;
		
	def SetPath(self, imagePath ):
		self.image = self.window.MakeImage(imagePath);
		self.size = self.window.GetImageExtents(self.image);
		
	def Render(self):
		self.window.RenderImage( self.image, self.Bounds());
		
	def Bounds(self):
		x,y =  self.pos[0], self.pos[1], 
		w,h = self.size[0], self.size[1];
		return x,y,w,h;		

	def ProcessInput(self,e):
		##print " ImageGlyph : got event",self
		return False;



class GroupedGlyph(Glyph):
	pass;

	
		
class RowGlyph(Glyph):
	def __init__(self, window):
		Glyph.__init__(self, window);
		self.children = [];
		
	def Render(self):
		
		for child in self.children:
			child.Render();
		
		
	def Insert( self, g , at ):
		#print at
		#print self	
		#print g;

		self.children.insert( at, g);
		
		#print self.children
		
		g.SetParent(self);
		self.AdjustChildPositions();
		return True;
		
	def Remove( self, at ):
		if len(self.children) is 0:
			return False;
		if at < 0 or at > len(self.children):
			return False;
		self.window.ClearRect(self.Bounds());
		self.children[at].SetParent(None);
		del self.children[at];
		self.AdjustChildPositions();
		return True
		
	def Bounds(self):
		#print "Row::Bounds"
		x,y,w,h = self.pos[0],self.pos[1],0,0;
		
		for child in self.children:
			x_child, y_child, w_child, h_child = child.Bounds();
			w = w + w_child;
			if h_child > h : h = h_child;
		return x,y, max(self.size[0] , w) ,max(self.size[1] , h);
		
	def SetPosition(self, pos):
		Glyph.SetPosition(self, pos);	
		self.AdjustChildPositions();
		
	def AdjustChildPositions(self):
		x,y= self.pos;
		for child in self.children:
			x_child, y_child, w_child, h_child = child.Bounds();
			child.SetPosition( (x, y));
			x = x + w_child;
			
	def ProcessInput(self,e):
		for child in self.children:
			if child.ProcessInput(e):
				return True;
		return False;

	def  GetChildren(self):
		return self.children;
		
	def GetHitGlyph(self, pos):	
		for child in self.children:
			if child.Intersects(pos):
				return child.GetHitGlyph(pos);
		return self;

	def Text(self):
		text = "";
		for child in self.children:
			if hasattr(child,'GetChar'):
				text = text + child.GetChar();
				
		return text;
		

class ColGlyph(RowGlyph):
	def __init__(self, window):
		RowGlyph.__init__(self, window);
		self.children = [];
		
		
		
	def Bounds(self):
		x,y,w,h = self.pos[0],self.pos[1],0,0;
		
		for child in self.children:
			x_child, y_child, w_child, h_child = child.Bounds();
			h = h + h_child;
			if w_child > w : w = w_child;
		return x,y, max(self.size[0] , w) ,max(self.size[1] , h);
		
		
	def AdjustChildPositions(self):		
		#print self.children

		x,y= self.pos;		
		#print x,y

		for child in self.children:	
			#print child
			#print child.Bounds()
			x_child, y_child, w_child, h_child = child.Bounds();
			child.SetPosition( (x, y));
			y = y + h_child;
			

		




		
class EditableRowGlyph(RowGlyph):
	def __init__(self, window):
		RowGlyph.__init__(self, window);
		self.cursor =  CharGlyph(window);
		self.cursor.SetChar('|');
		self.cursor.SetColor((255,0,0));
		self.cursorIndex = 0;
		
	def Render(self):
		RowGlyph.Render(self);
	def ProcessInput(self,e):
		#print " EditableRowGlyph : got event" , self
		
		if e.type is event.KEY_PRESS:
			#print "e.keyCode : ", e.keyCode 
			#print "before ",  self.cursorIndex, len(self.children)
			if e.keyCode == event.K_BACKSPACE:
				if self.Remove(self.cursorIndex-1):
					self.cursorIndex = self.cursorIndex -1;
			elif e.keyCode == event.K_LEFT :
				#print "left"
				if self.cursorIndex > 0 :
					self.cursorIndex = self.cursorIndex -1;
					return True;
				
			elif e.keyCode == event.K_RIGHT:
				#print "right"

				if self.cursorIndex < len(self.children):		
					self.cursorIndex = self.cursorIndex +1;		
					return True;
				
			else:	
				ch = CharGlyph(self.window);
				ch.SetChar(e.keyCode);
				if self.Insert(ch, self.cursorIndex):
					self.cursorIndex = self.cursorIndex +1;
			#print "after" , self.cursorIndex, len(self.children)

		if e.type is event.MOUSE_PRESS:
			rect = self.AcceptCursor(e.mousePosition)
			self.cursor.SetPosition((rect[0], rect[1]));
			##print e.mousePosition
			##print rect
			self.cursor.Render();
		return False;	
		
	def AcceptCursor(self, cursorPosition ):
		##print "AcceptCursor"
		##print cursorPosition ; 
		glyph = self.GetHitGlyph(cursorPosition);
		if self is not glyph:
			##print "Found"
			return glyph.Bounds();
		#print "Not found"	
		return self.pos[0] , self.pos[1],0,0




	




		
class EditableColGlyph(ColGlyph):
	def __init__(self, window):
		ColGlyph.__init__(self, window);		
		self.Insert(EditableRowGlyph(window), 0);
		self.rowWithCursor = 0;
		
	def SetSize(self, size):
		ColGlyph.SetSize(self, size)
		for row in self.children:
			row.SetSize((self.size[0],30));
		
	def ProcessInput(self,e):
		#print " EditableColGlyph : got event" , self
		if e.type is event.KEY_PRESS:
			if e.keyCode == event.K_RETURN:
				#print "Got event.K_RETURN"
				row = EditableRowGlyph(self.window)
				row.SetSize((self.size[0],30));
				self.Insert(row, len(self.children));
				self.rowWithCursor = len(self.children) -1;
				
				return True;
			elif e.keyCode == event.K_LEFT :
				if  not self.children[self.rowWithCursor].ProcessInput(e):
					self.rowWithCursor = max(self.rowWithCursor-1 , 0);
			elif e.keyCode == event.K_RIGHT:
				if  not self.children[self.rowWithCursor].ProcessInput(e):
					self.rowWithCursor = min(self.rowWithCursor+1 , len(self.children) -1 );
			else:	
				self.children[self.rowWithCursor].ProcessInput(e);
				
			
		return True;	
		




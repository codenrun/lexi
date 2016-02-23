
from glyphs import *

class Composition(Glyph):
	def __init__(self, window):
		Glyph.__init__(self, window);
		self.children = [];
		self.cursorIndex = 0;
		
	def Render(self):
		self.window.ClearRect(self.Bounds());
		for child in self.children:
			child.Render();
		
		
	def Insert( self, g , at ):
		self.children.insert( at, g);		
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
		x,y,w,h = self.pos[0],self.pos[1],0,0;
		return x,y, max(self.size[0] , w) ,max(self.size[1] , h);
		
	def SetPosition(self, pos):
		Glyph.SetPosition(self, pos);	
		self.AdjustChildPositions();
		
	def AdjustChildPositions(self):
		pass;
			
	
	def ProcessInput(self,e):
		
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
			hitGlyph = self.GetHitGlyph(e.mousePosition);
			if self is not hitGlyph:		
				self.cursorIndex =  self.children.index(hitGlyph);
		
		return False;	
		
		
	def  GetChildren(self):
		return self.children;
		
	def GetHitGlyph(self, pos):	
		for child in self.children:
			if child.Intersects(pos):
				return child.GetHitGlyph(pos);
		return self;
		
	def GetHitChild(self, pos):	
		for child in self.children:
			if child.Intersects(pos):
				return child;
		return self;
	

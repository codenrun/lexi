
from glyphs import *

class Composition(Glyph):
	def __init__(self, window):
		Glyph.__init__(self, window);
		self.children = [];
		self.cursorIndex = 0;
		self.cursor =  CharGlyph(window);
		self.cursor.SetChar('|');
		self.cursor.SetColor((255,0,0));
		
		
	def Render(self):
		self.window.ClearRect(self.Bounds());
		
		boldOn = False;
		for child in self.children:
			if child.IsMarker() and child.Marker() == "bold":
				boldOn = True if boldOn is False else False;

			child.SetBold(boldOn);			
			child.Render();
			
			
		self.RenderCursor();

		
		
	def RenderCursor(self):
		if self.cursorIndex > 0:
			cursorBounds = self.children[self.cursorIndex-1].Bounds();
			self.cursor.SetPosition((cursorBounds[0] + cursorBounds[2] - 2, cursorBounds[1]));
		else:
			cursorBounds = self.Bounds();
			self.cursor.SetPosition((cursorBounds[0], cursorBounds[1]));
			
		self.cursor.Render();	
		
		
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
			print "before ",  self.cursorIndex, len(self.children)
			
			if e.keyCode == event.K_UNKN:
				return False;
			
			if e.keyCode == event.K_BACKSPACE:
				if self.Remove(self.cursorIndex-1):
					self.cursorIndex = self.cursorIndex -1;
			elif e.keyCode == event.K_LEFT  or e.keyCode == event.K_UP:
				if self.cursorIndex > 0 :
					self.cursorIndex = self.cursorIndex -1;
					return True;
			elif e.keyCode == event.K_RIGHT or e.keyCode == event.K_DOWN :
				if self.cursorIndex < len(self.children):		
					self.cursorIndex = self.cursorIndex +1;		
					return True;
			elif e.keyCode == event.K_RETURN:
				ch = FormatMarker(self.window, "next-line");
				if self.Insert(ch, self.cursorIndex):
					self.cursorIndex = self.cursorIndex +1;	
			elif e.keyCode == event.K_BOLD:
				print "Inserting bold-on marker"
				ch = FormatMarker(self.window, "bold");
				if self.Insert(ch, self.cursorIndex):
					self.cursorIndex = self.cursorIndex +1;
			else:	
				ch = CharGlyph(self.window);
				ch.SetChar(e.keyCode);
				if self.Insert(ch, self.cursorIndex):
					self.cursorIndex = self.cursorIndex +1;
			
			
			print "after" , self.cursorIndex, len(self.children)
			
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
	

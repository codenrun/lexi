

class Compositor():
	def __init__(self):
		pass;
		
	def Compose(self, composition ):
		pass;
		
		
		
class OneColumnCompositor(Compositor):
	def __init__(self, pageWidth, pageHeight ):
		self.pageWidth = pageWidth;
		self.pageHeight = pageHeight;
		self.pages = [];
		
		
		
	def Compose(self, composition):
		class Page():
			def __init__(self,w,h):
				self.w = w;
				self.h = h;
				self.columns = [];
				
		
		
		self.pages = [];
		page = Page( self.pageWidth, self.pageHeight);
		
	
		itr = composition.CreateIterator();		
		while !itr.IsDone():
			glyph = itr.CurrentItem();

			gX,gY,gW,gH = glyph.Bounds();
			if page.currentRow.placeX + 	
				
			if pag



			itr.Next();



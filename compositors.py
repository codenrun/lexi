

class Compositor():
	def __init__(self):
		pass;
		
	def Compose(self, composition ):
		pass;
		
		
		
class OneColumnCompositor(Compositor):
	def __init__(self, pageSize ):
		self.pageWidth = pageSize[0]-10*2;
		self.pageHeight = pageSize[1];
		
		
	def Compose(self, composition, origins):
		
		rowX = origins[0];
		rowY = origins[1];
		
		rowW = self.pageWidth;
		rowHeight = 20;
		
		for child in composition.children:
			gX,gY,gW,gH = child.Bounds();
			
			if rowX + gW > rowW :
				rowX = 0;
				gX = 0;
				rowY = rowY + rowHeight;
			else:
				gX = rowX;
				rowX = rowX + gW;
				
			child.SetPosition( (gX , rowY ));
		
		return composition;

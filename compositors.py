

class Compositor():
	def __init__(self):
		pass;
		
	def Compose(self, composition ):
		pass;
		
		
		
class OneColumnCompositor(Compositor):
	def __init__(self, pageSize , origins ):
		self.pageWidth = pageSize[0];
		self.pageHeight = pageSize[1];
		self.origins = origins
		
	def Compose(self, composition ):
		
		rowX = self.origins[0];
		rowY = self.origins[1];
		
		rowW = self.pageWidth;
		rowHeight = 30;
		
		for child in composition.children:
			if child.IsRenderable():

				gX,gY,gW,gH = child.Bounds();
				
				if rowX + gW > rowW :
					rowX = self.origins[0];	
					rowY = rowY + rowHeight;
				
				gX = rowX;
				rowX = rowX + gW;	
				child.SetPosition( (gX , rowY ));
			else:				
				marker = child.Marker();
				if marker == "next-line":
					rowX = self.origins[0];	
					rowY = rowY + rowHeight;
				child.SetPosition( (rowX , rowY ));
									
		return composition;

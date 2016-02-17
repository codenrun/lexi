
import gfx;

import event;

gc = gfx.MakeGFX('pygame');
gc.Init();

eventing = gfx.MakeEventing('pygame' );
window = gfx.Window(gc , (700,500) );		
window.SetPosition((100,100));

cursor= gfx.CharGlyph(window);
cursor.SetChar('|');
cursor.SetColor((0,0,255));

row = gfx.EditableRowGlyph(window);
window.body.Insert(row,0);
window.Render();


bRunning = True;
while(bRunning):	
	gc.Blit();
	cursor.Render();

	for e in eventing.GetEvents():
		
		window.HandleInput(e);
		
			
		if e.type == event.QUIT:
			gc.Quit();
			bRunning = False;
	

	
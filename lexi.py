
import gfx;

import event;

gc = gfx.MakeGFX('pygame');
gc.Init();

eventing = gfx.MakeEventing('pygame' );
window = gfx.Window(gc , (700,500) );		
window.SetPosition((100,100));

window.Render();


bRunning = True;
while(bRunning):	
	gc.Blit();

	for e in eventing.GetEvents():
		
		window.HandleInput(e);
		
			
		if e.type == event.QUIT:
			gc.Quit();
			bRunning = False;
	

	

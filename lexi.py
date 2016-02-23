
import gfxFactory;
import event;
from window import *


eventing = gfxFactory.MakeEventing('pygame' );
gc = gfxFactory.MakeGFX('pygame');
gc.Init();

window = Window(gc , (700,500), (100,100) );		
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
	

	

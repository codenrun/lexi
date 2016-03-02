
import gfxFactory;
import event;
from window import *

from compositors import *

eventing = gfxFactory.MakeEventing('pygame' );
gc = gfxFactory.MakeGFX('pygame');
gc.Init();



window = Window(gc , (800,500), (100,0) );	
window.SetTitle("LEXi");	
window.SetPosition((100,0));

compositor2 =  TwoColumnCompositor( ( 800-10 , 500),(10,10) );
compositor1 =  OneColumnCompositor( ( 800-10 , 500),(10,10) );

window.SetCompositor(compositor1);
window.Render();

bRunning = True;
while(bRunning):	
	gc.Blit();
	for e in eventing.GetEvents():
		if e.type is event.KEY_PRESS and e.keyCode == event.K_F2:
			print "col-2-composer"
			window.SetCompositor(compositor2);
		elif e.type is event.KEY_PRESS and e.keyCode == event.K_F1:
			print "col-1-composer"
			window.SetCompositor(compositor1);
		else :
			window.HandleInput(e);		

		if e.type == event.QUIT:
			gc.Quit();
			bRunning = False;
	

	

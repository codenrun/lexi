			

import PygameGfx

def MakeGFX( type ):
	if type is 'pygame':
		return PygameGfx.PyGameGFX();


def MakeEventing( type ):
	if type is 'pygame':
		return PygameGfx.PyGameEventing();


		

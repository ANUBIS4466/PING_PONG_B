#4 

	#Игровая сцена:
	back = (0, 255, 0) 
	win_width = 600
	win_height = 500
	window = display.set_mode((win_width, win_height))
	window.fill(back)

	#флаги	
	game = True
	finish = False
	clock =	time.Clock()
	FPS = 60

	# мяч и ракетка
	racketl = Player('racket.png', 30, 200, 4, 50, 150) 
	ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

	font.init()
  font = font.Font('calibri.ttf', 35)
	losel	=	font.render('PLAYER	1	LOSE!',	True,	(180,	0,	0))
	lose2	=	font.render('PLAYER	2	LOSE!',	True,	(180,	0,	0))


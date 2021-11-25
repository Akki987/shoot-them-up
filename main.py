def on_down_pressed():
    global Haut, Bas, Gauche, Droite
    Haut = False
    Bas = True
    Gauche = False
    Droite = False
    Vaisseau.set_image(assets.image("""
        Vaisseau_bas
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_a_pressed():
    if Haut == True:
        pass
    if Bas == True:
        pass
    if Gauche == True:
        pass
    if Droite == True:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_up_pressed():
    global Haut, Bas, Gauche, Droite
    Haut = True
    Bas = False
    Gauche = False
    Droite = False
    Vaisseau.set_image(assets.image("""
        Vaisseau
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_right_pressed():
    global Haut, Bas, Gauche, Droite
    Haut = False
    Bas = False
    Gauche = False
    Droite = True
    Vaisseau.set_image(assets.image("""
        Vaisseau_droite
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    global Haut, Bas, Gauche, Droite
    Haut = False
    Bas = False
    Gauche = True
    Droite = False
    Vaisseau.set_image(assets.image("""
        Vaisseau_gauche
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

Droite = False
Gauche = False
Bas = False
Haut = False
Vaisseau: Sprite = None
Vaisseau = sprites.create(img("""
        . . . . . . c . . . . . . 
            . . . . . a a c . . . . . 
            . . . . c a a a a . . . . 
            . . a a a a 9 a a a c . . 
            . a a a a a 6 a a a a a . 
            c c a a a a a a a a a c c 
            . . . c c c a a c c . . . 
            . . . 2 4 5 5 5 4 2 . . . 
            . . . 2 4 4 5 4 4 2 . . . 
            . . . . 2 4 4 4 2 . . . . 
            . . . . 2 2 4 2 2 . . . . 
            . . . . . 2 2 2 . . . . . 
            . . . . . . 2 . . . . . .
    """),
    SpriteKind.player)
Vaisseau.set_stay_in_screen(True)
controller.move_sprite(Vaisseau)
@namespace
class SpriteKind:
    COIN = SpriteKind.create()
    FLOWER = SpriteKind.create()

def on_a_pressed():
    if HOPS_AND_PAWS.vy == 0:
        HOPS_AND_PAWS.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        POTTAL
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.over(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile2)

def on_on_overlap(sprite3, otherSprite):
    global BEE
    otherSprite.destroy()
    BEE = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(BEE,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                        . . 5 f 5 5 5 5 5 5 5 5 . . . . 
                        . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                        . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                        . . 5 f 5 5 5 5 5 5 5 5 . . . . 
                        . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                        . . 5 5 5 5 5 5 5 5 5 5 . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    BEE.set_position(0 + 0, 0)
sprites.on_overlap(SpriteKind.player, SpriteKind.FLOWER, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite2):
    info.change_score_by(1)
    otherSprite2.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.COIN, on_on_overlap2)

BEE: Sprite = None
FLOWER2: Sprite = None
COIN2: Sprite = None
HOPS_AND_PAWS: Sprite = None
scene.set_background_color(9)
HOPS_AND_PAWS = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . f . . . . . 
            . . . . . . . . . . f f f f . . 
            . . . . . . . . . . f f f 5 f f 
            . . . . . . . . . . f f f f f f 
            f f f f f f f f f f f f f f f f 
            . . f f f f f f f f f f f . . . 
            . . f f f f f f f f f f . . . . 
            . . f f f f f f f f f f . . . . 
            . . . f . . f . . f . f . . . . 
            . . . f . . f . . f . f . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(HOPS_AND_PAWS, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
HOPS_AND_PAWS.ay = 350
scene.camera_follow_sprite(HOPS_AND_PAWS)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile2
""")):
    COIN2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . f f 5 5 5 5 5 5 5 f f . . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    . . f f 5 5 5 5 5 5 5 f f . . . 
                    . . . . f f f f f f f . . . . .
        """),
        SpriteKind.COIN)
    animation.run_image_animation(COIN2,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . . . . f f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . f f 5 5 5 5 5 f f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f f 5 5 5 5 5 f f . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f f 5 5 5 f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f 5 5 5 f f . . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f . . . . . 
                        . . . . . f f 5 5 f f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f f 5 5 f f . . . . . 
                        . . . . . . f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . . . f 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 5 f . . . . . . 
                        . . . . . . f f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . . 5 f 5 . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . f 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 f 5 . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . f 5 f 5 . . . . . . 
                        . . . . . . . f f f . . . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . . . f 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 5 f . . . . . . 
                        . . . . . . f f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f f 5 5 5 f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f 5 5 5 f f . . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f . . . . . 
                        . . . . . f f 5 5 f f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f f 5 5 f f . . . . . 
                        . . . . . . f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . . . . f f f f f f f . . . . .
            """)],
        100,
        True)
    tiles.place_on_tile(COIN2, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile1
""")):
    FLOWER2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . 7 7 7 . . 9 9 9 9 . . . . . . 
                    . 7 7 . . . 9 9 9 9 9 . . . . . 
                    7 7 7 . . 9 9 5 5 9 9 . . . . . 
                    7 . 7 . . 9 9 5 5 9 9 . . . . . 
                    7 7 . . . . 9 7 9 9 9 . . . . . 
                    7 7 . . . . . 7 . . . . 7 7 7 . 
                    7 7 . . . . . 7 . . . . 7 7 7 . 
                    7 7 . . . . . 7 . . . 7 7 7 7 . 
                    7 7 7 7 7 . . 7 . . 7 7 7 7 7 . 
                    . . 7 7 7 . 7 7 7 7 7 7 7 7 7 . 
                    . . . 7 7 7 7 7 7 7 7 7 7 7 . . 
                    . . . . . . . 7 . . . . . . . .
        """),
        SpriteKind.FLOWER)
    tiles.place_on_tile(FLOWER2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))
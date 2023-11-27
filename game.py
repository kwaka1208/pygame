import pygame as pg
import sys

pg.init()   # pygame初期化
screen = pg.display.set_mode((800, 600))  # 画面設定

while True:
    screen.fill(pg.Color("WHITE"))  # 画面を白で塗りつぶす
    pg.draw.rect(screen, pg.Color("RED"), pg.Rect(10, 20, 100, 150))  # 赤い四角形を描画
    pg.display.update()    # 画面を更新
    for event in pg.event.get():
        if event.type == pg.QUIT:   # 閉じるボタンが押されたら終了
            pg.quit()
            sys.exit()
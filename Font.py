def RenderText(font, screen, content, index):
   text = font.render(content, False, (255, 0, 0))
   screen.blit(text, (0,index * 20))
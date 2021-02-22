import pygame
from pygame import *
import random
import sys
from pygame_vkeyboard import *


try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()

except ImportError:
    print "OOPS Pygame SDL2 not available"

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
background_color = (216,216,216)
touch_i_color = (88,88,88)
touch_a_color = (50,164,206)
kpad_c = (236,239,241) 

pygame.init()


def fps_message(msg,color,SW):
	terminal_font = font.Font('fonts/arial.ttf',25)
	screen_text = terminal_font.render(msg, True, color)#sys_font.render(msg, True, color)
	screen.blit(screen_text, ((SW/2)*2-125,0))

screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.RESIZABLE)
caption = pygame.display.set_caption('AlmnaCalcu')

SH = screen.get_height()
SW = screen.get_width()

clock = pygame.time.Clock()
FPS = 180


def consumer(text):
	global lable_txt
	lable_txt = text
	#print('Current text : %s' % text)

# TOP_LEFT_CORNER = (0,0)
# TOP_RIGHT_CORNER = ((SW/2)*2-W,0)
# BOTTOM_LEFT_CORNER = (0,(SH/2)*2-H)
# BOTTOM_RIGHT_CORNER = ((SW/2)*2-W,(SH/2)*2-H)
# CENTER = ((SW/2)-W,(SH/2)-H)

##GLOBAL##
lable_txt = ''
keypad_s = 'off'
layout = VKeyboardLayout(VKeyboardLayout.AZERTY)
keyboard = VKeyboard(screen, consumer, layout)

               

class Button(object):
	dreturner = False
	quit_counter = 0
	
	def __init__(self):
		self.cy_pre = 0
		self.yscroller = 0
		self.scroll_s = False
		self.scroll_live = False

	def text(self,msg,color,x,y,b,txts):
		terminal_font = font.Font('fonts/arial.ttf',txts)
		screen_text = terminal_font.render(msg, True, color)#sys_font.render(msg, True, color)
		screen.blit(screen_text, (x-b,y))
	def dmouse_click(self,button_x,button_y,dd,ll):
		cursor = pygame.mouse.get_pos()
		clickk = pygame.mouse.get_pressed()
		if(button_x + dd > cursor[0] > button_x and button_y + ll > cursor[1] > button_y):
		    if(clickk[0] == 1):
		        self.quit_counter = 5
		        return True
		    else:
		        return False
	def mouse_click(self,button_x,button_y,dd,ll):
		cursor = pygame.mouse.get_pos()
		clickk = pygame.mouse.get_pressed()
		if(button_x + dd > cursor[0] > button_x and button_y + ll > cursor[1] > button_y):
			if(clickk[0] == 1):
			    return True
			else:
			    return False

	def button(self,x,y,w,h,t,txt,b,size,txts,BW,BH,scroll):
		xx = x
		yy = y
		ww = w
		hh = h
		if(size == 'large'):
			pass
		elif(size == 'medium'):
			ww -= 50
			w = ww
			hh -= 25
			h = hh
		elif(size == 'small'):
			ww -= 100
			w = ww
			hh -= 50
			h = hh
		# CENTER = ((SW/2)-W,(SH/2)-H)
		txt_x =	x + (w/2) - (txts)
		txt_y = y + (h/2) - (txts)/2

		cx,cy = pygame.mouse.get_pos()

		self.scroll_live = False

		if(scroll == True and keypad_s == 'off'):
			if self.mouse_click(0,0,SW,SH):
				self.scroll_live = True
				if(cy - self.cy_pre > 0) or (cy - self.cy_pre < 0):
					self.scroll_s = True
					if cy - self.cy_pre > 0:
						self.yscroller = self.yscroller + (BH/8)# + 4
					elif cy - self.cy_pre < 0:
						self.yscroller = (self.yscroller) - (BH/8)# - 4
					self.cy_pre = cy

		if(self.scroll_s == True):
			y = y + self.yscroller
			#print(y)

		self.cy_pre = cy

		if self.mouse_click(x,y,w,h):
			if(size == 'small'):
				draw.rect(screen,touch_a_color,(x,y,w,h),t)
				draw.rect(screen,touch_a_color,(x-2,y-2,w+4,h+4),3)
				self.text(txt,white,txt_x,(y+(h/2))-20,b,txts)
				return True
			if(size == 'medium'):
				draw.rect(screen,touch_a_color,(x-2,y-2,w+4,h+4),3)
				draw.rect(screen,touch_a_color,(x,y,w,h),t)
				self.text(txt,white,txt_x,(y+(h/2))-20,b,txts)
				return True
			if(size == 'large'):
				draw.rect(screen,touch_a_color,(x-2,y-2,w+4,h+4),3)
				draw.rect(screen,touch_a_color,(x,y,w,h),t)
				self.text(txt,white,txt_x,(y+(h/2))-20,b,txts)
				return True
		else:
			if(size == 'small'):
				draw.rect(screen,touch_i_color,(x-2,y-2,w+4,h+4),3)
				draw.rect(screen,touch_i_color,(x,y,w,h),t)
				self.text(txt,white,txt_x,(y+(h/2))-20,b,txts)
			if(size == 'medium'):
				draw.rect(screen,touch_i_color,(x-2,y-2,w+4,h+4),3)
				draw.rect(screen,touch_i_color,(x,y,w,h),t)
				self.text(txt,white,txt_x,(y+(h/2))-20,b,txts)
			if(size == 'large'):
				draw.rect(screen,touch_i_color,(x-2,y-2,w+4,h+4),3)
				draw.rect(screen,touch_i_color,(x,y,w,h),t)
				self.text(txt,white,txt_x,(y+(h/2))-20,b,txts)
		

	def d_button(self,x,y,w,h,t,size):
		xx = x
		yy = y
		ww = w
		hh = h
		if(size == 'large'):
			pass
		elif(size == 'medium'):
			ww -= 50
			w = ww
			hh -= 25
			h = hh
		elif(size == 'small'):
			ww -= 100
			w = ww
			hh -= 50
			h = hh
		if self.dmouse_click(x,y,w,h):
			self.dreturner = True
			draw.rect(screen,black,(x,y,w,h),t)
		else:
			draw.rect(screen,red,(x,y,w,h),t)

		if(self.quit_counter > 0):
		    self.quit_counter = self.quit_counter - 1
		    if((self.quit_counter == 1) and (self.dreturner == True)):
		        return True	

class Lable(object):
	def __init__(self):
		self.text_ = []
		self.WD = 0
		self.HG = 0
		self.lable_s = False
		self.done = Button()
		self.font_size = 0
		self.cy_pre = 0
		self.yscroller = 0
		self.scroll_s = False
		self.scroll_live = False

	def mouse_click(self,button_x,button_y,dd,ll):
		cursor = pygame.mouse.get_pos()
		clickk = pygame.mouse.get_pressed()
		if(button_x + dd > cursor[0] > button_x and button_y + ll > cursor[1] > button_y):
			if(clickk[0] == 1):
			    return True
			else:
			    return False
	def lable_message(self,msg,color,x,y,BW,BH,size):
		terminal_font = font.Font('fonts/DejaVuSans.ttf',size)
		screen_text = terminal_font.render(msg, True, color)#sys_font.render(msg, True, color)
		if(self.lable_s == True):
			draw.rect(screen,touch_a_color,(x-2,y-2,BW+self.WD+4,BH+self.HG+4),3)
			draw.rect(screen,white,(x,y,BW+self.WD,BH+self.HG),0)

		if(self.lable_s == False):
			draw.rect(screen,touch_i_color,(x-2,y-2,BW+self.WD+4,BH+self.HG+4),3)
			draw.rect(screen,white,(x,y,BW+self.WD,BH+self.HG),0)
		
		screen.blit(screen_text, (x,y))

	def run(self,msg,color,x,y,BW,BH,size,scroll):
		global keypad_s,lable_txt
		self.font_size = (((BW/2)/2)/2)
		cx,cy = pygame.mouse.get_pos()

		self.scroll_live = False

		if(scroll == True and keypad_s == 'off'):
			if self.mouse_click(0,0,SW,SH):
				self.scroll_live = True
				if(cy - self.cy_pre > 0) or (cy - self.cy_pre < 0):
					self.scroll_s = True
					if cy - self.cy_pre > 0:
						self.yscroller = self.yscroller + (BH/8) #+ 4
					elif cy - self.cy_pre < 0:
						self.yscroller = (self.yscroller) - (BH/8)# - 4
					self.cy_pre = cy

		if(self.scroll_s == True):
			y = y + self.yscroller
			#print(y)

		self.cy_pre = cy
		#draw.rect(screen,red,(0,0,SW,SH),0)

		if(size == 'simple'):
			self.font_size = self.font_size - 17
			self.WD = 300
			self.HG = -50
		elif(size == 'large'):
			self.font_size = self.font_size + 3 
			self.WD = 500
			self.HG = 50
		elif(size == 'medium'):
			self.font_size = self.font_size - 12 
			self.WD = 400
			self.HG = 25
		elif(size == 'small'):
			self.font_size = self.font_size - 17
			self.WD = 300
			self.HG = 0

		self.lable_message(lable_txt,color,x,y,BW,BH,self.font_size)
		#if(self.scroll_live == False):
		if self.mouse_click(x,y,BW+self.WD,BH+self.HG):
			self.lable_s = True
			if(pygame_sdl2.key.has_screen_keyboard_support() != 0):
				pygame_sdl2.key.start_text_input()
				a = open("execution.txt", 'a')
				a.write("\nKeypad is Enabled: True")
				a.close()
			else:
				keypad_s = 'on'

		if(self.lable_s == True):
			if self.done.button(x+BW+self.WD+10,y,((BW/2)/2)/2+(self.WD)/2+4,BH+self.HG,0,'Done',5,'large',((BW-BH)/2)/2,BW,BH,True):
				self.lable_s = False
				if(pygame_sdl2.key.has_screen_keyboard_support() != 0):
					pygame_sdl2.key.stop_text_input()
					a = open("execution.txt", 'a')
					a.write("\nKeypad is Disabled: True")
					a.close()
				else:
					keypad_s = 'off'


##BUTTONS_DEFINITION##
button1 = Button()
##@LABLE_DEFINITION@##
lable1 = Lable()
lable2 = Lable()

def check_reso():
	global conx,cony
	r = 0 
	while r <= 20:
		screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.RESIZABLE)
		h = screen.get_height()
		w = screen.get_width()
		if(r == 19):
			main(w,h)
		r = r + 1


def main(w,h):	
	global typing,lable_txt,keypad_s,SH,SW
	screen = pygame.display.set_mode((w,h),pygame.RESIZABLE)
	current_w_height = screen.get_height()
	current_w_width = screen.get_width()
	SW = current_w_width
	SH = current_w_height
	if(SH > SW):
		BSB = SH
		SSS = SW
	else:
		BSB = SW
		SSS = SH
	BW = (BSB - SSS)/2 
	BH = BW/2
	a = open("execution.txt", 'w')
	a.write("App Started...")
	a.close()
	while True:
		typing = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == VIDEORESIZE:
				screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
				SH = screen.get_height()
				SW = screen.get_width()
				#SSS the smallest between SH,SW
				#BSB the biggest between SH,SW
				if(SH > SW):
					BSB = SH
					SSS = SW
				else:
					BSB = SW
					SSS = SH
				BW = (BSB - SSS)/2 
				BH = BW/2
				print(SW,SH,"BW:%s  BH:%s"%(BW,BH))
			keyboard.on_event(event)
			

		screen.fill(black)#(background_color)
		# CENTER = ((SW/2)-W,(SH/2)-H)
		button1.button((SW/2)-((BW-0)/2),((SH/2)-((BH-0)/2)),BW,BH,0,'Hello',0,'large',((BW-BH)/2)/2,BW,BH,True)
		#done.button(x+BW+self.WD+10,y,((BW/2)/2)/2+(self.WD)/2+4,BH+self.HG,0,'Done',5,'large',((BW-BH)/2)/2,BW,BH,True)
		#button1.button((SW/2)-((BW-50)/2),((SH/2)-((BH-25)/2)),BW,BH,0,'Hello',0,'medium',((BW-BH)/2)/2,BW,BH,True)
		#button1.button((SW/2)-((BW-100)/2),((SH/2)-((BH-50)/2)),BW,BH,0,'Hello',0,'small',((BW-BH)/2)/2,BW,BH,True)
		###############FPS#################
		fpss = int(clock.get_fps())
		fps_message("FPS = %s"%fpss,white,SW)
		###################################
		#TOP_LEFT_CORNER = (0,0)
		lable1.run(lable_txt,black,10,10,BW,BH,'simple',True)
		#lable1.run(lable_txt,black,10,((SH/2)*2-BH+40),BW,BH,'simple')
		#lable1.run(lable_txt,black,10,10,BW,BH,'simple')
		#lable2.run(black,(SW/2)-(BW/2),(SH/2)-(BH/2),BW,BH,'small')
		if(keypad_s == 'on'):
			keyboard.enable()
		else:
			keyboard.disable()
		
		display.update()
		clock.tick(FPS)


check_reso()
#main(480,800)




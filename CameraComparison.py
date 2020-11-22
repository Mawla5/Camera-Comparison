from os import system

def menu():
	system("cls")
	print("""
	Welcome To The Camera Comparison Program.
	Select A Camera
	[1] A7RIII
	[2] Panasonic S1R
	[3] Canon R5
	[4] Nikon Z7II
	[5] Fujifilm GFX 50
	[7] Quit
		""")

def print_header(msg):
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False
 

def A7RIII():
	print("The Specs Sheet Says... ")
	print("Name: Sony A7RIII")
	print("Price = $3699.00")
	print("Sensor Type = Full Frame")
	print("Megapixel = 61mp")
	print("IBIS = Yes")
	print("Burst_Speed = 10fps")
	input()

def Panasonic_S1R():
	print("The Specs Sheet Says... ")
	print("Name: Panasonic S1R")
	print("Price = $3500.00")
	print("Sensor Type = Full Frame")
	print("Megapixel = 47.3mp")
	print("IBIS = Yes")
	print("Burst_Speed = 9.6fps")
	input()

def Canon_R5():
	print("The Specs Sheet Says... ")
	print("Name: Canon R5")
	print("Price = $3,899.00")
	print("Sensor Type = Full Frame")
	print("Megapixel = 45mp")
	print("IBIS = Yes")
	print("Burst_Speed = 12fps")
	input()

def Nikon_Z7II():
	print("The Specs Sheet Says... ")
	print("Name: Nikon Z7II")
	print("Price = $2999.00")
	print("Sensor Type = Full Frame")
	print("Megapixel = 45.7mp")
	print("IBIS = Yes")
	print("Burst_Speed = 10fps")
	input()

def Fujifilm_GFX_50():
	print("The Specs Sheet Says... ")
	print("Name: Fujifilm GFX 50")
	print("Price = $4499.00")
	print("Sensor Type = Medium Format")
	print("Megapixel = 51mp")
	print("IBIS = No")
	print("Burst_Speed = 3fps")
	input()

def add_camera(): 
	Name = input("Name:    ")
	Price = input("Price:    ")
	Sensor_Type = input("Sensor Type:   ")
	Megapixel = input("Megapixel:   mp")
	IBIS = input("IBIS:   ")
	Burst_Speed = input("Burst Speed:   ")


	
def check_user_input(chud):
	chud = chud.upper()
	if chud == "6":
		print("Goodbye!")
		return True
	elif chud == "1":
		A7RIII()
	elif chud == "2":
		Panasonic_S1R()
	elif chud == "3":
		Canon_R5()
	elif chud == "4":
		Nikon_Z7II()
	elif chud == "5":
		Fujifilm_GFX_50()


stop = False
while not stop:
	menu()
	user_input = input("Pick Your Camera!   ")
	stop = check_user_input(user_input)
	






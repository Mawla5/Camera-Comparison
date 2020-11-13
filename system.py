from josn import load, dump

def load_ticket_data():
	with open(ticket_table_path, "r") as ticketfile:
		data = load(ticketfile)
	return data
def load_user_data():
	with open(user_table_path, "r") as userfile:
		data = load(userfile)
	return data
error = False
ticket_table_path = "data/tiket_table.json"
user_table_path = "data/user_table.json"

tickets = {}
users = {}

#####LIBRARY STRING

main_menu = """
APLIKASI TIKET PESAWAT AGENSI SANGET HEBAT

[1] Pesan/Booking Tiket Pesawat
[2] Carti Tiket Pesawat
[3] Edit Ticket Pesawat
[4] Batalkan/Hapus Tiket Pesawat
[5] Cetak PDF Tiket Pesawat
[6] Cetak QR Tiket Pesawat
[7] Tentang Aplikasi
"""	

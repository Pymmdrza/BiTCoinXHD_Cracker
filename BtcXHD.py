import threading

from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hexer import mHash
from rich.console import Console
from colorama import Fore, Style, Back
from hexer import mHash

mmdrza = '''
         - - - - - - - - - - - - - - - - - - - - - ---***--- - - - - - - - - - - - - - - - - - - - -
        ███╗███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗███╗
        ██╔╝████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║╚██║
        ██║ ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║ ██║
        ██║ ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║ ██║
        ███╗██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███║
        ╚══╝╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══╝
        '''

filename = input('[*]Enter File Name With Type Format: ')
console = Console()
console.clear()

with open(filename) as f:
	add = f.read().split()
add = set(add)
print('\n\n\n\n\n\n\n\n\n\n\n\n', Fore.RED, str(mmdrza), Style.RESET_ALL, '\n')

def mmdrza_t():
	w = 0
	z = 0
	print(Fore.YELLOW + '[*] Programmer Mmdrza.Com    ' + Fore.YELLOW + '\n[*] Telegram Channel: @mPython3   ' + Fore.YELLOW + '\n[*] Telegram iD @PyMmdrza\n' + Fore.YELLOW + '[*] All Address Type Generated Type:' + Fore.GREEN + '\n[*] P2PKH - P2SH - P2wSH - P2wPKH - Bech32\n')
	while True:
		ihex = mHash()
		PrivHex = str(ihex)
		hd: HDWallet = HDWallet(symbol=SYMBOL)
		hd.from_private_key(private_key=PrivHex)
		priv = hd.private_key()
		addr1 = hd.p2pkh_address()
		addr2 = hd.p2wpkh_address()
		addr3 = hd.p2wsh_address()
		addr4 = hd.p2sh_address()
		addr5 = hd.p2wsh_in_p2sh_address()
		addr6 = hd.p2wpkh_in_p2sh_address()
		if addr1 in add:
			print('New Find Detail BTC Wallet ... Saved On Text File .', str(addr1), str(priv))
			f = open("BTC_Winner_DETAIL.txt", "a")
			f.write('\nAddr:       ' + str(addr1))
			f.write('\nPrivateKey: ' + str(priv))
			f.write('\n================[ MMDRZA.COM ]==================\n')
			f.close()
			w += 1
			z += 1
		
		elif addr2 in add:
			print('New Find Detail BTC Wallet ... Saved On Text File .', str(addr2), str(priv))
			f = open("BTC_Winner_DETAIL.txt", "a")
			f.write('\nAddr:       ' + str(addr2))
			f.write('\nPrivateKey: ' + str(priv))
			f.write('\n================[ MMDRZA.COM ]==================\n')
			f.close()
			w += 1
			z += 1
		
		elif addr3 in add:
			print('New Find Detail BTC Wallet ... Saved On Text File .', str(addr3), str(priv))
			f = open("BTC_Winner_DETAIL.txt", "a")
			f.write('\nAddr:       ' + str(addr3))
			f.write('\nPrivateKey: ' + str(priv))
			f.write('\n================[ MMDRZA.COM ]==================\n')
			f.close()
			w += 1
			z += 1
		
		elif addr4 in add:
			print('New Find Detail BTC Wallet ... Saved On Text File .', str(addr4), str(priv))
			f = open("BTC_Winner_DETAIL.txt", "a")
			f.write('\nAddr:       ' + str(addr4))
			f.write('\nPrivateKey: ' + str(priv))
			f.write('\n================[ MMDRZA.COM ]==================\n')
			f.close()
			w += 1
			z += 1
		
		elif addr5 in add:
			print('New Find Detail BTC Wallet ... Saved On Text File .', str(addr5), str(priv))
			f = open("BTC_Winner_DETAIL.txt", "a")
			f.write('\nAddr:       ' + str(addr5))
			f.write('\nPrivateKey: ' + str(priv))
			f.write('\n================[ MMDRZA.COM ]==================\n')
			f.close()
			w += 1
			z += 1
		
		elif addr6 in add:
			print('New Find Detail BTC Wallet ... Saved On Text File .', str(addr6), str(priv))
			f = open("BTC_Winner_DETAIL.txt", "a")
			f.write('\nAddr:       ' + str(addr6))
			f.write('\nPrivateKey: ' + str(priv))
			f.write('\n================[ MMDRZA.COM ]==================\n')
			f.close()
			w += 1
			z += 1
		
		else:
			print(Fore.RED, '[+] TOTAL:', Fore.WHITE, str(z), Fore.YELLOW, '- Win:', Fore.CYAN, str(w), Fore.WHITE, Back.RED, str(priv), Style.RESET_ALL, end='\r')
			z += 1
mmdrza_t()

t_Core = threading.Thread(target=mmdrza_t)
t_Core.start()
t_Core.join()

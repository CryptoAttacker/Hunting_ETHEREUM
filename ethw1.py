# from hexer import mHash
from hdwallet import HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import generate_mnemonic, is_mnemonic
from hdwallet import BIP44HDWallet
from lxml import html
import requests
from mnemonic import Mnemonic
import random
from colorama import Fore, Style

def xBal(addr):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol

z = 1
while True:
    langrnd = ['english', 'french']
    sellan = random.choice(langrnd)
    mne = Mnemonic(str(sellan))
    listno = ["128", "256"]
    rnd = random.choice(listno)
    words = mne.generate(strength=int(rnd))
    STRENGTH = int(rnd)
    LANGUAGE: str = (sellan)
    MNEMONIC = words
    PASSPHRASE: str = "meherett"
    assert is_mnemonic(mnemonic=words, language=sellan)
    
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=Cryptocurrency, account=0, change=False, address=0)
    bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)
    mixword = words[:128]
    addr = bip44_hdwallet.p2pkh_address()
    priv = bip44_hdwallet.private_key()
    bal = xBal(addr)
  
    print(str(z) + Fore.RED +' ' + Fore.WHITE + str(mixword)[:64] + '...' + Style.RESET_ALL)
    print(Fore.YELLOW + '[+] Address: ' + Fore.RED + str(addr) + Fore.YELLOW + ' [TXID: ' + str(bal)+']'+Fore.RED+'[ETH' + str(rnd) + str(sellan)[:2]+']'+Style.RESET_ALL)
    z += 1
    if int(bal) > 0:
        print(Fore.GREEN,'New Wallet Winner and Save All Details To Text File (MMDRZA.CoM)')
        print(Fore.YELLOW,'Please Wait ----> Writing Data <----',Style.RESET_ALL)
        f = open("ETH-WiNER____Wallet___Detail.txt", "a")
        f.write('\nAddress     =====> ' + str(addr))
        f.write('\nPrivateKey  =====> ' + str(priv))
        f.write('\nMnemonic    =====> ' + str(words))
        f.write('\nTransaction =====> ' + str(bal))
        f.write('\n            -------[ M M D R Z A . C o M ]------                   \n')
        f.close()
        
        continue
        
# if __name__ == '__main__':
#     start = int(11579208923731619542357098500868790785283756427907490438260516314151816149631)
#     cpucores = int(20)
#     group_size = int(1)
#     print('[+] Starting.........Wait.....')
#     hunt_ETH_address(cores=cpucores)

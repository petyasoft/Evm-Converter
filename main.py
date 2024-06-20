from bip_utils import Bip39SeedGenerator, Bip44Coins, Bip44, Bip44Changes


class BlockChainAccount():
    def __init__(self, mnemonic, coin_type=Bip44Coins.ETHEREUM, password = '') -> None:
        self.mnemonic = mnemonic.strip()
        self.coin_type = coin_type
        self.password = password 

    def get_address(self,count):
        seed_bytes = Bip39SeedGenerator(self.mnemonic).Generate(self.password)
        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, self.coin_type).Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(count)
        return {"mnemonic" : self.mnemonic,
                "address" : bip44_mst_ctx.PublicKey().ToAddress(),
                "private" : f"0x{bip44_mst_ctx.PrivateKey().Raw().ToHex()}"}

    
with open("address.txt",'w') as file:
    pass
with open("private.txt",'w') as file:
    pass
with open("alldata.txt",'w') as file:
    pass

with open("mnemonics.txt",'r') as file:
    mnemonics = [mnemo.strip() for mnemo in file.readlines()]
for mnemonic in mnemonics:
    COUNT_DERIVATION_PATH = 1
    for count in range(COUNT_DERIVATION_PATH):
        try:
            keys = BlockChainAccount(mnemonic=mnemonic)
            info = keys.get_address(count)
            with open("address.txt",'a') as file:
                file.write(info["address"]+'\n')
            with open("private.txt",'a') as file:
                file.write(info["private"]+'\n')
            with open("alldata.txt",'a') as file:
                file.write(info["mnemonic"]+' '+info["private"]+' '+info["address"]+'\n')
        except:
            continue

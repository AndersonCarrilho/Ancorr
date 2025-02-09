# bitcoin_wallet_generator.py

from Blockthon import Wallet, Bitcoin
from mnemonic import Mnemonic
import multiprocessing

# Função para gerar endereços Bitcoin e chaves privadas a partir de mnemônicos
def generate_wallet_info(mnemonics):
    seed_bytes = Wallet.Mnemonic_To_Bytes(mnemonics)
    privatekey = Wallet.Bytes_To_PrivateKey(seed_bytes)
    
    p2pkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2PKH')
    p2shAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2SH')
    p2wpkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKH')
    p2wshAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSH')
    p2wpkhSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKHinP2SH')
    p2wshSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSHinP2SH')
    
    return {
        "PrivateKey": privatekey,
        "P2PKH": p2pkhAddress,
        "P2SH": p2shAddress,
        "P2WPKH": p2wpkhAddress,
        "P2WSH": p2wshAddress,
        "P2WPKHinP2SH": p2wpkhSegwit,
        "P2WSHinP2SH": p2wshSegwit
    }

# Função para gerar informações de carteira para uma linguagem específica
def generate_wallet_info_for_language(language):
    mnemo = Mnemonic(language)
    mnemonics_12 = mnemo.generate(128)
    mnemonics_18 = mnemo.generate(192)
    mnemonics_24 = mnemo.generate(256)

    wallet_info_12 = generate_wallet_info(mnemonics_12)
    wallet_info_18 = generate_wallet_info(mnemonics_18)
    wallet_info_24 = generate_wallet_info(mnemonics_24)

    return {
        "Language": language,
        "Mnemonic_12": mnemonics_12,
        "PrivateKey_12": wallet_info_12["PrivateKey"],
        "P2PKH_12": wallet_info_12["P2PKH"],
        "P2SH_12": wallet_info_12["P2SH"],
        "P2WPKH_12": wallet_info_12["P2WPKH"],
        "P2WSH_12": wallet_info_12["P2WSH"],
        "P2WPKHinP2SH_12": wallet_info_12["P2WPKHinP2SH"],
        "P2WSHinP2SH_12": wallet_info_12["P2WSHinP2SH"],
        "Mnemonic_18": mnemonics_18,
        "PrivateKey_18": wallet_info_18["PrivateKey"],
        "P2PKH_18": wallet_info_18["P2PKH"],
        "P2SH_18": wallet_info_18["P2SH"],
        "P2WPKH_18": wallet_info_18["P2WPKH"],
        "P2WSH_18": wallet_info_18["P2WSH"],
        "P2WPKHinP2SH_18": wallet_info_18["P2WPKHinP2SH"],
        "P2WSHinP2SH_18": wallet_info_18["P2WSHinP2SH"],
        "Mnemonic_24": mnemonics_24,
        "PrivateKey_24": wallet_info_24["PrivateKey"],
        "P2PKH_24": wallet_info_24["P2PKH"],
        "P2SH_24": wallet_info_24["P2SH"],
        "P2WPKH_24": wallet_info_24["P2WPKH"],
        "P2WSH_24": wallet_info_24["P2WSH"],
        "P2WPKHinP2SH_24": wallet_info_24["P2WPKHinP2SH"],
        "P2WSHinP2SH_24": wallet_info_24["P2WSHinP2SH"]
    }

# Função principal para gerar carteiras Bitcoin em várias línguas usando multiprocessing
def generate_bitcoin_wallets():
    languages = [
        "english", "chinese_simplified", "chinese_traditional", "french",
        "italian", "japanese", "korean", "spanish", "turkish", "czech", "portuguese"
    ]
    
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(generate_wallet_info_for_language, languages)
    pool.close()
    pool.join()
    
    return results

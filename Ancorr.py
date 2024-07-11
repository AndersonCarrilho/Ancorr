import os
import gc  # Importa o módulo de coleta de lixo
import time  # Importa o módulo time para gerenciar o atraso

from bitcoin_wallet_generator import generate_bitcoin_wallets
from mnemonic_generator import generate_mnemonics_for_languages
from wallet_balance import main  # Importa a função main de wallet_balance

def clear_screen():
    # Verifica o sistema operacional para determinar o comando correto de limpeza de tela
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print("Bem-vindo ao Ancorr.py")
    print("Escolha uma opção:")
    print("1. Gerar Wallets Bitcoin")
    print("2. Gerar Mnemonics")
    print("3. Consultar Wallets")
    print("4. Modo Quântico")
    print("0. Sair")

def generate_bitcoin_wallets_menu():
    try:
        while True:
            results = generate_bitcoin_wallets()

            for result in results:
                language = result["Language"]
                mnemonics_12 = result["Mnemonic_12"]
                privatekey_12 = result["PrivateKey_12"]
                p2pkh_12 = result["P2PKH_12"]
                p2sh_12 = result["P2SH_12"]
                p2wpkh_12 = result["P2WPKH_12"]
                p2wsh_12 = result["P2WSH_12"]
                p2wpkhSegwit_12 = result["P2WPKHinP2SH_12"]
                p2wshSegwit_12 = result["P2WSHinP2SH_12"]

                mnemonics_18 = result["Mnemonic_18"]
                privatekey_18 = result["PrivateKey_18"]
                p2pkh_18 = result["P2PKH_18"]
                p2sh_18 = result["P2SH_18"]
                p2wpkh_18 = result["P2WPKH_18"]
                p2wsh_18 = result["P2WSH_18"]
                p2wpkhSegwit_18 = result["P2WPKHinP2SH_18"]
                p2wshSegwit_18 = result["P2WSHinP2SH_18"]

                mnemonics_24 = result["Mnemonic_24"]
                privatekey_24 = result["PrivateKey_24"]
                p2pkh_24 = result["P2PKH_24"]
                p2sh_24 = result["P2SH_24"]
                p2wpkh_24 = result["P2WPKH_24"]
                p2wsh_24 = result["P2WSH_24"]
                p2wpkhSegwit_24 = result["P2WPKHinP2SH_24"]
                p2wshSegwit_24 = result["P2WSHinP2SH_24"]

                print(f"""
Language: {language}
Mnemonic (12 words): {mnemonics_12}
PrivateKey [Hex]: {privatekey_12}
{'-' * 22} Bitcoin Addresses {'-' * 22}
Bitcoin P2PKH: {p2pkh_12}
Bitcoin P2SH: {p2sh_12}
Bitcoin P2WPKH: {p2wpkh_12}
Bitcoin P2WSH: {p2wsh_12}
Bitcoin P2WPKH in Segwit: {p2wpkhSegwit_12}
Bitcoin P2WSH in Segwit: {p2wshSegwit_12}

Mnemonic (18 words): {mnemonics_18}
PrivateKey [Hex]: {privatekey_18}
{'-' * 22} Bitcoin Addresses {'-' * 22}
Bitcoin P2PKH: {p2pkh_18}
Bitcoin P2SH: {p2sh_18}
Bitcoin P2WPKH: {p2wpkh_18}
Bitcoin P2WSH: {p2wsh_18}
Bitcoin P2WPKH in Segwit: {p2wpkhSegwit_18}
Bitcoin P2WSH in Segwit: {p2wshSegwit_18}

Mnemonic (24 words): {mnemonics_24}
PrivateKey [Hex]: {privatekey_24}
{'-' * 22} Bitcoin Addresses {'-' * 22}
Bitcoin P2PKH: {p2pkh_24}
Bitcoin P2SH: {p2sh_24}
Bitcoin P2WPKH: {p2wpkh_24}
Bitcoin P2WSH: {p2wsh_24}
Bitcoin P2WPKH in Segwit: {p2wpkhSegwit_24}
Bitcoin P2WSH in Segwit: {p2wshSegwit_24}
""")
    except KeyboardInterrupt:
        print("\nRetornando ao menu principal.")
    finally:
        # Limpa variáveis locais e coleta o lixo da memória
        del results, result, language, mnemonics_12, privatekey_12, p2pkh_12, p2sh_12, p2wpkh_12, p2wsh_12, p2wpkhSegwit_12, p2wshSegwit_12
        del mnemonics_18, privatekey_18, p2pkh_18, p2sh_18, p2wpkh_18, p2wsh_18, p2wpkhSegwit_18, p2wshSegwit_18
        del mnemonics_24, privatekey_24, p2pkh_24, p2sh_24, p2wpkh_24, p2wsh_24, p2wpkhSegwit_24, p2wshSegwit_24
        gc.collect()  # Coleta o lixo da memória

def generate_mnemonics_menu():
    try:
        results = generate_mnemonics_for_languages()
    
        for result in results:
            for mnemonic in result:
                print(mnemonic)
            print("=" * 20)  # Separador entre idiomas
    except Exception as e:
        print(f"Ocorreu um erro ao gerar mnemônicos: {e}")

def wallet_balance_menu():
    try:
        main()  # Chama a função main de wallet_balance para consultar os wallets
    except Exception as e:
        print(f"Ocorreu um erro ao consultar os wallets: {e}")

if __name__ == "__main__":
    while True:
        menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            generate_bitcoin_wallets_menu()
            time.sleep(3)  # Atraso de 3 segundos ao retornar ao menu principal
        elif option == "2":
            generate_mnemonics_menu()
            time.sleep(3)  # Atraso de 3 segundos ao retornar ao menu principal
        elif option == "3":
            wallet_balance_menu()
            time.sleep(3)  # Atraso de 3 segundos ao retornar ao menu principal
        elif option == "4":
            # Implementar função para Modo Quântico
            print("Opção em desenvolvimento...")
        elif option == "0":
            print("Saindo do programa...")
            break  # Sai do loop principal e encerra o programa
        else:
            print("Opção inválida. Escolha novamente.")

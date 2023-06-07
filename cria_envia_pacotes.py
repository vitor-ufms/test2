from scapy.all import Ether, IP, TCP, Raw, sendp, hexdump, wrpcap
from threading import Thread

# Criação do pacote
mensagem = "Conteúdo do pacote"  # a \ é para continuar código em outra linhas
pacote = Ether(src="00:11:22:33:44:55", dst="FF:FF:FF:FF:FF:FF") / \
         IP(src="192.168.0.55", dst="10.10.0.13") / \
         TCP(sport=1234, dport=80) / \
         Raw(mensagem.encode("utf-8"))

# Envio do pacote
#pacote.show()

print("###############################")
hexdump(pacote) # mostra igual o wireshark
print("##########################")


# Salve o pacote em um arquivo pcap
wrpcap("output.pcap", pacote)

# hex_representation = hexdump(pacote, dump=True)
# linhas = hex_representation.split("\n")
# for linha in linhas:
#     print(linha[5:53].replace(" ", ", 0x")[2:].replace(" 0x,",""))

# def f1(count=100):
#     #sendp(pacote, loop=True)
#     sendp(pacote, count=count)

# Thd1 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend
# Thd2 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend
# Thd3 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend
# Thd4 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend
# Thd5 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend
# Thd6 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend
# Thd7 = Thread(target=f1,args=[1000000]) # Cria uma thread para rodar o backend

# Thd1.start()
# Thd2.start()
# Thd3.start()
# Thd4.start()
# Thd5.start()
# Thd6.start()
# Thd7.start()

# # Espera as threads terminarem
# Thd1.join()
# Thd2.join()
# Thd3.join()
# Thd4.join()
# Thd5.join()
# Thd6.join()
# Thd7.join()


print("Programa finalizado")
#sendp(pacote, loop=True)
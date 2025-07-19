import os 
import datetime
import socket

def obter_ip():
    """Obtem o IP da maquina."""
    try:
        #Obtém o hostname da maquina
        hostname = socket.gethostname()
        #Retorna o IP da maquina
        ip = socket.gethostbyname(hostname)
        return ip
    except Exception as e:
        return f"Erro ao obter IP: {e}"
    
def registrar_log(cidade, ip):
    #Obtém a data e a hora atuais
    data_hora_atual = datetime.datetime.now()
    #Formata a data e hora
    data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
    #Obtém o diretório atual
    diretorio_atual = os.getcwd()

    #Prepara a mensagem a ser salva
    log_message = (f"Data e hora: {data_hora_formatada}, "
                   f"Cidade: {cidade}, "
                   f"IP: {ip}, "
                   f"Pasta: {diretorio_atual}\n")
    
    #Salva a mensagem no arquivo log.txt
    with open('logs.txt', 'a', encoding= 'utf-8') as arquivo:
        arquivo.write(log_message)

if __name__ == "__main__":
    cidade = input("Digite a cidade onde você está:  ")
    ip = obter_ip()
    registrar_log(cidade, ip)
    print("Registro salvo com sucesso.")
    
    
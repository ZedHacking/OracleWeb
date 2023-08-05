import webbrowser
import socket
import time
from colored import fg, attr

# Função para imprimir o cabeçalho do menu
def print_header(text):
    color = fg('purple')
    print(f"{color}{text}{attr(0)}")

# Função para imprimir as opções do menu
def print_option(number, text):
    color = fg('cyan')
    print(f"{color}{number}. {text}{attr(0)}")

# Função para consultar o IP do site
def check_website_status(site):
    try:
        ip = socket.gethostbyname(site)
        print(f"\n{fg('magenta')}=== Informações do site {site} ===")
        print(f"IP do site: {ip}")

        # Implemente aqui a verificação das portas abertas e se o site está fora do ar

    except socket.gaierror:
        print(f"{fg('red')}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")

# Função para verificar o tempo de resposta do site
def get_website_response_time(site):
    try:
        ip = socket.gethostbyname(site)
        start_time = time.time()
        socket.create_connection((ip, 80), timeout=10)
        end_time = time.time()
        response_time = end_time - start_time
        print(f"\n{fg('magenta')}=== Tempo de Resposta do site {site} ===")
        print(f"Tempo de resposta: {response_time:.2f} segundos")
    except socket.gaierror:
        print(f"{fg('red')}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")
    except socket.timeout:
        print(f"{fg('red')}O site {site} não respondeu em um tempo razoável.")

# Função para verificar se o site está fora do ar
def check_site_status(site):
    try:
        ip = socket.gethostbyname(site)
        # Implemente aqui a verificação se o site está fora do ar
        print(f"\n{fg('magenta')}=== Status do site {site} ===")
        print(f"Verificação do status em andamento...")
    except socket.gaierror:
        print(f"{fg('red')}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")

# Função para verificar se o site é UDP ou TCP
def check_site_protocol(site):
    try:
        # Implemente aqui a verificação se o site é UDP ou TCP
        print(f"\n{fg('magenta')}=== Protocolo do site {site} ===")
        print(f"Verificação do protocolo em andamento...")
    except:
        print(f"{fg('red')}Ocorreu um erro ao verificar o protocolo do site {site}.")

# Função para verificar as portas abertas do site
def check_open_ports(site):
    try:
        ip = socket.gethostbyname(site)
        print(f"\n{fg('magenta')}=== Portas Abertas do site {site} ===")
        
        port_found = False  # Variável de controle para verificar se encontrou alguma porta aberta
        
        for port in range(1, 1025):  # Verifica as portas de 1 a 1024
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Porta {port} está aberta.")
                port_found = True  # Marca a variável como True caso encontre uma porta aberta
                break  # Sai do loop, pois já encontrou uma porta aberta
            sock.close()
        
        if not port_found:
            print(f"Todas as portas estão fechadas no site {site}.")
    except socket.gaierror:
        print(f"{fg('red')}Não foi possível encontrar o IP para o site {site}. O site pode estar fora do ar ou não existe.")

# Função para redirecionar o usuário para o link "https://utilities-hon-this-speak.trycloudflare.com"
def redirect_user():
    link = "https://utilities-hon-this-speak.trycloudflare.com"
    print(f"\n{fg('magenta')}=== Redirecionando para {link} ===")
    webbrowser.open(link)

# Loop principal do menu
while True:
    print_header("=== MENU ===")
    print_option(1, "Consultar IP de um site")
    print_option(2, "Verificar se o site está fora do ar")
    print_option(3, "Verificar tempo de resposta do site")
    print_option(4, "Verificar se o site é UDP ou TCP")
    print_option(5, "Verificar portas abertas do site")
    print_option(6, "Créditos")
    print_option(7, "Não entre")
    print_option(0, "Sair")
    
    choice = int(input(f"{fg('cyan')}Escolha uma opção: {attr(0)}"))

    if choice == 1:
        site = input(f"{fg('yellow')}Digite o nome do site: {attr(0)}")
        check_website_status(site)
    elif choice == 2:
        site = input(f"{fg('yellow')}Digite o nome do site: {attr(0)}")
        check_site_status(site)
    elif choice == 3:
        site = input(f"{fg('yellow')}Digite o nome do site: {attr(0)}")
        get_website_response_time(site)
    elif choice == 4:
        site = input(f"{fg('yellow')}Digite o nome do site: {attr(0)}")
        check_site_protocol(site)
    elif choice == 5:
        site = input(f"{fg('yellow')}Digite o nome do site: {attr(0)}")
        check_open_ports(site)
    elif choice == 6:
        print(f"\n{fg('green')}Créditos: @zedhacking {attr(0)}")
    elif choice == 7:
        redirect_user()
    elif choice == 0:
        print(f"{fg('red')}Saindo do programa...{attr(0)}")
        break
    else:
        print(f"{fg('red')}Opção inválida. Tente novamente.{attr(0)}")

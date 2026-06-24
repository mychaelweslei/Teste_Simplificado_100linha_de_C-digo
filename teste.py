import pyautogui
import pyperclip
import time

# Adicione suas novas perguntas dentro da lista abaixo, separadas por vírgula
perguntas_lista = [# --- PROTOCOLO E PROCESSOS (Com números de protocolo simulados em seguida) ---
    # --- PROTOCOLO / CONSULTA DE PROCESSOS (Fluxo Pergunta -> Dado Separado) ---
    "Quero consultar o andamento do meu processo administrativo de despesa.",
    "00004112/2026",
    "Ver andamento do processo da minha empresa que deu entrada ano passado.",
    "00031721/2024",
    "Como está a situação do meu protocolo mais antigo na prefeitura?",
    "00030284/2014",
    "Preciso de uma atualização sobre o andamento deste processo aqui:",
    "00002734/2026",
    "Poderia checar se o meu requerimento deste ano já foi movimentado?",
    "00002727/2026",
    "Gostaria de saber o status atual desse processo de despesa pública:",
    "00002729/2026",
    "Acompanhar andamento do processo aberto recentemente no meu setor.",
    "00002736/2026",
    "Ver histórico de despachos do meu protocolo de 2021.",
    "00014423/2021",
    "Consultar documentos anexados e resposta da prefeitura para este processo:",
    "00011231/2021",
    "Quero saber se o processo de empenho e despesa já foi aprovado.",
    "00002755/2026",

    # --- IPTU / CADASTRO / EXTRATO (Fluxo Pergunta -> CPF/CNPJ/Inscrição Cadastrada) ---
    "Quero o extrato de débitos e IPTU associados a este CNPJ de Cabo Frio.",
    "02.382.073/0001-10",
    "Preciso emitir a cota única do IPTU deste ano para a minha empresa.",
    "04.307.683/0001-85",
    "Puxar segunda via do carnê completo do IPTU pelo meu CPF por favor.",
    "234.966.657-34",
    "Como faço para consultar os imóveis e dívidas no meu documento?",
    "05.679.547/0001-89",
    "Verificar se existe alguma pendência fiscal de IPTU ou taxa de lixo para este CNPJ:",
    "33.050.071/0001-58",
    "Emitir boleto de IPTU em atraso e ver o cadastro imobiliário deste favorecido:",
    "12.292.556/0001-88",
    "Preciso da segunda via do IPTU de Cabo Frio do meu imóvel no Braga.",
    "Inscrição Municipal 662302",
    "Quero pagar a cota única do IPTU com desconto da minha casa na Praia do Forte.",
    "Inscrição Municipal 554433",
    "Baixar PDF do IPTU deste ano do loteamento em Unamar.",
    "Inscrição Municipal 102245",
    "Preciso do IPTU parcelado, todas as parcelas em aberto do Peró.",
    "Inscrição Municipal 884321",
    "Como puxar o IPTU da minha inscrição municipal de Tamoios?",
    "Inscrição Municipal 334190",
    "Segunda via de IPTU carnê completo de casa no Jardim Esperança.",
    "CPF 123.456.789-10",
    "Quero a cota única do Imposto Predial e Territorial Urbano de São Cristóvão.",
    "Inscrição Municipal 776211",
    "IPTU atrasado do meu imóvel na Passagem.",
    "Inscrição Municipal 199200",
    "Gerar boleto de IPTU vencido de casa no Foguete.",
    "Inscrição Municipal 441255",
    "Como consigo o carnê do IPTU em PDF do condomínio no Ogiva?",
    "Inscrição Municipal 992377",
    "Me envia a segunda via da cota única do IPTU do Jacaré.",
    "Inscrição Municipal 112234",
    "Quero pagar o IPTU atrasado do ano passado da loja no Centro.",
    "CNPJ 23.456.789/0001-00",

    # --- ALVARÁ, TAXAS E CERTIDÕES (Fluxo Pergunta -> Inscrição/Documento) ---
    "Quero emitir o alvará de funcionamento da minha empresa.",
    "Inscrição Municipal 1006248",
    "Consultar situação cadastral e alvará da loja no Centro.",
    "Inscrição Municipal 1006248",
    "Preciso do alvará de funcionamento do quiosque da Praia do Forte.",
    "Inscrição Municipal 1000000",
    "Baixar alvará de localização da minha empresa pelo CNPJ em Tamoios.",
    "CNPJ 05.679.547/0001-89",
    "Quero baixar o PDF do alvará do restaurante no Braga.",
    "Inscrição Municipal 1006248",
    "Imprimir segunda via do alvará de funcionamento de Cabo Frio.",
    "Inscrição Municipal 1006248",
    "Como puxar certidão negativa de débitos do meu imóvel no Algodoal?",
    "Inscrição Municipal 554433",
    "Quero pagar a taxa de coleta de lixo de Tamoios / taxas municipais.",
    "CPF 776.554.332-11",
    "Quero a certidão de regularidade fiscal do meu CNPJ.",
    "CNPJ 33.050.071/0001-58",
    "Consultar todas as taxas pendentes da minha inscrição municipal no Braga.",
    "Inscrição Municipal 1006248"]

def iniciar_automacao():
    # Coordenada atualizad conforme o seu print (campo "Write a message...")
    X_CHAT, Y_CHAT = 575, 1001 #<<<<<<< Troque para as coordenadas corretas do campo de mensagem do chat
    print("--- Script de Automação ---")
    print(f"Total de perguntas: {len(perguntas_lista)}")
    print("Iniciando em 5 segundos... Abra a tela do chat.")
    time.sleep(5)

    for i, pergunta in enumerate(perguntas_lista, 1):
        print(f"[{i}/{len(perguntas_lista)}] Enviando: '{pergunta}'")
        
        # 1. Clica exatamente na coordenada (1195, 830)
        pyautogui.click(X_CHAT, Y_CHAT)
        time.sleep(0.5) # Pequena pausa para garantir o clique
        
        # 2. Copia o texto para a área de transferência e cola
        pyperclip.copy(pergunta)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        
        # 3. Pressiona Enter para enviar
        pyautogui.press('enter')

        # 4. Tempo de espera entre o envio de uma mensagem e outra (ajuste se precisar)
        print("   Aguardando intervalo para a próxima mensagem (35s)...\n")
        time.sleep(35)# AQUI FICA PO TEMPO PODE MODIFICAR O TEMPO DE ESPERA ENTRE AS MENSAGENS

    print("✅ Sucesso! Todas as mensagens foram enviadas.")

if __name__ == "__main__":
    try:
        iniciar_automacao()
    except KeyboardInterrupt:
        print("\nAutomação interrompida pelo usuário.")
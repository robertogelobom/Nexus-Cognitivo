# -*- coding: utf-8 -*-
"""Nexus_cognitivo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eKSP3YVdPQPna3E6qmaae7YrXPx9sjXH
"""

!pip install google-generativeai

import os
import google.generativeai as genai
from google.generativeai import types
import datetime
import random
import time  
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"


def get_gemini_response(prompt):
    """Obtém uma resposta do modelo Gemini."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Erro: A chave da API do Gemini não foi configurada como variável de ambiente."
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao obter resposta do Gemini: {e}"

def explicar_tecnica_estudo():
    """Solicita ao usuário uma técnica de estudo e usa o Gemini para explicá-la."""
    tecnica = input("Sobre qual técnica de estudo você gostaria de saber mais?(Ex.: Pomodoro, Método de Feynman, Repetição Espaçada, Recordação Ativa, Mapa Mental)\n")
    prompt = f"""Explique detalhadamente a técnica de estudo '{tecnica}'.
    Inclua os principais passos para aplicá-la, os benefícios esperados e exemplos práticos de como um estudante pode usá-la."""
    return get_gemini_response(prompt)

def definir_metas():
    """Solicita ao usuário que defina suas metas de estudo."""
    return input("Qual é a sua meta de estudo principal para hoje/esta semana? Seja específico.\n")

def criar_plano_estudo(meta):
    """Cria um plano de estudo personalizado com a ajuda do Gemini."""
    prompt = f"""Com base na seguinte meta de estudo: "{meta}", crie um plano de estudo detalhado.
    Inclua os tópicos a serem estudados, a ordem sugerida, o tempo estimado para cada tópico e sugestões de técnicas de estudo que podem ser úteis (incluindo Pomodoro, Método de Feynman, Repetição Espaçada, Recordação Ativa e Mapa Mental).
    Formate o plano de forma clara e organizada, com marcadores ou listas."""
    return get_gemini_response(prompt)

def definir_tempo_lembrete():
    """Solicita ao usuário o tempo para o lembrete e pergunta se deseja iniciar o cronômetro."""
    while True:
        tempo_str = input("Em quantos minutos você gostaria de receber um lembrete? (Digite um número).\n")
        try:
            tempo = int(tempo_str)
            if tempo > 0:
                return tempo * 60  # Converter para segundos
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def executar_cronometro(duracao):
    """Executa um cronômetro simples e exibe uma 'notificação'."""
    print(f"Cronômetro iniciado para {duracao // 60} minutos.")
    time.sleep(duracao)
    print("\n⏰ Tempo acabou! Faça uma pausa ou revise seu material.")

def enviar_lembrete(tempo):
    """Define um lembrete e oferece a opção de iniciar o cronômetro."""
    print(f"\nLembrete configurado para daqui a {tempo // 60} minutos.")
    iniciar_cronometro = input("Gostaria de iniciar um cronômetro com a mesma duração? (sim/não): ").lower()
    if iniciar_cronometro == "sim":
        executar_cronometro(tempo)

def monitorar_progresso():
    """Solicita ao usuário que descreva seu progresso."""
    return input("Como você avalia seu progresso até agora? Quais tópicos você já cobriu?\n")

def obter_recursos_foco():
    """Utiliza o Gemini para obter recursos de foco com base nas preferências do usuário."""
    preferencia = input("Você tem alguma preferência específica para recursos de foco (ex: tipo de música, sons da natureza, aplicativos)? (opcional)\n")
    prompt = f"""Sugira uma lista de 3 a 5 recursos úteis para melhorar o foco e a concentração durante os estudos.
    Para cada recurso, inclua um breve título, uma descrição e, se aplicável, um link.
    Se o usuário mencionou alguma preferência ('{preferencia}'), tente incluir recursos relacionados a essa preferência."""
    return get_gemini_response(prompt)


def obter_exercicio_mindfulness():
    """Sugere um exercício rápido de mindfulness."""
    exercicios = [
        "Concentre-se na sua respiração por um minuto. Sinta o ar entrando e saindo do seu corpo.",
        "Observe os sons ao seu redor sem julgamento. Apenas note o que você ouve.",
        "Preste atenção às sensações do seu corpo enquanto você está sentado. Sinta o contato com a cadeira e seus pés no chão."
    ]
    return f"Aqui está um exercício rápido de mindfulness:\n{random.choice(exercicios)}"

def responder_duvidas():
    """Solicita a dúvida do usuário e tenta responder com o Gemini."""
    duvida = input("Qual é a sua dúvida sobre o material de estudo? Seja específico.\n")
    prompt = f"""Responda à seguinte dúvida de um estudante da melhor forma possível, com explicações claras e concisas:
    "{duvida}"
    Se a dúvida não estiver clara ou precisar de mais contexto, peça educadamente por mais informações."""
    return get_gemini_response(prompt)

def fornecer_feedback(progresso):
    """Fornece feedback e motivação com base no progresso do usuário."""
    prompt = f"""Com base na seguinte descrição do progresso de um estudante: "{progresso}", forneça feedback encorajador e motivacional.
    Destaque os pontos positivos e ofereça sugestões construtivas para continuar avançando. Mantenha um tom positivo e de apoio."""
    return get_gemini_response(prompt)

def adaptar_dinamicamente(progresso_atual, plano_anterior):
    """Sugere adaptações ao plano de estudo com base no progresso."""
    prompt = f"""O estudante relatou o seguinte progresso: "{progresso_atual}". O plano de estudo anterior era:
    "{plano_anterior}".
    Com base nisso, sugira possíveis adaptações ao plano de estudo. Considere o que foi concluído, as dificuldades encontradas e o tempo restante disponível.
    Ofereça sugestões específicas para ajustar o plano de forma realista e eficaz. Mencione as técnicas de estudo (Pomodoro, Método de Feynman, Repetição Espaçada, Recordação Ativa e Mapa Mental) e recursos de foco (como música, sons da natureza e aplicativos) como possíveis estratégias para o novo plano."""
    return get_gemini_response(prompt)

def main():
    print("Olá! Sou seu bot de apoio para estudos. Como posso te ajudar hoje?")

    plano_de_estudo = None
    progresso = None  # Inicializa progresso
    meta = None # Inicializa meta

    while True:
        print("\nEscolha uma opção:")
        print("1. Explicar técnica de estudo")
        print("2. Definir metas de estudo")
        print("3. Criar plano de estudo")
        print("4. Definir lembrete")
        print("5. Monitorar progresso")
        print("6. Obter recursos de foco")
        print("7. Exercício de mindfulness")
        print("8. Tirar dúvidas")
        print("9. Receber feedback")
        print("10. Adaptar plano de estudo")
        print("0. Sair")

        opcao = input("Digite o número da sua escolha: ")

        if opcao == "1":
            explicacao = explicar_tecnica_estudo()
            print(explicacao)
        elif opcao == "2":
            meta = definir_metas()
            print(f"Sua meta definida é: {meta}")
        elif opcao == "3":
            if not meta:
                print("Por favor, defina sua meta de estudo primeiro (opção 2).")
            else:
                print("Gerando seu plano de estudo personalizado...")
                plano_de_estudo = criar_plano_estudo(meta)
                print("\nSeu plano de estudo:\n", plano_de_estudo)
        elif opcao == "4":
            tempo_lembrete = definir_tempo_lembrete()
            if tempo_lembrete:
                enviar_lembrete(tempo_lembrete)
        elif opcao == "5":
            progresso = monitorar_progresso()
            print(f"Seu progresso relatado: {progresso}")
        elif opcao == "6":
            recursos = obter_recursos_foco()
            print(recursos)
        elif opcao == "7":
            exercicio = obter_exercicio_mindfulness()
            print(exercicio)
        elif opcao == "8":
            resposta = responder_duvidas()
            print("Resposta:\n", resposta)
        elif opcao == "9":
            if not progresso:
                progresso = input("Por favor, descreva seu progresso para que eu possa te dar feedback:\n")
            feedback = fornecer_feedback(progresso)
            print("Feedback:\n", feedback)
        elif opcao == "10":
            if not progresso or not plano_de_estudo:
                print("Por favor, relate seu progresso (opção 5) e tenha um plano de estudo (opção 3) para que eu possa ajudar a adaptá-lo.")
            else:
                print("Adaptando seu plano de estudo com base no seu progresso...")
                novo_plano = adaptar_dinamicamente(progresso, plano_de_estudo)
                print("\nPlano de estudo adaptado:\n", novo_plano)
                plano_de_estudo = novo_plano
        elif opcao == "0":
            print("Obrigado por usar o bot de apoio para estudos! Bons estudos!")
            break
        else:
            print("Opção inválida. Por favor, digite um número entre 0 e 10.")

if __name__ == "__main__":
    main()

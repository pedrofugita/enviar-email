# selecionar ação
import yfinance as yf

ticker = "PETR4.SA"
#ticker = input("Digite o código da ação: ")

# selecionar período
dados = yf.Ticker(ticker).history("5y")
print("\n", dados)
fechamento = dados['Close']
print("\n", fechamento)

# plotar gráfico
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
fechamento.plot()
plt.title(f"Preço de Fechamento de {ticker}")
plt.xlabel("Data")
plt.ylabel("Preço de Fechamento")
plt.grid(True)
plt.show()

# montar análises
print("\n")
maxima = round(fechamento.max(),2)
minima = round(fechamento.min(),2)
atual = round(fechamento[-1],2)
print(maxima)
print(minima)
print(atual)

# enviar email automático
import pyautogui
import time
import pyperclip

# pausa entre as ações
pyautogui.PAUSE = 1

# abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
#pyautogui.click(x=945, y=1054)

# entrar no link
pyautogui.click(x=2324, y=51)
pyautogui.write("https://gmail.com")
pyautogui.press("enter")
time.sleep(8)   # ajustar de acordo com a velocidade da internet

# clicar no botão escrever
pyautogui.click(x=2038, y=180)

# preencher destinatário
pyperclip.copy("pedrofugita98@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# preencher assunto
pyperclip.copy("Análise diária")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# preencher corpo do email
mensagem = f"""
Prezado Gestor,

Seguem as análises diárias da ação {ticker} referentes aos últimos meses:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Cotação atual: R${atual}

Qualquer dúvida estou a disposição.
Att, Pedro
"""
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# clicar no botão de enviar
pyautogui.click(x=2848, y=790)
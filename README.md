# psel-shinier-2023-iot
Desafio da Fase Técnica do processo seletivo da Shinier

## Descrição do Projeto
Esse projeto é um programa escrito em Python capaz de baixar a versão mais recente de si mesmo de um repositório de controle de versão e se atualiza regularmente. Além disso o programa possui uma interface de usuário simples. O programa foi desenvolvido para rodar em um Raspberry Pi.

## Funcionalidades
1. **Auto-atualização:** o programa é capaz de verificar regularmente se há uma versão nova de si no repositório do Git e, se houver, ele baixa a e substitui a versão atual pela nova.
2. **Inicialização Automática**: o programa é configurado para iniciar automaticamente quando o Raspberry Pi for ligado.
3. **Interface de Usuário**: o programa possui uma interface de usuário simples, onde se pode digitar o nome do candidato e, ao apertar um botão, aparecerá um popup com o nome do candidato seguido do texto "candidato processo seletivo Shinier IoT".a

## Pré-Requisitos
- Python 3 (recomenda-se usar a versão mais atual disponível)
- Raspberry Pi (emuladores, como VMs ou Docker, podem ser utilizados como alternativas)

## Instalação

Primeiramente é importante instalar as dependências:
- GitPython:
```
pip3 install GitPython
```
- Tkinter
```
pip3 install tk
```
Após isso é só clonar esse repositório e entrar na pasta:
```
cd psel-shinier-2023-iot
```
E assim executar o programa:
```
python3 main.py
```

Abaixo está a configuração do Raspberry Pi para rodar o programa automaticamente.
### Configuração do Raspberry Pi

Para o programa iniciar automaticamente quando o Raspberry Pi é ligado é necessário:  
Abrir o rc.local:
```
sudo nano /etc/rc.local
```
Adicionar o programa no fim do arquivo, antes do `exit 0`:
```
sudo python3 <caminho_do_programa> &
```
Exemplo:
```
sudo python3 /home/pi/main.py &
```
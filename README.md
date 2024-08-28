# QR Code Generator

Um simples gerador de QR Code em Python, que permite gerar QR Codes a partir de URLs e salvar a imagem ou imprimir uma representação ASCII no console.

## Instalação

Caso queira instalar na sua maquina execute os seguintes comandos:

```bash
  git clone https://github.com/GuiCezaF/QRify.git
  cd QRify  
  pip install -r requirements.txt
  pyinstaller --onefile --name qrify main.py
  sudo mv dist/qrify /usr/local/bin/
```

## Uso

O script principal permite gerar QR Codes a partir de URLs. Ele oferece a opção de salvar o QR Code como uma imagem PNG ou imprimi-lo como uma arte ASCII no console.

Executando o Script
Você pode executar o script a partir da linha de comando com as seguintes opções:

- --url: URL para gerar o QR Code (obrigatório).
- --img: Se essa flag for fornecida, o QR Code será salvo como uma imagem PNG (qrcode.png). Se não fornecida, o QR Code será impresso como arte ASCII.

## Exemplos

### Gerar QR Code e salvar como imagem

```bash
qrify --url "https://www.exemplo.com" --img
```

isso gerará um QR Code para a URL fornecida e salvará a imagem como qrcode.png.

### Gerar QR Code e imprimir no console

```bash
qrify --url "https://www.exemplo.com"
```

Isso gerará um QR Code para a URL fornecida e imprimirá uma representação ASCII no console.

## Licença

Este projeto está licenciado sob a [MIT License.](./LICENSE.MD)

# Conversor PDF/Word

Este projeto é uma aplicação de interface gráfica em Python desenvolvida para converter arquivos PDF em arquivos Word e vice-versa. A aplicação utiliza a biblioteca `tkinter` para criar uma interface gráfica simples e intuitiva, permitindo que os usuários escolham arquivos e realizem as conversões com facilidade.

## Funcionalidades

- **Converter PDF para Word:** A aplicação permite selecionar um arquivo PDF e convertê-lo em um arquivo Word (.docx).
- **Converter Word para PDF:** A aplicação permite selecionar um arquivo Word (.docx) e convertê-lo em um arquivo PDF.

## Ferramentas e Bibliotecas Utilizadas

- **tkinter:** Biblioteca padrão do Python para a criação de interfaces gráficas. É utilizada para a construção da interface do usuário e a interação com os botões de conversão.
- **fpdf:** Biblioteca que possibilita a geração de arquivos PDF a partir de conteúdos textuais. Neste projeto, é usada para criar o PDF a partir de um documento Word.
- **docx (python-docx):** Biblioteca para manipulação de arquivos `.docx`. Usada para ler o conteúdo de arquivos Word e processá-los para a conversão em PDF.
- **pdf2docx:** Ferramenta para converter arquivos PDF em arquivos Word. Facilita a conversão do formato PDF para o formato `.docx`.
- **os:** Biblioteca padrão para interações com o sistema operacional, usada para manipulação de caminhos e arquivos.

## Estrutura do Código

- **Função `pdf_to_word()`:** Realiza a conversão de um arquivo PDF em um arquivo Word. Utiliza a função `filedialog.askopenfilename` para abrir uma janela de seleção de arquivos PDF. Em seguida, usa `pdf2docx.Converter` para realizar a conversão do arquivo.
- **Função `word_to_pdf()`:** Realiza a conversão de um arquivo Word em PDF. Abre uma janela de seleção para arquivos Word e utiliza `fpdf.FPDF` para criar um novo PDF a partir do conteúdo lido com a biblioteca `docx`.
- **Interface Gráfica:** A interface gráfica é criada com `tkinter`, com dois botões principais para iniciar cada tipo de conversão. A interface é configurada para ser simples e funcional.

Na interface gráfica que se abrirá, clique no botão correspondente ao tipo de conversão desejado (PDF para Word ou Word para PDF) e selecione o arquivo a ser convertido.

## Observações
Este projeto é uma ferramenta básica para conversão entre formatos PDF e Word. Devido a limitações nas bibliotecas de conversão, o layout dos arquivos convertidos pode não ser idêntico ao do arquivo original em alguns casos.
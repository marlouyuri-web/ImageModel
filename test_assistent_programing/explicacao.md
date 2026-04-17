## explicacao.md atualizada para o código refatorado

### Estrutura geral
- `Calculator` é a classe que encapsula a interface gráfica e o comportamento da calculadora.
- São usadas constantes no topo do arquivo para separar dados de configuração (`BUTTON_LAYOUT`, `WINDOW_TITLE`, etc.) da lógica de interface.
- A função `main()` inicializa a janela e executa o loop principal do `tkinter`.

---

### Importações e constantes
- `import tkinter as tk` importa a biblioteca de interface gráfica.
- `from tkinter import messagebox` importa o componente de diálogo para erros.
- As constantes tornam o código mais legível e facilitam ajustes futuros.

---

### Inicialização do objeto `Calculator`
- `def __init__(self, root: tk.Tk) -> None:` define o construtor da classe.
- `self.expression` guarda a expressão matemática atual.
- `self.display_value = tk.StringVar()` cria o valor ligado ao campo de exibição.
- O construtor chama métodos específicos para configurar a janela e criar widgets:
  - `configure_root()`
  - `create_display()`
  - `create_buttons()`
  - `create_control_buttons()`

---

### Configuração da janela
- `configure_root()` define o título e o tamanho da janela.
- Separar essa configuração em um método deixa o construtor mais limpo.

---

### Display da calculadora
- `create_display()` cria um `tk.Entry` para mostrar a expressão ou o resultado.
- O widget usa `textvariable=self.display_value` para manter o texto sincronizado automaticamente.

---

### Botões numéricos e operadores
- `create_buttons()` percorre `BUTTON_LAYOUT` e cria cada botão em sua posição de grade.
- `create_button()` é um método auxiliar que encapsula a construção e o posicionamento de cada botão.
- Esse design evita repetição e melhora a clareza.

---

### Botões de controle
- `create_control_buttons()` adiciona os botões `C` e `CE`.
- `C` limpa toda a expressão.
- `CE` apaga apenas o último caractere.

---

### Lógica de clique
- `on_button_click(self, label: str) -> None:` processa o valor do botão clicado.
- Se o botão for `=`, chama `evaluate_expression()`.
- Caso contrário, chama `append_character(label)`.

---

### Atualização do display
- `append_character()` concatena um caractere à expressão e atualiza a interface.
- `update_display()` escreve `self.expression` em `self.display_value`.
- Isso separa o estado interno da forma de exibição.

---

### Avaliação da expressão
- `evaluate_expression()` tenta calcular o resultado com `eval()`.
- O método trata exceções específicas: `SyntaxError`, `ZeroDivisionError`, `TypeError` e `NameError`.
- Se houver erro, chama `show_error()`.

---

### Tratamento de erros
- `show_error()` exibe um `messagebox` com a mensagem `Expressão inválida`.
- Em seguida, limpa a expressão para evitar estado inconsistente.

---

### Limpeza e correção
- `clear()` reinicia a expressão e atualiza o display.
- `clear_entry()` remove o último caractere da expressão e atualiza o display.

---

### Inicialização do programa
- `main()` cria a instância do `tk.Tk()` e instancia `Calculator`.
- `if __name__ == '__main__':` garante que o código rode apenas quando o arquivo for executado diretamente.

## Benefícios da refatoração
- Responsabilidade única: cada método tem uma função clara.
- Reutilização: `create_button()` reduz duplicação.
- Legibilidade: constantes e métodos nomeados tornam o fluxo mais fácil de entender.
- Manutenção: ajustes de layout e comportamento são mais simples de aplicar.
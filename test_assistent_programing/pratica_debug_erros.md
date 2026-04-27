## Código com Erros
def calcular_media(notas):
    if len(notas) = 0:
        return 0
    
    soma = 0
    for nota in notas
        soma += nota
    
    media = soma / len(notas)
    return media

# Entrada do usuário
entrada = input("Digite as notas separadas por vírgula: ")
notas = [int(x) for x in entrada.split(',')]

resultado = calcular_media(notas)
print(f"A média das notas é: {resultado}")
```

---

## Erros Identificados

### ❌ Erro 1: Operador de Comparação Incorreto (Linha 2)

**Linha com erro:**
```python
if len(notas) = 0:
```

**Tipo:** Erro de Sintaxe

**Causa:** 
- Usar `=` (atribuição) em vez de `==` (comparação)
- O operador `=` é para atribuir valores, enquanto `==` é para comparar
- Isso causará um `SyntaxError` ao executar o código

**Correção:**
```python
if len(notas) == 0:
```

---

### ❌ Erro 2: Dois-pontos Faltando (Linha 6)

**Linha com erro:**
```python
for nota in notas
    soma += nota
```

**Tipo:** Erro de Sintaxe

**Causa:**
- A instrução `for` requer `:` (dois-pontos) ao final
- Sem ele, Python não consegue interpretá-lo corretamente
- Causará um `SyntaxError: invalid syntax`

**Correção:**
```python
for nota in notas:
    soma += nota
```

---

### ❌ Erro 3: Conversão de Tipo Ausente (Linha 15)

**Linha com erro:**
```python
notas = [int(x) for x in entrada.split(',')]
```

**Contexto:** O código tenta converter strings em inteiros, mas se o usuário não digitar números válidos, causará um `ValueError`. 

**Tipo:** Erro de Lógica/Validação

**Causa:**
- Não há tratamento de erros para entradas inválidas
- Se o usuário digitar letras, o `int()` lançará exceção
- O código não valida se os valores são realmente números

**Melhor Correção (com tratamento de erro):**
```python
try:
    notas = [int(x.strip()) for x in entrada.split(',')]
except ValueError:
    print("Erro: Digite apenas números separados por vírgula!")
    notas = []
```

---

## Resumo dos Erros

| Erro | Linha | Tipo | Problema | Solução |
|------|-------|------|----------|---------|
| 1 | 2 | Sintaxe | `=` em vez de `==` | Usar `==` para comparação |
| 2 | 6 | Sintaxe | Falta `:` após `for` | Adicionar `:` |
| 3 | 15 | Lógica | Sem validação de entrada | Adicionar `try/except` |

---

## Aprendizados Importantes

✅ **Dica 1:** Operadores de comparação (`==`, `!=`, `>`, `<`) são diferentes de atribuição (`=`)

✅ **Dica 2:** Estruturas de controle (`if`, `for`, `while`, `def`) **sempre** terminam com `:`

✅ **Dica 3:** Sempre valide entradas do usuário com `try/except` para evitar crashes


palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'MERCADO', 'FUTURO')

for p in palavras:
    print('\nNa palavra', p.upper(), 'temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
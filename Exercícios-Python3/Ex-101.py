def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade}: NÃO VOTA AINDA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: VOTO OPCIONAL!'
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO!'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

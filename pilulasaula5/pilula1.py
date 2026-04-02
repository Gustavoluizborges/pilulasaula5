def validarSenha(s):
    if len(s) < 8:
        return 'Senha inválida, muito curta'
    
    temNumero = False
    temMaiuscula = False

    for c in s:
        if c == ' ':
            return "Erro: não pode conter espaço"
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <='Z':
            temMaiuscula = True
    if temNumero == False:
        return "Precisa de pelo menos um número"
    if not temMaiuscula:
        return "Precisa de pelo menos uma letra máiuscula"

#main
senha = input('Digite a senha: ')
r = validarSenha(senha)
print(r)
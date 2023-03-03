import re


def is_valid_cnpj(cnpj):
    pattern = r'^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$'
    return bool(re.match(pattern, cnpj))

def is_valid_cep(cep):
    if not re.match(r'^\d{8}$', cep):
        return False
    return True


def is_valid_telephone(telefone):
    pattern = r'^\(\d{2}\) \d{4}\-\d{4}$'
    return bool(re.match(pattern, telefone))


def is_valid_email(email):
    if not re.match(r'^\S+@\S+\.\S+$', email):
        return False
    return True

import re
import validate_docbr as docbr

def nome_valido(nome):
    return nome.replace(' ', '').isalpha()

def cpf_valido(cpf):
    return docbr.CPF().validate(cpf)

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """verifica se o celular é valido -> 11 99999-9999"""
    return re.findall('[0-90]{2} [0-9]{5}-[0-9]{4}', celular)
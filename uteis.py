###############################################################################

# suporte ao uso de regex
import re

###############################################################################

def validar_telefone( telefone ):
  pass

def formatar_telefone( telefone ):
  pass

def validar_cpf(cpf: str) -> bool:
  # Verifica a formatação do CPF
  # match = re.match(r"/^[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}/", cpf)
  # if not match:
  #   return False

  # Obtém apenas os números do CPF, ignorando pontuações
  numbers = [int(digit) for digit in cpf if digit.isdigit()]

  # Verifica se o CPF possui 11 dígitos:
  if len(numbers) != 11:
    return False

  # Validação do primeiro dígito verificador:
  sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
  expected_digit = (sum_of_products * 10 % 11) % 10
  if numbers[9] != expected_digit:
    return False

  # Validação do segundo dígito verificador:
  sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
  expected_digit = (sum_of_products * 10 % 11) % 10
  if numbers[10] != expected_digit:
    return False

  return True

def formatar_cpf(cpf: str) -> str:
  return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11])

def validar_uf(uf):
  pass

def formatar_uf(uf):
  pass
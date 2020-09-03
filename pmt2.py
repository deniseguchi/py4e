# Cálculo do pagamento
def computepay(h,r):
  if h > 40:
    h = 40 + (h-40)*1.5
  payment = h*r
  return payment

# Recebendo os dados de horas e salário
hrs = input("Enter Hours:")
h = float(hrs)
rates = input("Enter rate: ")
r = float(rates)

# Print dos resultados
p = computepay(h,r)
print("Pay",p)

hrs = input("Enter Hours:")
h = float(hrs)
rates = input("Enter rate:")
rate = float(rates)
if h > 40:
  h = 40 + (h-40)*1.5
print(h*rate)

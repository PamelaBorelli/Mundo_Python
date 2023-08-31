cidade = str(input("Em que cidade vc nasceu?: ")).strip()

print(cidade[:5] == 'Santo' or cidade[:5] == 'santo' )
print(cidade[:5].upper() == 'SANTO'  )
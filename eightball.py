from random import randint

eightball = [" Ano"," Ne"," Možná"," Spíš ne"," Czechbol říká, že ne"," Je vyšší šance, že dostaneš ban."," Smrdí ti nohy"," Zeptej se později"," Opravdu? Ne."," Zítra ráno"," Ano... i když spíš ne.",":kek:"]
print(" Hello there, zeptej se mě na něco.\n\n PS: Až tě přestanu bavit, ukonči mě příkazem 'exit'.\n")

exitprog = False
while exitprog != True:
    a = input()
    if a == 'exit':
        exitprog = True
    else:
        print(eightball[randint(0,len(eightball)-1)])

import subprocess

path = input("Inserisci il path del programma: ")
n = input("Quante istanze del programma avviare: ")

for i in range(int(n)):
    subprocess.Popen([path])
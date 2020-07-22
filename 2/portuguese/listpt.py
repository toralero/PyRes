import random

turma = ["Ana", "Bernardo", "Constança"]
print("O/A primeiro/a estudante da lista é", turma[0])
print("O/A último/a estudante da lista é", turma[-1])
print("A turma tem", len(turma), "estudantes")
print("turma =", turma)
print("-------")
print("Alguém vai estudar para outra escola")
randn = random.randint(0,2)
print("Adeus, ", turma[randn])
turma.pop(randn)
print("Agora a turma tem", len(turma), "estudantes")
print("turma =", turma)
print("-------")
print("Vamos ter um novo aluno.")
print("O nome dele é Daniel")
turma.append("Daniel")
print("turma =", turma)
print("-------")
print("O Daniel decidiu mudar com o Emílio da outra turma")
turma[-1] = "Emílio"
print("turma =", turma) 

from Bio import SeqIO

for fasta in SeqIO.parse("my_seq.fasta","fasta"):
    #Imprime o cabeçalho do arquivo
    print(fasta.id)
    #Imprime a sequência
    print(fasta.seq)

sequence="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(sequence)
print("\nprinting the count of each")
#A count
A=sequence.count("A")
print("the count of A is: ",A)
#T count
T=sequence.count("T")
print("the count of lsp is: ",T)
AT_content=(A+T)/len(sequence)
print("The content of AT is: ",AT_content)
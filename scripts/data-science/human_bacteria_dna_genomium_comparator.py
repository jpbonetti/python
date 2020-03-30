human_data = open("files/human_genomium.fasta").read()
bacteria_data = open("files/bacteria_genomium.fasta").read()

nucleo_bases_dna = ["A", "T", "G", "C"]
human_dna_sequence = {}
bacteria_dna_sequence = {}

def replace_all_invalid_caracters(text):
	return text.replace("\n", "").replace("\r", "")

def create_dna_sequence(nucleo_bases_dna):
	sequence = {}
	for a in nucleo_bases_dna:
		for b in nucleo_bases_dna:
			sequence[a + b] = 0	
	return sequence

human_data = replace_all_invalid_caracters(human_data)
human_dna_sequence = create_dna_sequence(nucleo_bases_dna)

bacteria_data = replace_all_invalid_caracters(bacteria_data)
bacteria_dna_sequence = create_dna_sequence(nucleo_bases_dna)

# COUNTING HUMAN DNA SEQUENCES
for i in range(len(human_data) - 1):
	human_dna_sequence[human_data[i] + human_data[i + 1]] += 1

# COUNTING BACTERIA DNA SEQUENCES
for i in range(len(bacteria_data) - 1):
	bacteria_dna_sequence[bacteria_data[i] + bacteria_data[i + 1]] += 1

print("HUMAN DNA SEQUENCE")
print(human_dna_sequence)
print("BACTERIA DNA SEQUENCE")
print(bacteria_dna_sequence)
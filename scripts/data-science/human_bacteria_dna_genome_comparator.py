human_data = open("files/data/human_genome.fasta").read()
bacteria_data = open("files/data/bacteria_genome.fasta").read()
final_file = open("dna_genome_compared.html", "w")

nucleo_bases_dna = ["A", "T", "C", "G"]
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

def create_dna_presentation_struct(cards_title, final_file, dna_sequence):
	final_file.write("<div class='col-sm-4'>")
	final_file.write("<h1>" + cards_title + "</h1>")
	div_count_separator = 1;
	for i in dna_sequence:
		transparency_level = float(dna_sequence[i]) / float(max(dna_sequence.values()))
		
		final_file.write("<div style='width: 100px; border: 1px solid #111; height: 100px; float: left; " +
			" color: #fff; background-color: rgba(0, 0, 0, " + str(transparency_level) + "')>" + i + 
			"</div>")

		if div_count_separator % 4 == 0:
			final_file.write("<div style='clear: both'></div>")

		div_count_separator+=1
	final_file.write("</div>")

def create_header_html(final_file):
	final_file.write("<html lang='en'>");
	final_file.write("<head>");
	final_file.write("<meta name='viewport' content='width=device-width, initial-scale=1'>");
	final_file.write("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'>");
	final_file.write("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>");
	final_file.write("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js'></script>");
	final_file.write("</head>");

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

#HTML
create_header_html(final_file)

final_file.write("<body>");
final_file.write("<div class='row'>")

create_dna_presentation_struct("HUMAN", final_file, human_dna_sequence)
create_dna_presentation_struct("BACTERIA", final_file, bacteria_dna_sequence)

final_file.write("</div>")

final_file.close()
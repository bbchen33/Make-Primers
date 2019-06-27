def calculate_Tm(input_sequence):
	input_sequence = input_sequence.upper()
	Tm = int(0)
	for nucleotide in input_sequence:
		if nucleotide == 'A':
			Tm += 2
		elif nucleotide == 'T':
			Tm += 2
		else:
			Tm += 4
	return Tm

def make_primers(input_sequence, length, Tm):
	input_sequence = input_sequence.upper()
	input_sequence_list = list(input_sequence)
	iteration_length = len(input_sequence_list) - length + 1
	list_of_primer = []
	for i in range(iteration_length):
		list_of_primer.append("".join(input_sequence_list[i:i+length]))
	
	primer_Tm_dict = {}
	for primer in list_of_primer:
		if calculate_Tm(primer) > Tm:
			primer_Tm_dict[primer] = [calculate_Tm(primer),0]
	
	for primer in primer_Tm_dict:
		primer_Tm_dict[primer][1] = input_sequence.find(primer)
	
	import pandas
	primer_Tm_location_df = pandas.DataFrame(primer_Tm_dict)
	primer_Tm_location_df = primer_Tm_location_df.transpose()
	primer_Tm_location_df.columns = ['Tm', 'location',]
	return primer_Tm_location_df

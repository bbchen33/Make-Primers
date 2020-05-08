def calculate_Tm(input_sequence): # simple function to calculate Tm based on the DNA sequence
	input_sequence = input_sequence.upper()
	Tm = 0
	for nucleotide in input_sequence:
		if nucleotide in ['A','T']:
			Tm += 2
		else:
			Tm += 4
	return Tm

import pandas
def make_primers(input_sequence, length, Tm):
	input_sequence = input_sequence.upper()
	iteration_length = len(input_sequence) - length + 1 # how many times the window size of the assigned primer length will iterate
	list_of_primer = []
	primer_Tm_dict = {}
	for i in range(iteration_length):
		primer = input_sequence[i:i+length]
		if calculate_Tm(primer) >= Tm:
			primer_Tm_dict[''.join(primer)] = [calculate_Tm(primer), 0]

	if len(primer_Tm_dict) == 0:
		return "No primers could be found with the given restrains. Try increasing the primer length or lowering the Tm"

	for primer in primer_Tm_dict:
		primer_Tm_dict[primer][1] = input_sequence.find(primer) # find the primer location
		primer_Tm_location_df = pandas.DataFrame(primer_Tm_dict) # transform the dictionary to pandas dataframe
		primer_Tm_location_df = primer_Tm_location_df.transpose()
		primer_Tm_location_df.columns = ['Tm', 'location']
	return primer_Tm_location_df


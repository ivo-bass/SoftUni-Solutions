def maximum_number_for_shell(index):
	shell = index + 1
	maximum = 2 * (shell ** 2)
	return maximum


def fill_atoms_shell(shells_list, electrons):
	curr_index = len(shells_list)
	maximum = maximum_number_for_shell(curr_index)
	shells_list.append(0)  # Adding new empty shell
	while shells_list[curr_index] < maximum:
		if not electrons:
			break
		shells_list[curr_index] += 1
		electrons -= 1
	if electrons:
		fill_atoms_shell(shells_list, electrons)
	return shells_list


given_electrons = int(input())
atoms_shells = []
print(fill_atoms_shell(atoms_shells, given_electrons))

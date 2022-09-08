mass_array = [57, 71, 87, 97, 99, 101, 103, 113,
              114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def read_exp_spectrum():

    spectrum = []
    file = open("input", "r")
    text = ""
    masses = file.read().split()
    # print(masses)

    for mass in masses:
        spectrum.append(int(mass))

    # print(spectrum)
    file.close()
    return spectrum


def masses_in_spectrum(spectrum):
    shared = []

    for mass in spectrum:

        if mass in mass_array:

            if mass in shared:
                continue
            else:
                shared.append(mass)

    return shared


def build_candidate(shared):
    table = []

    for mass in shared:
        table.append(str(mass))
    return table


def expand(peptides, shared):
    temp = []

    for peptide in peptides:
        # print(peptide)
        for mass in shared:
            temp.append(peptide + [mass])

    # print(temp)
    return temp

def cyclospectrum(peptide):
    prefixMass = [0]

    for i in range(0, len(peptide)):
        for j in range(0, len(mass_array)):
            if mass_array[j] == peptide[i]:

                prefixMass.append(prefixMass[i] + mass_array[j])

    peptideMass = prefixMass[len(peptide)]
    cyclic = [0]
    for i in range(0,len(peptide)):
        for j in range(i+1, len(peptide)+1): 

            if i > 0 and j < len(peptide):
                cyclic.append(peptideMass - (prefixMass[j] - prefixMass[i]))
            #else: 
            cyclic.append(prefixMass[j] - prefixMass[i])
    cyclic.sort()

    return cyclic


def is_Consistent(peptide, spectrum):

    # if sum(peptide) > spectrum[-1] - 57:
    #     return False

    linear = linear_spectrum(peptide)

    for mass in linear:
        if mass not in spectrum:
            return False

    return True


def check_mass_greater(peptides, parent_mass):

    good_peps = []

    for peptide in peptides:

        if sum(peptide) <= parent_mass:
            good_peps.append(peptide)

    return good_peps

# following code from book


def linear_spectrum(peptide):
    prefixMass = [0]

    for i in range(len(peptide)):
        prefixMass.append(prefixMass[i] + peptide[i])

    linearSpec = [0]

    for i in range(len(peptide)):
        for j in range(i+1, len(peptide) + 1):
            linearSpec.append(prefixMass[j] - prefixMass[i])
    linearSpec.sort()

    return linearSpec


def cyclopeptide_sequencing(shared, spectrum):

    pep_set = set()
    peptides = [[]]
    parent_mass = spectrum[-1]

    while peptides:

        peptides = expand(peptides, shared)
        peptides = check_mass_greater(peptides, parent_mass)

        for peptide in peptides:
            if sum(peptide) > parent_mass:
                peptides.remove(peptide)
                continue

            if sum(peptide) == parent_mass:
                if cyclospectrum(peptide) == spectrum:
                    pep_set.add("-".join(map(str,peptide)))
                temp = peptides [:]
                temp.remove(peptide)
                peptides = temp
  
            elif not is_Consistent(peptide, spectrum):
                temp = peptides[:]
                temp.remove(peptide)
                peptides = temp
           

    return pep_set


spectrum = read_exp_spectrum()

shared = masses_in_spectrum(spectrum)
# print(shared)

table = build_candidate(shared)
# print(table)

cyclo = cyclopeptide_sequencing(shared, spectrum)

output = open("output", "w")
answer = " ".join(cyclo)
output.write(answer)
output.close()
print(answer)



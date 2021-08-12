# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
        (
            ["8243"],
            ["Introduce el tiempo: ", "Horas: 2", "Minutos: 17", "Segundos: 23"],
            "Revisa tu código"
        ),
        # Test case 2
        (
            ["3521"],
            ["Introduce el tiempo: ", "Horas: 0", "Minutos: 58", "Segundos: 41"],
            "Revisa tu código"
        ),
        # Test case 3
        (
            ["5679"],
            ["Introduce el tiempo: ", "Horas: 1", "Minutos: 34", "Segundos: 39"],
            "Revisa tu código"
        )
]
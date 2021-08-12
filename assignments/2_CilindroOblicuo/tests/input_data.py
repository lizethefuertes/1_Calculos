# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
        (
            ["5", "2", "3"],
            ["Radio: ", "Altura 1: ", "Altura 2: ", "Volumen: 196.35"],
            "Revisa tu código"
        ),
    # Test case 2
        (
            ["2.5", "4.2", "8.6"],
            ["Radio: ", "Altura 1: ", "Altura 2: ", "Volumen: 125.66"],
            "Revisa tu código"
        ),
    # Test case 3
        (
            ["3.1", "5.7", "9.4"],
            ["Radio: ", "Altura 1: ", "Altura 2: ", "Volumen: 227.94"],
            "Revisa tu código"
        )
]
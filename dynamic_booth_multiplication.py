import time

# Function to count bit transitions in multiplier
def count_bit_transitions(q_bin):
    count = 0
    for i in range(1, len(q_bin)):
        if q_bin[i] != q_bin[i - 1]:
            count += 1
    return count

# Helper: Two's complement for binary string
def twos_complement(bstr):
    inverted = ''.join('1' if bit == '0' else '0' for bit in bstr)
    return bin(int(inverted, 2) + 1)[2:].zfill(len(bstr))

# Booth Algorithm (Restoring and Non-Restoring versions)
def booth_algorithm(M, Q, n, restoring=True):
    A = '0' * n
    Q_1 = '0'
    M_bin = format(M if M >= 0 else (1 << n) + M, f'0{n}b')
    negM_bin = twos_complement(M_bin)
    Q_bin = format(Q if Q >= 0 else (1 << n) + Q, f'0{n}b')

    steps = 0
    for _ in range(n):
        steps += 1
        last_two = Q_bin[-1] + Q_1

        if last_two == '10':
            if restoring:
                A = bin((int(A, 2) - int(M_bin, 2)) & ((1 << n) - 1))[2:].zfill(n)
            else:
                A = bin((int(A, 2) - int(M_bin, 2)) & ((1 << n) - 1))[2:].zfill(n)
        elif last_two == '01':
            if restoring:
                A = bin((int(A, 2) + int(M_bin, 2)) & ((1 << n) - 1))[2:].zfill(n)
            else:
                A = bin((int(A, 2) + int(M_bin, 2)) & ((1 << n) - 1))[2:].zfill(n)

        # Arithmetic right shift
        combined = A + Q_bin + Q_1
        shifted = combined[0] + combined[:-1]
        A = shifted[:n]
        Q_bin = shifted[n:2*n]
        Q_1 = shifted[-1]

    final_binary = A + Q_bin
    if final_binary[0] == '1':
        final_result = -((1 << (2 * n)) - int(final_binary, 2))
    else:
        final_result = int(final_binary, 2)

    return final_result, steps

# Main Program
if __name__ == "__main__":
    M = int(input("Enter Multiplicand (M): "))
    Q = int(input("Enter Multiplier (Q): "))

    n = 8  # 8-bit width for simplicity
    M_bin = format(M if M >= 0 else (1 << n) + M, f'0{n}b')
    Q_bin = format(Q if Q >= 0 else (1 << n) + Q, f'0{n}b')

    transitions = count_bit_transitions(Q_bin)
    chosen = "Restoring Booth" if transitions < (n // 2) else "Non-Restoring Booth"

    print("\n=====================================")
    print(f"Binary (M): {M_bin}")
    print(f"Binary (Q): {Q_bin}")
    print(f"Number of bit transitions in Q: {transitions}")
    print(f"Chosen Algorithm (based on bit pattern): {chosen}")
    print("=====================================\n")

    # Run chosen algorithm
    start_time = time.time()
    if chosen == "Restoring Booth":
        result, steps = booth_algorithm(M, Q, n, restoring=True)
    else:
        result, steps = booth_algorithm(M, Q, n, restoring=False)
    exec_time = time.time() - start_time

    print("--- Executing Selected Algorithm ---")
    print(f"Final Result: {result}")
    print(f"Steps Taken: {steps}")
    print(f"Execution Time: {exec_time:.6f} seconds\n")

    # Comparison run for report analysis
    start_rest = time.time()
    r_result, r_steps = booth_algorithm(M, Q, n, restoring=True)
    time_rest = time.time() - start_rest

    start_non = time.time()
    nr_result, nr_steps = booth_algorithm(M, Q, n, restoring=False)
    time_non = time.time() - start_non

    print("-------------------------------------")
    print("Performance Comparison (for analysis)")
    print("-------------------------------------")
    print(f"Restoring Booth     -> Time: {time_rest:.6f}s, Steps: {r_steps}")
    print(f"Non-Restoring Booth -> Time: {time_non:.6f}s, Steps: {nr_steps}")
    print("-------------------------------------")
    print("Note: Bit pattern favored", chosen)
    print("      but actual execution times may vary slightly.")

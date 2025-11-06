# Dynamic Booth Multiplication (Restoring vs Non-Restoring)

## Architecture Explanation
The architecture of the **Dynamic Booth Multiplication** system is designed to automatically decide whether to perform **Restoring Booth multiplication** or **Non-Restoring Booth multiplication** based on the bit pattern of the multiplier.

The process begins when the user inputs the **multiplicand** and **multiplier**. Both values are converted into binary form.  
Then, the **Bit Transition Analyzer** examines the multiplier to count the number of bit transitions (changes between 0 and 1).

Based on this count, the **Dynamic Selection Logic** decides:  
- If the bit transitions are low, the system uses **Restoring Booth**.  
- If the bit transitions are high, the system uses **Non-Restoring Booth**.

After the algorithm is selected, the corresponding multiplication method is executed. The **Result Generator** computes the product, step count, and execution time. Finally, the **Performance Analyzer** compares both methods and displays the result.

*(Block diagram image will be inserted here)*

---

## Tools Used – Hardware / Software
- **Hardware:** Standard computer or laptop (no additional hardware required)  
- **Software:**  
  - Python 3.x  
  - Visual Studio Code or any Python IDE  
  - GitHub (for version control)  
  - Command-line terminal for execution  

---

## Algorithm and Explanation

### Step 1 – Input Phase  
- User enters **Multiplicand (M)** and **Multiplier (Q)**.  
- Both values are converted to binary representation with a fixed bit length.

### Step 2 – Bit Pattern Analysis  
- The program counts the **number of bit transitions** in the multiplier (Q).  
- A transition occurs when a bit changes from 0 to 1 or 1 to 0.

### Step 3 – Dynamic Selection  
- If the number of transitions is less than or equal to a threshold, the program selects **Restoring Booth**.  
- Otherwise, it selects **Non-Restoring Booth**.

### Step 4 – Booth Multiplication Execution  
- The chosen algorithm performs multiplication step-by-step, using shift and add/subtract operations.  
- Partial products and accumulator values are updated each iteration.

### Step 5 – Output and Comparison  
- The product, step count, and execution time are displayed.  
- A comparison table shows the performance metrics of both algorithms.

---

## Evaluation Metrics

| Metric                  | Description                                         |
|-------------------------|-----------------------------------------------------|
| **Execution Time**       | Measures how fast each algorithm completes.          |
| **Step Count**           | Number of internal iterations performed.             |
| **Bit Transitions**      | Used to predict algorithm efficiency.                |
| **Algorithm Selection Accuracy** | Whether the chosen algorithm was optimal for that input.|

---

## Results Findings & Explanation
The system effectively determines which Booth multiplication method is more suitable based on bit patterns:  
- For low bit transitions, **Restoring Booth** performs well.  
- For inputs with highly alternating bits, **Non-Restoring Booth** tends to execute faster.  

Both methods produce the correct product, but the dynamic selection optimizes computation time depending on the input pattern.  

This confirms that using bit-pattern analysis as a heuristic can improve multiplication efficiency by selecting the appropriate algorithm dynamically.

---

## Conclusion & Future Work
The dynamic algorithm successfully selects between **Restoring** and **Non-Restoring Booth** multiplication methods based on bit transition analysis, providing optimized performance for different binary inputs.

### Future Enhancements
- Extend support to signed 16-bit and 32-bit numbers.  
- Develop a GUI for visualizing step-by-step multiplication.  
- Integrate the algorithm into hardware simulators such as FPGA or Verilog-based systems.  
- Use machine learning to predict the best algorithm based on input patterns.

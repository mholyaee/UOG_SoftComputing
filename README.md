# Genetic Algorithm for the 0/1 Knapsack Problem

A simple, educational implementation of a **Genetic Algorithm (GA)** in Python to solve the 0/1 Knapsack Problem.

This project demonstrates the main steps of a standard Genetic Algorithm using basic Python features and no external dependencies.

## 1. Overview

The 0/1 Knapsack Problem involves selecting items to maximize their total value without exceeding a given weight capacity.

Each item has:
- A weight
- A value

An item can either be selected (`1`) or not selected (`0`).

The objective is to maximize the total value while satisfying the capacity constraint.

## 2. Problem Instance

This implementation uses a predefined example with eight items.

| Item | Weight | Value |
|---:|---:|---:|
| 1 | 2 | 6 |
| 2 | 3 | 5 |
| 3 | 5 | 12 |
| 4 | 4 | 8 |
| 5 | 7 | 14 |
| 6 | 1 | 3 |
| 7 | 6 | 10 |
| 8 | 3 | 7 |

**Knapsack capacity:** 15

## 3. Genetic Algorithm Features

The implementation includes the following components:

- **Chromosome representation:** Binary list
- **Initial population:** Randomly generated chromosomes
- **Fitness function:** Total value with a penalty for exceeding capacity
- **Parent selection:** Roulette-wheel selection with replacement
- **Crossover:** One-point crossover
- **Mutation:** Bit-flip mutation, changing one randomly selected bit when mutation occurs
- **Replacement:** Generational replacement without elitism
- **Stopping criterion:** Fixed number of generations
- **Reproducibility:** Fixed random seed

The algorithm also tracks the best feasible solution found during the search.

## 4. Requirements

- Python 3
- No external libraries are required.

The program uses Python's built-in `random` module.

## 5. Installation and Execution

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR-REPOSITORY
```

Run the program:

```bash
python knapsack_ga.py
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

## 6. Algorithm Parameters

The following parameters can be modified in the source code.

| Parameter | Default value | Description |
|---|---:|---|
| `POPULATION_SIZE` | 20 | Number of chromosomes in the population |
| `CROSSOVER_RATE` | 0.8 | Probability of crossover for a pair of parents |
| `MUTATION_RATE` | 0.05 | Probability of mutation for each offspring |
| `MAX_GENERATIONS` | 100 | Maximum number of generations |
| `PENALTY` | 10 | Penalty coefficient for exceeding capacity |
| `random.seed(42)` | 42 | Random seed for reproducible runs |

## 7. Fitness Function

The fitness function is defined as:

\[
f(x)=V(x)-\lambda\max(0,W(x)-C)
\]

where:

- \(V(x)\) is the total value of the selected items.
- \(W(x)\) is their total weight.
- \(C\) is the knapsack capacity.
- \(\lambda\) is the penalty coefficient.

Feasible solutions receive their total value as fitness. Infeasible solutions receive a penalty proportional to the excess weight.

For roulette-wheel selection, negative fitness values are shifted when necessary. If all adjusted fitness values are zero, the algorithm selects parents uniformly at random.

## 8. Output

The program reports the following information for each generation:

- Best penalized fitness in the current population
- Best feasible solution value found so far

At the end, it displays:

- Best feasible chromosome
- Selected item numbers
- Total weight
- Total value
- An independent feasibility validation

If no feasible solution is found, the program reports this explicitly and displays the best penalized chromosome as a diagnostic result rather than presenting it as a valid solution.

## 9. Educational Notes

This project is intended for learning and experimentation.

**Important characteristics:**

- The algorithm is stochastic, although the fixed random seed makes the default run reproducible.
- No elitism is used; the best chromosome is tracked separately and is not automatically preserved in the population.
- The penalty coefficient affects the selection pressure toward feasible solutions.
- A Genetic Algorithm is a heuristic and does not guarantee that the global optimum will be found.
- The program uses a fixed example rather than reading problem instances from a file.

## 10. Suggested Experiments

Students can experiment with the algorithm by changing one parameter at a time:

1. Increase or decrease the population size.
2. Compare different crossover probabilities.
3. Experiment with mutation probabilities.
4. Change the penalty coefficient.
5. Increase the maximum number of generations.
6. Change the random seed and compare the results.
7. Modify item weights, values, and capacity.

Observe how these changes affect the search process and the best feasible solution found.

## License

Choose an appropriate open-source license before distributing or reusing this code. For example, the MIT License permits broad reuse while requiring preservation of the copyright and license notice.

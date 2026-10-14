
import random

# Problem data
weights = [2, 3, 5, 4, 7, 1, 6, 3]
values = [6, 5, 12, 8, 14, 3, 10, 7]
capacity = 15

# GA parameters
POPULATION_SIZE = 20
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05
MAX_GENERATIONS = 100
PENALTY = 10

random.seed(42)


# Calculate chromosome weight and value
def evaluate(chromosome):
    total_weight = 0
    total_value = 0

    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]

    return total_weight, total_value


# Calculate penalized fitness
def fitness(chromosome):
    total_weight, total_value = evaluate(chromosome)
    excess_weight = max(0, total_weight - capacity)

    return total_value - PENALTY * excess_weight


# Generate a random binary chromosome
def create_chromosome():
    chromosome = []

    for i in range(len(weights)):
        chromosome.append(random.randint(0, 1))

    return chromosome


# Create the initial population
def create_population():
    population = []

    for i in range(POPULATION_SIZE):
        population.append(create_chromosome())

    return population


# Select one parent using roulette-wheel selection
def select_parent(population):
    fitness_values = []

    for chromosome in population:
        fitness_values.append(fitness(chromosome))

    # Shift fitness values if any are negative
    minimum = min(fitness_values)

    if minimum < 0:
        fitness_values = [
            value - minimum for value in fitness_values
        ]

    total_fitness = sum(fitness_values)

    # If all adjusted fitness values are zero,
    # select uniformly at random
    if total_fitness == 0:
        return random.choice(population)

    # Roulette-wheel selection
    pick = random.uniform(0, total_fitness)
    current = 0

    for i in range(len(population)):
        current += fitness_values[i]

        if current >= pick:
            return population[i]

    return population[-1]


# One-point crossover
def crossover(parent1, parent2):
    child1 = parent1[:]
    child2 = parent2[:]

    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, len(parent1) - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

    return child1, child2


# Flip exactly one randomly selected bit with a given probability
def mutate(chromosome):
    chromosome = chromosome[:]

    if random.random() < MUTATION_RATE:
        position = random.randint(0, len(chromosome) - 1)
        chromosome[position] = 1 - chromosome[position]

    return chromosome


# Update the best feasible solution found so far
def update_best_feasible(population, best_solution):
    for chromosome in population:
        total_weight, total_value = evaluate(chromosome)

        if total_weight <= capacity:
            if (best_solution is None or
                    total_value > evaluate(best_solution)[1]):
                best_solution = chromosome[:]

    return best_solution


# Main genetic algorithm
def genetic_algorithm():
    population = create_population()
    best_feasible = None

    # Check the initial population
    best_feasible = update_best_feasible(
        population, best_feasible
    )

    for generation in range(1, MAX_GENERATIONS + 1):
        new_population = []

        # Generate a new population of the same size
        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.append(child1)
            new_population.append(child2)

        # Keep exactly POPULATION_SIZE chromosomes
        population = new_population[:POPULATION_SIZE]

        # Track the best feasible solution across all generations
        best_feasible = update_best_feasible(
            population, best_feasible
        )

        # Best penalized fitness in the current population
        best_current = max(population, key=fitness)
        best_current_fitness = fitness(best_current)

        # Best feasible value found so far
        if best_feasible is None:
            best_value_text = "None"
        else:
            best_value_text = str(evaluate(best_feasible)[1])

        print(
            f"Generation {generation:3d} | "
            f"Best current fitness: {best_current_fitness:6.1f} | "
            f"Best feasible value so far: {best_value_text}"
        )

    return population, best_feasible


# Run the algorithm
final_population, best_feasible = genetic_algorithm()


# Display and independently validate the final result
print("\n========== FINAL RESULT ==========")

if best_feasible is not None:
    total_weight, total_value = evaluate(best_feasible)

    print("Best chromosome:", best_feasible)

    selected_items = []

    for i in range(len(best_feasible)):
        if best_feasible[i] == 1:
            selected_items.append(i + 1)

    print("Selected items:", selected_items)
    print("Total weight:", total_weight)
    print("Total value:", total_value)

    # Independent feasibility check
    check_weight = sum(
        weights[i]
        for i in range(len(best_feasible))
        if best_feasible[i] == 1
    )

    check_value = sum(
        values[i]
        for i in range(len(best_feasible))
        if best_feasible[i] == 1
    )

    print("\nValidation:")
    print("Recalculated weight:", check_weight)
    print("Recalculated value:", check_value)
    print("Capacity:", capacity)
    print("Feasible:", check_weight <= capacity)

else:
    print("No feasible solution was found.")

    # Show the best penalized chromosome for diagnosis
    best_infeasible = max(final_population, key=fitness)
    total_weight, total_value = evaluate(best_infeasible)

    print("Best penalized chromosome:", best_infeasible)
    print("Total weight:", total_weight)
    print("Total value:", total_value)
    print("Penalized fitness:", fitness(best_infeasible))
    print("This chromosome is not a valid feasible solution.")

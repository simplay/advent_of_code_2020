global accumulator


class Program:
    def __init__(self, instructions: list):
        self.instructions = instructions
        self.accumulator = 0
        self.regular_termination = False

    def update_accumulator(self, value):
        self.accumulator += value
        return 1

    def execute(self):
        encountered_program_counters = []

        supported_operations = {
            "acc": lambda argument: self.update_accumulator(argument),
            "jmp": lambda argument: argument,
            "nop": lambda _: 1
        }

        program_counter = 0

        while True:
            operation, argument = self.instructions[program_counter].split(" ")
            # print(f"{program_counter}: {operation} {argument}")

            program_counter_offset = supported_operations[operation](int(argument))
            program_counter += program_counter_offset

            # regular program termination
            if program_counter > len(self.instructions) - 1:
                self.regular_termination = True
                break

            if (encountered_program_counters.__contains__(program_counter)):
                break

            encountered_program_counters.append(program_counter)

        return self.accumulator


if __name__ == "__main__":
    with open("input.txt") as file:
        instructions = file.read().splitlines()
        accumulator = Program(instructions).execute()
        print("Task 1:", accumulator)

        instruction_swap_table = {
            "jmp": "nop",
            "nop": "jmp"
        }

        for program_counter in range(len(instructions)):
            copied_instructions = instructions.copy()

            operation, argument = copied_instructions[program_counter].split(" ")
            if operation == "acc":
                continue

            copied_instructions[program_counter] = f"{instruction_swap_table[operation]} {argument}"
            program = Program(copied_instructions)
            accumulator = program.execute()
            if program.regular_termination:
                print("Task 2:", accumulator)

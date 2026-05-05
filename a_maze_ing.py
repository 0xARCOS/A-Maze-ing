import sys
from pathlib import Path
from mazegen import get_config, MazeGenerator, visualize, color_generator, RESET


def main(list: list) -> None:
    if len(sys.argv) != 2:
        print("Must have one argument")
        return
    try:
        validated_config = get_config(Path(sys.argv[1]))
        my_gen = MazeGenerator()
        action = "1"
        show = 0
        color = color_generator()
        color_now = next(color)
        while action != "4":
            if action == "1":
                my_gen.generate_perfect(
                    validated_config.width,
                    validated_config.height,
                    validated_config.entry,
                    validated_config.exit,
                    validated_config.output_file,
                    validated_config.perfect,
                    validated_config.seed
                    )
                grid = visualize(Path(validated_config.output_file))
                output = grid[0]
                show = 0
            elif action == "2":
                if show == 0:
                    output = grid[1]
                    show = 1
                else:
                    output = grid[0]
                    show = 0
            elif action == "3":
                color_now = next(color)
            else:
                output = "Invalid instruction."
            print(color_now + output + RESET)
            print(
                "=== Instructions ===",
                "1. Re-generate maze",
                "2. Show/Hide solution path",
                "3. Change maze colors",
                "4. Quit",
                sep="\n"
            )
            action = input("Choice (1-4):")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main(sys)

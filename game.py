from gameparts.parts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    game = Board()
    current_player = "X"
    running = True
    game.display()

    def save_result(str_result: str):
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(str_result + "\n")
        # file = open("results.txt", "a", encoding="utf-8")
        # file.write(str_result + "\n")
        # file.close()
        # return f"resultat uspeshno zapisan v fail"

    while running:
        print(f"Hod delaut {current_player}")

        while True:
            try:
                row = int(input("vvedite nomer stolbca: "))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input("vvedite nomer stroki: "))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != " ":
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    "Znachenie doljno bit neotricatelnym i menshe "
                    f"{game.field_size}."
                )
                print("Pojaluysta, vvedite znacheniya dlya stroki i stolbca zanovo.")
                continue
            except CellOccupiedError:
                print("yacheika zanyata")
                print("Vvedite drugie koordinaty.")
                continue
            except ValueError:
                print("Bukvi vvodit nelzya. Tolko chisla.")
                print("Pojaluysta, vvedite znacheniya dlya stroki i stolbca zanovo.")
                continue
            except Exception as e:
                print(f"Voznikla oshibka: {e}")
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            result = f"Pobedili {current_player}."
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = "Nichya!"
            print(result)
            save_result(result)
            running = False

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()

"""One Line, One Laugh: Roast Your Fridge entry: writes one original fridge roast to /output/entry.txt."""
import os

LINE = "My fridge has two settings: Arctic expedition and lukewarm soup — there is no in-between."

def main():
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        path = out
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)

if __name__ == "__main__":
    main()

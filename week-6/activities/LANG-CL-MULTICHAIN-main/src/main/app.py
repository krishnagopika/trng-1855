from src.main.lab import final_chain_invoke

def main():
    # Expected Behavior: Entering a movie title should result in
    # a list of movies that share 3 common actors being generated and printed
    print(final_chain_invoke(input("Enter a movie=> ")))

if __name__ == "__main__":
    main()

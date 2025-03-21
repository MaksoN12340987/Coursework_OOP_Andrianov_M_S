from src.get_api_hh import HH


def main():
    item_hh = HH("")
    result = item_hh.load_vacancies(keyword="")
    print(result)

if __name__ == "__main__":
    main()

import directory_reader
import kattis_scrapper
from datetime import date

Tłumaczenia = {
    'January': 'Styczeń',
    'February': 'Luty',
    'March': 'Marzec',
    'April': 'Kwiecień',
    'May': 'Maj',
    'June': 'Czerwiec',
    'July': 'Lipiec',
    'August': 'Sierpień',
    'September': 'Wrzesień',
    'October': 'Październik',
    'November': 'Listopad',
    'December': 'Grudzień'
}
current_date = date.today()
month_name_english = current_date.strftime("%B")
month_name_polish = Tłumaczenia.get(month_name_english, month_name_english)
formated_date = current_date.strftime(f"{month_name_polish} %d, %Y")

inputSource = directory_reader.ListingDirectory(r'C:\Users\2001s\PycharmProjects\Giraffe\Kattis')
dictSource = inputSource.make_dictionary()

def linkProblems(problem_name):
    problem_link = 'https://open.kattis.com/problems/{}'.format(problem_name)
    return problem_link

def linkSolutions(problem_name, solution):
    if ' ' in problem_name:
        problem_name = problem_name.replace(' ', '%20')
    link = 'https://github.com/WyginaczBlachy/Kattis/blob/main/Kattis/{}/{}'.format(problem_name, solution)
    extension = None
    if '.py' in solution:
        extension = 'Python'
    if '.cpp' in solution:
        extension = 'C++'
    readme_link = '[{}]({})'.format(extension, link)
    return readme_link

def writingReadme(option):
    if option.lower() == 'y':
        scrapper = kattis_scrapper.PointScrapper()
        try:
            with open('README.md', 'w', encoding='UTF-8') as f:
                tmp = 0
                f.write('# Kattis rozwiązania \n')
                f.write('Rozwiazania problemów z [Kattis](https://open.kattis.com/). \n\n')
                f.write('Zaktualizowano: ' + formated_date + '\n\n')
                if option.lower() == 'y':
                    f.write(' | LP | Problem | Rozwiązanie | Trudność |\n')
                    f.write(' | -- | ------- | ----------- | -------- |\n')
                else:
                    f.write(' | LP | Problem | Rozwiązanie |\n')
                    f.write(' | -- | ------- | ----------- |\n')
                for key in dictSource:
                    list_tmp = dictSource[key]
                    tmp += 1
                    f.write(' | ' + str(tmp))
                    target = list_tmp[0].split('.')
                    target = target[0]
                    problem_link = linkProblems(target)
                    f.write(' | [{}]({}) | '.format(key, problem_link))
                    for i in range(len(list_tmp)):
                        if i == len(list_tmp) - 1:
                            f.write(linkSolutions(key, list_tmp[i]) + ' ')
                        else:
                            f.write(linkSolutions(key, list_tmp[i]) + ', ')
                    f.write('|')
                    if option.lower() == 'y':
                        f.write(scrapper.getPoints(problem_link))
                        f.write('|')
                        print(problem_link)
                        print(f"pobieranie {tmp} z {len(dictSource)}")
                    f.write('\n')
                f.write('\n\n')

                f.write('## Autor:\n')
                f.write('- [WyginaczBlachy](https://open.kattis.com/users/wyginaczblachy)')

                print('\nREADME.MD zaktulizowane pomyślnie \n')
                userExit = input('Wciśnij ENTER, żeby zakończyć')
        except IOError as e:
            print(f"Error writing to file: {e}")

if __name__ == '__main__':
    userInput = input("Czy chcesz pokazać poziom trudności? (y/n)? ")
    writingReadme(userInput)
    
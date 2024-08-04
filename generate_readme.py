import directory_reader
import kattis_scrapper
from datetime import date

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
                f.write('Zaktualizowano: ' + str(date.today().strftime("%B %d, %Y")) + '\n\n')
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
                        print(f"scrapping {tmp} from total {len(dictSource)}")
                    f.write('\n')
                f.write('\n\n')

                f.write('## Autor:\n')
                f.write('- [Wyginacz Blachy](https://open.kattis.com/users/WyginaczBlachy)')

                print('\nREADME.MD Successfully Generated/Updated \n')
                userExit = input('Press ENTER to exit..')
        except IOError as e:
            print(f"Error writing to file: {e}")

if __name__ == '__main__':
    userInput = input("Do you want to show 'Difficulty' or not (y/n)? ")
    writingReadme(userInput)
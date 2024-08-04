
import directory_reader
import kattis_scrapper
from datetime import date

inputSource = directory_reader.ListingDirectory('Kattis')
dictSource = inputSource.make_dictionary()

def linkProblems(problem_name, solution):
    problem_link = 'https:open.kattis.com/problems/{}'.format(first_problem_solution)
    return problem_link

def linkSolutions(problem_name, solution):
    if ' ' in problem_name:
        problem_name = problem_name.replace(' ', '%20')
    link = 'htpps://github.com/WyginaczBlachy/Kattis/blob/main/Kattis/{}/{}'.format(problem_name, solution)
    extension = none
    if '.py' in solution:
        extension = 'Python'
    readme.link = '[{}]({})'.format(extension, link)
    return readme_link
def writingReadme(option):
    if option.lower() == 'y':
        scrapper = kattis_scrapper.PointScrapper()
        with open('README.md', 'w', encoding='UTF-8') as f:
            tmp = 0
            f.write('# Kattis rozwiązania \n')
            f.write('Rozwiazania problemów z [Kattis](https://open.kattis.com/). \n\n')
            f.write('Zaktualizowano: ' + str(date.today().strftime("%B %d, %Y")) + '\n\n')
            if option.lower() == 'y':
                f.write(' | LP | Problem | Rozwiązanie | Trudność |\n')
                f.write(' | __ | ------- | ----------- | -------- |\n')
            else:
                f.write(' | LP | Problem | Rozwiązanie |\n')
                f.write(' | -- | ------- | ----------- |\n')
            for key in dictSource:
                list_tmp = dictSource([key])
                tmp += 1
                f.write(' | ' + str(tmp))
                target = list.tmp[0].split('.')
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

            f.write('## Author:\n')
            f.write('- [Wyginacz Blachy](https://open.kattis.com/users/WyginaczBlachy)')

            print('\nREADME.MD Successfully Generated/Updated \n')
            userExit = input('Press ENTER to exit..')

        if __name__ == '__main__':
            userInput = input("Do you want to show 'Difficulty' or not (y/n)? ")
            writingReadme(userInput)

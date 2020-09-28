__author__ = 'khrystyna'
import io
from retry import retry
import requests
from pycookiecheat import chrome_cookies
import json
import time
import autopep8
import re


class LeetCodeSession:

    LOGIN_URL = "https://leetcode.com/accounts/login/"
    PROBLEMS_URL = "https://leetcode.com/api/problems/algorithms/"
    SUBMISSIONS_URL = 'https://leetcode.com/api/submissions/'
    COOKIES = chrome_cookies(LOGIN_URL)
    DETAILS_URL = 'https://leetcode.com/submissions/detail/'
    TEMPLATE = re.compile('\\\\u0022distribution\\\\u0022: \[(.*)\]}')

    # Gets problems that were submitted and accepted for the logged in user
    def getProblems(self, status='ac'):

        problems = requests.get(self.PROBLEMS_URL, cookies=self.COOKIES)
        parsed_problems = json.loads(problems.content)
        accepted_problems = list(
            filter(
                lambda p: p["status"] == status,
                parsed_problems["stat_status_pairs"]
            )
        )
        problem_list = list(map(lambda x: Problem(x[0], x[1]), list(
            map(
                lambda p: (p["stat"]["question__title_slug"], p["stat"]),
                accepted_problems
            )
        )
        ))
        return problem_list

    # Gets all user's submissions to the problem
    @retry(ValueError, delay=1, backoff=2)
    def getSubmissions(self, problem):
        time.sleep(1)
        submissions = requests.get(
            LeetCodeSession.SUBMISSIONS_URL + problem.slug, cookies=LeetCodeSession.COOKIES)
        if submissions.status_code == 403:
            raise ValueError
        parsed_submissions = json.loads(submissions.content)
        submissions = list(
            map(lambda x: Submission(problem.get_id(), problem.slug, x),
                parsed_submissions['submissions_dump'])
        )
        return submissions

    # calculates percentile for submission of the problem
    def get_percentile(self, submission):
        details = requests.get(LeetCodeSession.DETAILS_URL+str(
            submission.get_id())+'/', cookies=LeetCodeSession.COOKIES).text
        numbers = (LeetCodeSession.TEMPLATE.search(details).group(1))
        numbers = numbers.replace('\\u0022', '').replace(
            '[', '').replace('], ', '|').replace(']', '')
        distribution = list(map(lambda x: list(
            map(lambda y: float(y), x.split(', '))), (numbers.split('|'))))
        runtime = submission.get_runtime()
        accum_value = 0
        for (time, percentile) in distribution:
            if time < runtime:
                accum_value += percentile
            else:
                return (100-accum_value)
        return None


class Problem:

    def __init__(self, slug, stat):
        self.slug = slug
        self.stat = stat

    def get_id(self):
        return self.stat['frontend_question_id']

    def get_title(self):
        return self.stat['question__title']


class Submission:

    def __init__(self, problem_id, problem_slug, submissions_dump):
        self.problem_id = problem_id
        self.problem_slug = problem_slug
        self.content = submissions_dump

    def get_code(self):
        return autopep8.fix_code(self.content['code'])

    def get_id(self):
        return self.content['id']

    def get_runtime(self):
        return float(self.content['runtime'].split()[0])


class Query:

    def __init__(self, lc_session):
        self.session = lc_session

    def best_submission(self, problem):
        submissions = self.session.getSubmissions(problem)
        best_submission = min(submissions,
                              key=lambda x: (float(x.content['runtime'].split()[0]) if x.content['runtime'] != 'N/A' else float('inf'),
                                             float(x.content['memory'].split()[0] if x.content['memory'] != 'N/A' else float('inf'))))
        return best_submission

    def file_best_submission(self, problem, path=''):
        best_subm = self.best_submission(problem)
        filepath = path+str(best_subm.problem_id)+'_'+problem.slug+'.py'
        filetitle = '# Problem Title: '+problem.get_title() + '\n' + \
            best_subm.get_code()+'\n'
        f = open(filepath, 'w+')

        f.write(filetitle)

        f.close()

    def try_again(self, n=5):
        submissions = []
        for problem in self.session.getProblems()[:10]:
            best_submission = self.best_submission(problem)
            submissions.append(
                [self.session.get_percentile(best_submission), best_submission])
        return list(map(lambda x: (x[1].problem_id, x[1].problem_slug), sorted(submissions)[:n]))


class API():
    def __init__(self):
        self.session = LeetCodeSession()
        self.query = Query(self.session)

    def fileProblems(self, n):
        for problem in self.session.getProblems()[:n]:
            self.query.file_best_submission(problem)
        return

    def practiceAgainProblems(self, n, path=''):
        tasks = self.query.try_again(n)
        problems = str(tasks)
        f = open(path+'PracticeMore'+'.txt', 'w+')

        f.write(problems)

        f.close()

        return


api = API()
api.practiceAgainProblems(4)
api.fileProblems()

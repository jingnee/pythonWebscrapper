from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file
#wanted_result = requests.get("https://www.wanted.co.kr/wdlist/518/674?country=kr&job_sort=job.latest_order&years=-1&locations=all") 

so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs + indeed_jobs
save_to_file(jobs)


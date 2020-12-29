from indeed import extract_indeed_pages, extract_indeed_jobs 
#wanted_result = requests.get("https://www.wanted.co.kr/wdlist/518/674?country=kr&job_sort=job.latest_order&years=-1&locations=all") 
last_indeed_pages = extract_indeed_pages() 
extract_indeed_jobs(last_indeed_pages)
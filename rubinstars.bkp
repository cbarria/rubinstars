from github import Github
import yaml
repoStars = {} 
g=Github()
repoList = ["freeCodeCamp/freeCodeCamp","996icu/996.ICU","EbookFoundation/free-programming-books"] 
for repoName in repoList:
	repo = g.get_repo(repoName)
	repoStars.update({repoName : repo.stargazers_count})
print(yaml.dump(repoStars, default_flow_style = False))	
